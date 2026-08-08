"""
Competitive Intelligence Agent (Local Laboratory Blueprint)

Responsible for synthesizing market positioning, peer benchmarks,
and strategic alerts from approved local fixtures.
"""

from typing import List

import pandas as pd

from retrieval.competitive_intelligence_retriever import (
    CompetitiveIntelligenceRetriever,
)


class CompetitiveIntelligenceAgent:
    """
    Generates grounded competitive-intelligence briefings.

    The agent delegates data access to CompetitiveIntelligenceRetriever
    and only formats the resulting context into an executive summary.
    """

    def __init__(self, base_institution: str = "ACME_BANKING"):
        self.base_institution = base_institution
        self.retriever = CompetitiveIntelligenceRetriever()

    def generate_competitive_briefing(
        self,
        peer_institutions: List[str],
    ) -> str:
        """
        Generate an executive summary for the selected peer cohort.
        """

        peer_institutions = peer_institutions or []

        context = self.retriever.get_context(
            base_institution=self.base_institution,
            peer_institutions=peer_institutions,
        )

        transactions = context.get("transactions", pd.DataFrame())
        signals = context.get("signals", pd.DataFrame())
        institutions = context.get("institutions", pd.DataFrame())

        briefing: list[str] = [
            "=== COMPETITIVE INTELLIGENCE BRIEFING ===",
            f"Base Institution: {self.base_institution}",
            f"Target Peers: {', '.join(peer_institutions) or 'None selected'}",
            "",
        ]

        briefing.extend(self._build_transaction_section(
            transactions=transactions,
            institutions=institutions,
        ))

        briefing.extend(self._build_signal_section(
            signals=signals,
            institutions=institutions,
        ))

        briefing.extend(
            [
                "",
                "3. Compliance & Validation:",
                "- Analysis based solely on approved local competitive fixtures.",
                "- Tracked volume must not be interpreted as official market share.",
                "- Findings require validation against current coverage and CRM context.",
            ]
        )

        return "\n".join(briefing)

    def _build_transaction_section(
        self,
        transactions: pd.DataFrame,
        institutions: pd.DataFrame,
    ) -> list[str]:
        lines = [
            "1. Transaction Volume Snapshot:",
        ]

        required_transactions = {"InstitutionId", "Amount"}
        required_institutions = {"InstitutionId", "InstitutionName"}

        if transactions.empty:
            lines.append("- No transaction data available for the selected cohort.")
            return lines

        if not required_transactions.issubset(transactions.columns):
            lines.append("- Transaction data is missing required columns.")
            return lines

        if not required_institutions.issubset(institutions.columns):
            lines.append("- Institution mapping is unavailable.")
            return lines

        ranking = (
            transactions.groupby("InstitutionId", dropna=False)
            .agg(TrackedValue=("Amount", "sum"))
            .reset_index()
            .merge(
                institutions[["InstitutionId", "InstitutionName"]],
                on="InstitutionId",
                how="left",
            )
            .sort_values("TrackedValue", ascending=False)
        )

        if ranking.empty:
            lines.append("- No transaction data available for the selected cohort.")
            return lines

        for _, row in ranking.iterrows():
            institution_name = row["InstitutionName"]
            tracked_value = float(row["TrackedValue"])

            lines.append(
                f"- {institution_name}: "
                f"${tracked_value / 1_000_000:.1f}M tracked value."
            )

        top_institution = ranking.iloc[0]["InstitutionName"]

        if top_institution != self.base_institution:
            lines.append(
                f"ALERT: {top_institution} is currently leading "
                "in tracked deal volume."
            )

        return lines

    def _build_signal_section(
        self,
        signals: pd.DataFrame,
        institutions: pd.DataFrame,
    ) -> list[str]:
        lines = [
            "",
            "2. Recent Market Signals:",
        ]

        required_signals = {
            "SignalDate",
            "InstitutionId",
            "SignalType",
            "Description",
            "Confidence",
        }
        required_institutions = {"InstitutionId", "InstitutionName"}

        if signals.empty:
            lines.append("- No recent market signals tracked for this cohort.")
            return lines

        if not required_signals.issubset(signals.columns):
            lines.append("- Market signals are missing required columns.")
            return lines

        recent_signals = signals.sort_values(
            "SignalDate",
            ascending=False,
        ).head(3)

        for _, row in recent_signals.iterrows():
            institution_name = str(row["InstitutionId"])

            if required_institutions.issubset(institutions.columns):
                institution_rows = institutions.loc[
                    institutions["InstitutionId"].astype(str)
                    == str(row["InstitutionId"]),
                    "InstitutionName",
                ]

                if not institution_rows.empty:
                    institution_name = str(institution_rows.iloc[0])

            lines.append(
                f"- [{row['SignalDate']}] "
                f"{institution_name} ({row['SignalType']}): "
                f"{row['Description']} "
                f"[Confidence: {row['Confidence']}]"
            )

        return lines
