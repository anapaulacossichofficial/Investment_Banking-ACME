import pandas as pd
import pytest

from retrieval.competitive_intelligence_retriever import (
    CompetitiveIntelligenceRetriever,
)


BASE_INSTITUTION = "ACME_Banking"


@pytest.fixture
def retriever():
    return CompetitiveIntelligenceRetriever()


def test_retriever_initialization(retriever):
    assert retriever.data_dir.exists()
    assert retriever.data_dir.name == "competitive"


@pytest.mark.parametrize(
    ("loader_name", "required_columns"),
    [
        (
            "load_institutions",
            {"InstitutionId", "InstitutionName"},
        ),
        (
            "load_peers",
            {
                "PeerId",
                "BaseInstitutionId",
                "PeerInstitutionId",
                "PeerInstitutionName",
            },
        ),
        (
            "load_metrics",
            {
                "MetricId",
                "BaseInstitutionId",
                "PeerInstitutionId",
                "MetricName",
                "MetricValue",
                "SourceId",
            },
        ),
        (
            "load_insights",
            {
                "InsightId",
                "BaseInstitutionId",
                "PeerInstitutionId",
                "Takeaway",
                "Recommendation",
                "Confidence",
                "SourceId",
            },
        ),
        (
            "load_sources",
            {
                "SourceId",
                "SourceName",
                "Approved",
            },
        ),
    ],
)
def test_real_competitive_loaders(
    retriever,
    loader_name,
    required_columns,
):
    loader = getattr(retriever, loader_name)
    dataframe = loader()

    assert isinstance(dataframe, pd.DataFrame)
    assert not dataframe.empty
    assert required_columns.issubset(dataframe.columns)


def test_get_institution_options_contains_base_institution(retriever):
    options = retriever.get_institution_options()

    assert isinstance(options, list)
    assert options
    assert BASE_INSTITUTION in options


def test_get_peer_options_returns_configured_peers(retriever):
    peers = retriever.get_peer_options(BASE_INSTITUTION)

    assert isinstance(peers, list)
    assert peers


def test_get_metrics_returns_dictionary_for_valid_peer(retriever):
    peers = retriever.get_peer_options(BASE_INSTITUTION)

    assert peers

    metrics = retriever.get_metrics(
        base_institution_name=BASE_INSTITUTION,
        peer_name=peers[0],
    )

    assert isinstance(metrics, dict)


def test_get_insight_contains_expected_fields_for_valid_peer(retriever):
    peers = retriever.get_peer_options(BASE_INSTITUTION)

    assert peers

    insight = retriever.get_insight(
        base_institution_name=BASE_INSTITUTION,
        peer_name=peers[0],
    )

    assert isinstance(insight, dict)

    if insight:
        assert {
            "takeaway",
            "recommendation",
            "confidence",
            "source_id",
        }.issubset(insight.keys())


def test_get_sources_returns_approved_source_labels(retriever):
    peers = retriever.get_peer_options(BASE_INSTITUTION)

    assert peers

    insight = retriever.get_insight(
        base_institution_name=BASE_INSTITUTION,
        peer_name=peers[0],
    )

    assert isinstance(insight, dict)

    if insight and insight.get("source_id"):
        sources = retriever.get_sources(
            [str(insight["source_id"])]
        )

        assert isinstance(sources, list)
        assert all(isinstance(source, str) for source in sources)


def test_current_retriever_does_not_require_get_context(retriever):
    assert not hasattr(retriever, "get_context")