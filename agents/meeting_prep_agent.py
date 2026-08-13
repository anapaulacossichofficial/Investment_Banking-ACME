from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from retrieval.crm_retriever import CRMRetriever
from retrieval.knowledge_retriever import KnowledgeRetriever


@dataclass
class BriefingContext:
    account_name: str
    account_id: str


class MeetingPrepAgent:
    def __init__(self, client_id: str, client_name: str):
        self.client_id = client_id
        self.client_name = client_name
        self.crm_retriever = CRMRetriever()
        self.knowledge_retriever = KnowledgeRetriever()

    def _build_recommended_next_actions(
        self, opportunities: pd.DataFrame, activities: pd.DataFrame
    ) -> list[str]:
        actions = []

        if opportunities.empty:
            actions.append(
                "Reconfirm the client’s current priorities and identify whether a new opportunity has emerged."
            )
            actions.append(
                "Schedule a relationship check-in to refresh coverage context."
            )
            return actions

        if "StageName" in opportunities.columns:
            stages = set(
                opportunities["StageName"].dropna().astype(str).tolist()
            )
            if "Prospecting" in stages:
                actions.append(
                    "Clarify the client’s strategic priorities and identify the buying center."
                )
            if "Due Diligence" in stages:
                actions.append(
                    "Confirm open diligence items, decision criteria, and key stakeholders."
                )
            if "Negotiation" in stages:
                actions.append(
                    "Validate negotiation milestones, timeline, and executive sponsorship."
                )

        if "DealType" in opportunities.columns:
            deal_types = sorted(
                set(opportunities["DealType"].dropna().astype(str).tolist())
            )
            if deal_types:
                actions.append(
                    f"Position ACME_Banking around {' / '.join(deal_types)} capabilities relevant to the client’s pipeline."
                )

        if not activities.empty:
            actions.append(
                "Follow up on the latest recorded activity and confirm the next expected interaction."
            )

        actions.append("Validate all claims against CRM records before client delivery.")
        return actions[:4]

    def generate_briefing(self, competitive_context: Optional[dict] = None) -> str:
        bundle = self.crm_retriever.get_account_bundle(self.client_id)
        docs = self.knowledge_retriever.list_documents()

        contacts = bundle.get("contacts", pd.DataFrame())
        opportunities = bundle.get("opportunities", pd.DataFrame())
        activities = bundle.get("activities", pd.DataFrame())

        overview_lines = [
            "1. Executive Summary:",
            f"- {self.client_name} is the institutional coverage target for the upcoming meeting.",
            "- The briefing is grounded in account-specific CRM records and approved knowledge sources.",
            "",
            "2. CRM Snapshot:",
            f"- Active opportunities: {len(opportunities)}",
            f"- Related contacts: {len(contacts)}",
            f"- Recent activities: {len(activities)}",
            "",
            "3. Strategic Talking Points:",
        ]

        if not opportunities.empty:
            deal_types = sorted(
                set(opportunities["DealType"].dropna().astype(str).tolist())
            )
            stages = sorted(
                set(opportunities["StageName"].dropna().astype(str).tolist())
            )

            if deal_types:
                overview_lines.append(
                    f"- Focus on the active {' / '.join(deal_types)} pipeline."
                )
            else:
                overview_lines.append(
                    "- Focus on the active opportunity pipeline."
                )

            if stages:
                overview_lines.append(
                    f"- Reinforce next-step alignment across {' / '.join(stages)} milestones."
                )
            else:
                overview_lines.append(
                    "- Reinforce next-step alignment across active milestones."
                )
        else:
            overview_lines.append(
                f"- No active pipeline was identified for {self.client_name}."
            )
            overview_lines.append(
                "- Prioritize relationship discovery and coverage planning."
            )

        overview_lines.extend(
            [
                "",
                "4. Evidence Context:",
                f"- Structured evidence bundle includes CRM account, contact, opportunity, and activity records for {self.client_name}.",
            ]
        )

        if docs:
            overview_lines.append(
                f"- Approved knowledge sources available: {', '.join(sorted(docs))}."
            )
        else:
            overview_lines.append(
                "- No approved knowledge documents were available at runtime; use CRM-only fallback."
            )

        overview_lines.extend(
            [
                "",
                "5. Recommended Next Actions:",
            ]
        )

        next_actions = self._build_recommended_next_actions(
            opportunities=opportunities,
            activities=activities,
        )

        for action in next_actions:
            overview_lines.append(f"- {action}")

        if competitive_context:
            overview_lines.extend(
                [
                    "",
                    "6. Competitive Intelligence Context:",
                ]
            )

            base_institution = competitive_context.get("base_institution")
            top_peer = competitive_context.get("top_peer")
            takeaway = competitive_context.get("takeaway")
            recommendation = competitive_context.get("recommendation")
            confidence = competitive_context.get("confidence", "Medium")

            if base_institution:
                overview_lines.append(f"- Base institution: {base_institution}")
            if top_peer:
                overview_lines.append(f"- Peer benchmark: {top_peer}")
            if takeaway:
                overview_lines.append(f"- Insight: {takeaway}")
            if recommendation:
                overview_lines.append(f"- Recommended action: {recommendation}")

            overview_lines.append(f"- Confidence: {confidence}")

        overview_lines.extend(
            [
                "",
                "7. Validation Guardrail:",
                "- Validate all claims against CRM records and approved source materials before client delivery.",
            ]
        )

        return "\n".join(overview_lines)
