import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from retrieval.competitive_intelligence_retriever import CompetitiveIntelligenceRetriever

st.set_page_config(
    page_title="Competitive Intelligence",
    page_icon="📊",
    layout="wide",
)


@st.cache_resource
def get_retriever() -> CompetitiveIntelligenceRetriever:
    return CompetitiveIntelligenceRetriever()


retriever = get_retriever()

st.title("ACME_Banking Competitive Intelligence")
st.caption("Institutional peer benchmarking and relationship coverage support.")

institutions = retriever.get_institution_options()
if not institutions:
    st.error("No competitive institutions were found.")
    st.stop()

st.sidebar.markdown("### Analysis Scope")
base_institution = st.sidebar.selectbox(
    "Base Institution", options=institutions, key="competitive_base_institution"
)

peer_options = retriever.get_peer_options(base_institution)
if not peer_options:
    st.warning(f"No peer benchmarks were found for {base_institution}.")
    st.stop()

selected_peer = st.sidebar.selectbox(
    "Peer Benchmark", options=peer_options, key="competitive_top_peer"
)

st.caption(f"Analysis scope: {base_institution} versus {selected_peer}")

metrics = retriever.get_metrics(base_institution, selected_peer)

col1, col2, col3 = st.columns(3)
col1.metric("Market Share", metrics.get("Market Share", "Pending"))
col2.metric("Growth", metrics.get("Growth", "Pending"))
col3.metric("Momentum", metrics.get("Momentum", "Pending"))

st.markdown("---")

insight = retriever.get_insight(base_institution, selected_peer)
if insight:
    st.subheader("Insight")
    st.write(f"**Takeaway:** {insight.get('takeaway', 'No approved takeaway is available.')}")
    st.write(f"**Recommendation:** {insight.get('recommendation', 'No recommendation is available.')}")
    st.write(f"**Confidence:** {insight.get('confidence', 'Unknown')}")
    source_id = insight.get("source_id")
    citations = retriever.get_sources([source_id]) if source_id else []
else:
    st.subheader("Insight")
    st.write("No approved competitive insight is available.")
    st.write("Maintain CRM-first coverage until evidence is available.")
    citations = []

st.markdown("---")
st.subheader("Citations")
if citations:
    for c in citations:
        st.code(c, language="text")
else:
    st.caption("No approved citations available.")