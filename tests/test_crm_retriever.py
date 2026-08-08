import pandas as pd

from retrieval.crm_retriever import CRMRetriever


def test_get_account_bundle_returns_expected_keys():
    retriever = CRMRetriever()
    bundle = retriever.get_account_bundle("ACC-001")

    assert isinstance(bundle, dict)
    assert set(bundle.keys()) == {"account", "contacts", "opportunities", "activities"}
    assert all(isinstance(v, pd.DataFrame) for v in bundle.values())


def test_get_account_bundle_filters_by_account_id():
    retriever = CRMRetriever()
    bundle = retriever.get_account_bundle("ACC-001")

    for key in ["contacts", "opportunities", "activities"]:
        df = bundle[key]
        if not df.empty:
            assert "AccountId" in df.columns
            assert all(df["AccountId"].astype(str).str.strip() == "ACC-001")