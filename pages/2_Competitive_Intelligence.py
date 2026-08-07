import streamlit as st

from app.templates.citation_panel import render_citation_panel
from app.templates.insight_panel import render_insight_panel
from app.templates.metric_cards import render_competitive_metrics
from app.templates.page_header import render_page_header
from retrieval.competitive_retriever import CompetitiveRetriever


st.set_page_config(
    page_title="Competitive Intelligence",
    page_icon="📊",
    layout="wide",
)


@st.cache_resource
def get_competitive_retriever() -> CompetitiveRetriever:
    return CompetitiveRetriever()


retriever = get_competitive_retriever()

render_page_header(
    title="ACME_Banking Competitive Intelligence",
    subtitle=(
        "Institutional peer benchmarking and relationship coverage support."
    ),
)

institutions = retriever.get_institution_options()

if not institutions:
    st.error("No competitive institutions were found.")
    st.stop()

st.sidebar.markdown("### Analysis Scope")

base_institution = st.sidebar.selectbox(
    "Base Institution",
    options=institutions,
    key="competitive_base_institution",
)

peer_options = retriever.get_peer_options(base_institution)

if not peer_options:
    st.warning(
        f"No peer benchmarks were found for {base_institution}."
    )
    st.stop()

selected_peer = st.sidebar.selectbox(
    "Peer Benchmark",
    options=peer_options,
    key="competitive_top_peer",
)

st.caption(
    f"Analysis scope: {base_institution} versus {selected_peer}"
)

metrics = retriever.get_metrics(
    base_institution_name=base_institution,
    peer_name=selected_peer,
)

render_competitive_metrics(
    market_share=metrics.get("Market Share", "Pending"),
    growth=metrics.get("Growth", "Pending"),
    momentum=metrics.get("Momentum", "Pending"),
)

st.markdown("---")

insight = retriever.get_insight(
    base_institution_name=base_institution,
    peer_name=selected_peer,
)

if insight:
    render_insight_panel(
        takeaway=insight.get(
            "takeaway",
            "No approved takeaway is available.",
        ),
        recommendation=insight.get(
            "recommendation",
            "No recommendation is available.",
        ),
        confidence=insight.get("confidence", "Unknown"),
    )

    source_id = insight.get("source_id")
    citations = retriever.get_sources([source_id]) if source_id else []
else:
    render_insight_panel(
        takeaway="No approved competitive insight is available.",
        recommendation=(
            "Maintain CRM-first coverage until evidence is available."
        ),
        confidence="Low",
    )
    citations = []

st.markdown("---")

render_citation_panel(citations)