from pathlib import Path
import pandas as pd

class CRMRetriever:
    def __init__(self, base_path="data/crm"):
        self.base_path = Path(base_path)

    def _load_csv(self, name: str) -> pd.DataFrame:
        path = self.base_path / name
        return pd.read_csv(path) if path.exists() else pd.DataFrame()

    def get_account_bundle(self, account_id: str) -> dict:
        accounts = self._load_csv("accounts.csv")
        contacts = self._load_csv("contacts.csv")
        opportunities = self._load_csv("opportunities.csv")
        activities = self._load_csv("activities.csv")

        return {
            "account": accounts[accounts["AccountId"] == account_id] if not accounts.empty else pd.DataFrame(),
            "contacts": contacts[contacts["AccountId"] == account_id] if not contacts.empty else pd.DataFrame(),
            "opportunities": opportunities[opportunities["AccountId"] == account_id] if not opportunities.empty else pd.DataFrame(),
            "activities": activities[activities["AccountId"] == account_id] if not activities.empty else pd.DataFrame(),
        }