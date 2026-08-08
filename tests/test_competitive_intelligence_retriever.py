from retrieval.competitive_intelligence_retriever import CompetitiveIntelligenceRetriever


def _pick_base_and_peer(retriever):
    institutions = retriever.load_institutions()
    peers = retriever.load_peers()
    assert not institutions.empty
    assert not peers.empty
    base_name = institutions.iloc[0]["InstitutionName"]
    peer_name = peers.iloc[0]["PeerInstitutionName"]
    return base_name, peer_name


def test_loaders_return_dataframes():
    retriever = CompetitiveIntelligenceRetriever()
    assert not retriever.load_institutions().empty
    assert not retriever.load_peers().empty
    assert not retriever.load_metrics().empty
    assert not retriever.load_insights().empty
    assert not retriever.load_sources().empty


def test_options_and_metrics_and_insight_and_sources():
    retriever = CompetitiveIntelligenceRetriever()
    institutions = retriever.get_institution_options()
    assert institutions

    base_name, peer_name = _pick_base_and_peer(retriever)
    peers = retriever.get_peer_options(base_name)
    assert isinstance(peers, list)

    metrics = retriever.get_metrics(base_name, peer_name)
    assert isinstance(metrics, dict)

    insight = retriever.get_insight(base_name, peer_name)
    assert isinstance(insight, dict)
    if insight:
        assert {"takeaway", "recommendation", "confidence", "source_id"}.issubset(insight.keys())
        citations = retriever.get_sources([insight["source_id"]])
        assert isinstance(citations, list)