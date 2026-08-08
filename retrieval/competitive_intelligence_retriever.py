from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "competitive"


class CompetitiveIntelligenceRetriever:
    """
    Loads and filters local competitive-intelligence fixtures.
    Schema real confirmado via pandas.read_csv:
    institutions.csv, peers.csv, metrics.csv, insights.csv, sources.csv
    """

    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = Path(data_dir)

    def _load_csv(self, filename: str) -> pd.DataFrame:
        path = self.data_dir / filename
        return pd.read_csv(path) if path.exists() else pd.DataFrame()

    def load_institutions(self) -> pd.DataFrame:
        return self._load_csv("institutions.csv")

    def load_peers(self) -> pd.DataFrame:
        return self._load_csv("peers.csv")

    def load_metrics(self) -> pd.DataFrame:
        return self._load_csv("metrics.csv")

    def load_insights(self) -> pd.DataFrame:
        return self._load_csv("insights.csv")

    def load_sources(self) -> pd.DataFrame:
        return self._load_csv("sources.csv")

    def get_institution_options(self) -> list[str]:
        institutions = self.load_institutions()
        if institutions.empty or "InstitutionName" not in institutions.columns:
            return []
        return (
            institutions["InstitutionName"]
            .dropna().astype(str).str.strip().tolist()
        )

    def get_peer_options(self, base_institution_name: str) -> list[str]:
        institutions = self.load_institutions()
        peers = self.load_peers()

        required_inst = {"InstitutionName", "InstitutionId"}
        required_peers = {"BaseInstitutionId", "PeerInstitutionName", "PeerRank"}
        if (
            institutions.empty or peers.empty
            or not required_inst.issubset(institutions.columns)
            or not required_peers.issubset(peers.columns)
        ):
            return []

        base_rows = institutions[
            institutions["InstitutionName"].astype(str).str.strip() == base_institution_name
        ]
        if base_rows.empty:
            return []

        base_id = str(base_rows.iloc[0]["InstitutionId"]).strip()
        selected_peers = peers[
            peers["BaseInstitutionId"].astype(str).str.strip() == base_id
        ]
        return (
            selected_peers.sort_values("PeerRank")["PeerInstitutionName"]
            .dropna().astype(str).str.strip().tolist()
        )

    def get_metrics(self, base_institution_name: str, peer_name: str) -> dict[str, str]:
        institutions = self.load_institutions()
        peers = self.load_peers()
        metrics = self.load_metrics()

        needed = {
            "InstitutionName", "InstitutionId"
        }.issubset(institutions.columns) if not institutions.empty else False
        if not needed or peers.empty or metrics.empty:
            return {}

        base_rows = institutions[
            institutions["InstitutionName"].astype(str).str.strip() == base_institution_name
        ]
        if base_rows.empty:
            return {}
        base_id = str(base_rows.iloc[0]["InstitutionId"]).strip()

        peer_rows = peers[
            (peers["PeerInstitutionName"].astype(str).str.strip() == peer_name)
            & (peers["BaseInstitutionId"].astype(str).str.strip() == base_id)
        ]
        if peer_rows.empty:
            return {}
        peer_id = str(peer_rows.iloc[0]["PeerInstitutionId"]).strip()

        selected = metrics[
            (metrics["BaseInstitutionId"].astype(str).str.strip() == base_id)
            & (metrics["PeerInstitutionId"].astype(str).str.strip() == peer_id)
        ]

        result: dict[str, str] = {}
        for _, row in selected.iterrows():
            name = str(row["MetricName"]).strip()
            value = row["MetricValue"]
            unit = str(row["MetricUnit"]).strip()
            result[name] = f"{float(value):.1f}%" if unit == "percent" else str(value)
        return result

    def get_insight(self, base_institution_name: str, peer_name: str) -> dict[str, str]:
        institutions = self.load_institutions()
        peers = self.load_peers()
        insights = self.load_insights()

        if institutions.empty or peers.empty or insights.empty:
            return {}

        base_rows = institutions[
            institutions["InstitutionName"].astype(str).str.strip() == base_institution_name
        ]
        if base_rows.empty:
            return {}
        base_id = str(base_rows.iloc[0]["InstitutionId"]).strip()

        peer_rows = peers[
            (peers["PeerInstitutionName"].astype(str).str.strip() == peer_name)
            & (peers["BaseInstitutionId"].astype(str).str.strip() == base_id)
        ]
        if peer_rows.empty:
            return {}
        peer_id = str(peer_rows.iloc[0]["PeerInstitutionId"]).strip()

        selected = insights[
            (insights["BaseInstitutionId"].astype(str).str.strip() == base_id)
            & (insights["PeerInstitutionId"].astype(str).str.strip() == peer_id)
        ]
        if selected.empty:
            return {}

        row = selected.iloc[0]
        return {
            "takeaway": str(row["Takeaway"]),
            "recommendation": str(row["Recommendation"]),
            "confidence": str(row["Confidence"]),
            "source_id": str(row["SourceId"]),
        }

    def get_sources(self, source_ids: list[str]) -> list[str]:
        sources = self.load_sources()
        if sources.empty or not source_ids:
            return []
        selected = sources[
            sources["SourceId"].astype(str).isin(source_ids)
            & sources["Approved"].astype(str).str.lower().eq("true")
        ]
        return [f"[Source: {row['SourceName']}]" for _, row in selected.iterrows()]