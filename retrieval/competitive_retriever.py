from pathlib import Path

import pandas as pd


class CompetitiveRetriever:
    def __init__(self, data_dir: Path | None = None):
        root_dir = Path(__file__).resolve().parent.parent

        self.data_dir = data_dir or (root_dir / "data" / "competitive")

        self.institutions_path = self.data_dir / "institutions.csv"
        self.peers_path = self.data_dir / "peers.csv"
        self.metrics_path = self.data_dir / "metrics.csv"
        self.insights_path = self.data_dir / "insights.csv"
        self.sources_path = self.data_dir / "sources.csv"

    def _load_csv(self, path: Path) -> pd.DataFrame:
        if not path.exists():
            return pd.DataFrame()

        return pd.read_csv(path)

    def load_institutions(self) -> pd.DataFrame:
        return self._load_csv(self.institutions_path)

    def load_peers(self) -> pd.DataFrame:
        return self._load_csv(self.peers_path)

    def load_metrics(self) -> pd.DataFrame:
        return self._load_csv(self.metrics_path)

    def load_insights(self) -> pd.DataFrame:
        return self._load_csv(self.insights_path)

    def load_sources(self) -> pd.DataFrame:
        return self._load_csv(self.sources_path)

    def get_institution_options(self) -> list[str]:
        institutions = self.load_institutions()

        if institutions.empty:
            return []

        return (
            institutions["InstitutionName"]
            .dropna()
            .astype(str)
            .str.strip()
            .tolist()
        )

    def get_peer_options(self, base_institution_name: str) -> list[str]:
        institutions = self.load_institutions()
        peers = self.load_peers()

        if institutions.empty or peers.empty:
            return []

        base_rows = institutions[
            institutions["InstitutionName"].astype(str).str.strip()
            == base_institution_name
        ]

        if base_rows.empty:
            return []

        base_institution_id = base_rows.iloc[0]["InstitutionId"]

        return (
            peers[
                peers["BaseInstitutionId"].astype(str).str.strip()
                == str(base_institution_id).strip()
            ]
            .sort_values("PeerRank")["PeerInstitutionName"]
            .dropna()
            .astype(str)
            .str.strip()
            .tolist()
        )

    def get_metrics(
        self,
        base_institution_name: str,
        peer_name: str,
    ) -> dict[str, str]:
        institutions = self.load_institutions()
        peers = self.load_peers()
        metrics = self.load_metrics()

        base_rows = institutions[
            institutions["InstitutionName"].astype(str).str.strip()
            == base_institution_name
        ]

        peer_rows = peers[
            peers["PeerInstitutionName"].astype(str).str.strip()
            == peer_name
        ]

        if base_rows.empty or peer_rows.empty:
            return {}

        base_id = str(base_rows.iloc[0]["InstitutionId"]).strip()
        peer_id = str(peer_rows.iloc[0]["PeerInstitutionId"]).strip()

        selected = metrics[
            (metrics["BaseInstitutionId"].astype(str).str.strip() == base_id)
            & (metrics["PeerInstitutionId"].astype(str).str.strip() == peer_id)
        ].copy()

        result = {}

        for _, row in selected.iterrows():
            metric_name = str(row["MetricName"]).strip()
            value = row["MetricValue"]
            unit = str(row["MetricUnit"]).strip()

            if unit == "percent":
                result[metric_name] = f"{float(value):.1f}%"
            else:
                result[metric_name] = str(value)

        return result

    def get_insight(
        self,
        base_institution_name: str,
        peer_name: str,
    ) -> dict[str, str]:
        institutions = self.load_institutions()
        peers = self.load_peers()
        insights = self.load_insights()

        base_rows = institutions[
            institutions["InstitutionName"].astype(str).str.strip()
            == base_institution_name
        ]

        peer_rows = peers[
            peers["PeerInstitutionName"].astype(str).str.strip()
            == peer_name
        ]

        if base_rows.empty or peer_rows.empty:
            return {}

        base_id = str(base_rows.iloc[0]["InstitutionId"]).strip()
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

        return [
            f"[Source: {row['SourceName']}]"
            for _, row in selected.iterrows()
        ]