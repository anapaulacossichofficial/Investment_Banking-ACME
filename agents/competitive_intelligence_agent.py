"""
Competitive Intelligence Agent (Local Laboratory Blueprint)

Responsible for synthesizing peer benchmarks, strategic insights,
and approved source references from local competitive fixtures.
"""

from typing import List

from retrieval.competitive_intelligence_retriever import (
    CompetitiveIntelligenceRetriever,
)


class CompetitiveIntelligenceAgent:
    """
    Generates grounded competitive-intelligence briefings.

    The agent consumes only the explicit API exposed by the current
    CompetitiveIntelligenceRetriever:
    - get_metrics()
    - get_insight()
    - get_sources()
    """

    def __init__(self, base_institution: str = "ACME_Banking"):
        self.base_institution = base_institution
        self.retriever = CompetitiveIntelligenceRetriever()

    def generate_competitive_briefing(
        self,
        peer_institutions: List[str],
    ) -> str:
        """
        Generate an executive briefing for selected peer institutions.
        """

        peer_institutions = peer_institutions or []

        briefing: list[str] = [
            "=== COMPETITIVE INTELLIGENCE BRIEFING ===",
            f"Base Institution: {self.base_institution}",
            (
                "Target Peers: "
                f"{', '.join(peer_institutions) or 'None selected'}"
            ),
            "",
        ]

        if not peer_institutions:
            briefing.extend(
                [
                    "1. Peer Benchmarking & Metrics:",
                    "- No peers selected for comparison.",
                    "",
                    "2. Strategic Insights & Recommendations:",
                    "- No peer insights available without a selected comparison.",
                    "",
                    "3. Compliance & Validation:",
                    "- Analysis based solely on approved local competitive fixtures.",
                    "- Findings require validation against current CRM coverage context.",
                ]
            )
            return "\n".join(briefing)

        briefing.append("1. Peer Benchmarking & Metrics:")

        for peer in peer_institutions:
            metrics = self.retriever.get_metrics(
                base_institution_name=self.base_institution,
                peer_name=peer,
            )

            if metrics:
                metrics_text = " | ".join(
                    f"{name}: {value}"
                    for name, value in metrics.items()
                )
                briefing.append(f"- {peer}: {metrics_text}")
            else:
                briefing.append(f"- {peer}: No metrics available.")

        briefing.append("")
        briefing.append("2. Strategic Insights & Recommendations:")

        source_ids: list[str] = []

        for peer in peer_institutions:
            insight = self.retriever.get_insight(
                base_institution_name=self.base_institution,
                peer_name=peer,
            )

            if not insight:
                briefing.append(
                    f"- vs {peer}: No approved insights available."
                )
                continue

            briefing.extend(
                [
                    f"- vs {peer}:",
                    (
                        "  * Takeaway: "
                        f"{insight.get('takeaway', 'Not available')}"
                    ),
                    (
                        "  * Recommendation: "
                        f"{insight.get('recommendation', 'Not available')}"
                    ),
                    (
                        "  * Confidence: "
                        f"{insight.get('confidence', 'Unknown')}"
                    ),
                ]
            )

            source_id = insight.get("source_id")
            if source_id:
                source_ids.append(str(source_id))

        briefing.extend(
            [
                "",
                "3. Approved Sources:",
            ]
        )

        if source_ids:
            sources = self.retriever.get_sources(source_ids)

            if sources:
                briefing.extend(
                    f"- {source}"
                    for source in sources
                )
            else:
                briefing.append("- No approved source labels available.")
        else:
            briefing.append("- No source identifiers available.")

        briefing.extend(
            [
                "",
                "4. Compliance & Validation:",
                "- Analysis based solely on approved local competitive fixtures.",
                "- Findings require validation against current CRM coverage context.",
                "- Tracked metrics must not be interpreted as official market share.",
            ]
        )

        return "\n".join(briefing)
