from pathlib import Path
import pandas as pd


class MeetingPrepAgent:
    def __init__(self, client_id: str = "ACC-001", client_name: str = "ACME INVESTMENTS"):
        self.client_id = client_id
        self.client_name = client_name
        self.prompt_path = "prompts/meeting_prep_prompt.txt"
        self.fallback_path = "prompts/fallback_prompt.txt"

    def _load_text(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8") if Path(path).exists() else ""

    def _load_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path) if Path(path).exists() else pd.DataFrame()

    def generate_briefing(self) -> str:
        accounts_df = self._load_csv("data/crm/accounts.csv")
        contacts_df = self._load_csv("data/crm/contacts.csv")
        opps_df = self._load_csv("data/crm/opportunities.csv")
        activities_df = self._load_csv("data/crm/activities.csv")

        account = accounts_df[accounts_df["AccountId"] == self.client_id] if not accounts_df.empty else pd.DataFrame()
        contacts = contacts_df[contacts_df["AccountId"] == self.client_id] if not contacts_df.empty else pd.DataFrame()
        opps = opps_df[opps_df["AccountId"] == self.client_id] if not opps_df.empty else pd.DataFrame()
        activities = activities_df[activities_df["AccountId"] == self.client_id] if not activities_df.empty else pd.DataFrame()

        summary = [f"=== EXECUTIVE BRIEFING: {self.client_name} ===", ""]

        summary.append("1. Executive Summary:")
        summary.append(f"- {self.client_name} is the institutional coverage target for the upcoming meeting.")
        summary.append("- Briefing synthesized only from CRM fixtures and approved prompt guardrails.")
        summary.append("")

        summary.append("2. Active Deal Pipeline & Financial Position (CRM):")
        if not opps.empty:
            for _, row in opps.iterrows():
                summary.append(
                    f"- Opportunity: {row['Name']} | Stage: {row['StageName']} | "
                    f"Value: R$ {int(row['Amount']):,}.00 | Close: {row['CloseDate']} "
                    f"[Source: CRM {row['OpportunityId']}]"
                )
        else:
            summary.append("- Data not available in current institutional records.")
        summary.append("")

        summary.append("3. Strategic Market Insights & Research Context:")
        if not activities.empty:
            for _, row in activities.iterrows():
                summary.append(
                    f"- Activity: {row['Subject']} on {row['ActivityDate']} "
                    f"[Source: CRM {row['ActivityId']}]"
                )
        else:
            summary.append("- Data not available in current institutional records.")
        summary.append("")

        summary.append("4. Recommended Strategic Talking Points for the Banker:")
        if not opps.empty:
            deal_types = sorted([x for x in opps["DealType"].dropna().unique().tolist() if str(x).strip()])
            stages = sorted([x for x in opps["StageName"].dropna().unique().tolist() if str(x).strip()])

            if deal_types:
                summary.append(
                    f"- Focus on {' and '.join(deal_types).lower()} opportunities relevant to {self.client_name}."
                )
            else:
                summary.append(f"- Focus on the active pipeline opportunities relevant to {self.client_name}.")

            if stages:
                summary.append(
                    f"- Reinforce next-step alignment across {' and '.join(stages).lower()} milestones."
                )
            else:
                summary.append("- Reinforce next-step alignment across active pipeline milestones.")

            if not contacts.empty:
                summary.append("- Validate all claims against CRM records before client delivery.")
        else:
            summary.append(f"- No active deal pipeline identified for {self.client_name}.")
            summary.append("- Focus on relationship discovery and coverage planning.")
            summary.append("- Validate all claims against CRM records before client delivery.")

        return "\n".join(summary)