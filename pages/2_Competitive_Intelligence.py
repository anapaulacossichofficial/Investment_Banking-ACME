import sys
from pathlib import Path

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from agents.competitive_intelligence_agent import (
    CompetitiveIntelligenceAgent,
)
from retrieval.competitive_intelligence_retriever import (
    CompetitiveIntelligenceRetriever,
)


st.set_page_config(
    page_title="Competitive Intelligence",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        min-width: 330px;
        max-width: 380px;
    }

    section[data-testid="stSidebar"] .stMultiSelect {
        width: 100%;
    }

    section[data-testid="stSidebar"] [data-baseweb="tag"] {
        margin: 0.15rem 0.15rem 0.15rem 0;
    }

    section[data-testid="stSidebar"] [data-baseweb="tag"] span {
        white-space: normal;
        overflow-wrap: anywhere;
    }
    </style>
    """
    ,
    unsafe_allow_html=True,
)


@st.cache_resource
def get_retriever() -> CompetitiveIntelligenceRetriever:
    return CompetitiveIntelligenceRetriever()


@st.cache_resource
def get_agent(base_institution: str) -> CompetitiveIntelligenceAgent:
    return CompetitiveIntelligenceAgent(
        base_institution=base_institution,
    )


retriever = get_retriever()

st.title("ACME_Banking Competitive Intelligence")
st.caption(
    "Institutional peer benchmarking and relationship coverage support."
)

institutions = retriever.get_institution_options()

if not institutions:
    st.error("No competitive institutions were found.")
    st.stop()

with st.sidebar:
    st.markdown("## Analysis Scope")
    st.caption("Select the base institution and peer benchmarks.")

    default_base = (
        "ACME_Banking"
        if "ACME_Banking" in institutions
        else institutions[0]
    )

    base_institution = st.selectbox(
        "Base Institution",
        options=institutions,
        index=institutions.index(default_base),
        key="competitive_base_institution",
        help="Institution used as the primary comparison reference.",
    )

    peer_options = retriever.get_peer_options(base_institution)

    if not peer_options:
        st.warning(
            f"No peer benchmarks were found for {base_institution}."
        )
        st.stop()

    selected_peers = st.multiselect(
        "Peer Institutions",
        options=peer_options,
        default=[],
        key="competitive_peer_institutions",
        placeholder="Choose one or more peers",
        help="Select the institutions to include in the comparison.",
    )

    run_analysis = st.button(
        "Generate Competitive Briefing",
        type="primary",
        use_container_width=True,
    )

st.caption(
    f"Analysis scope: {base_institution} "
    f"versus {', '.join(selected_peers) or 'no selected peers'}"
)

if not selected_peers:
    st.info("Select at least one peer institution in the sidebar.")
    st.stop()

if not run_analysis:
    st.info("Click **Generate Competitive Briefing** to run the analysis.")
    st.stop()

agent = get_agent(base_institution)
briefing = agent.generate_competitive_briefing(
    peer_institutions=selected_peers,
)

st.subheader("Executive Competitive Briefing")
st.code(briefing, language="text")

st.markdown("---")
st.subheader("Peer Metrics")

for peer in selected_peers:
    metrics = retriever.get_metrics(
        base_institution_name=base_institution,
        peer_name=peer,
    )

    st.markdown(f"**{peer}**")
    if not metrics:
        st.info("No metrics available.")
        continue

    metric_columns = st.columns(len(metrics))
    for column, (metric_name, metric_value) in zip(
        metric_columns,
        metrics.items(),
    ):
        column.metric(metric_name, metric_value)

st.markdown("---")
st.subheader("Approved Insight References")

for peer in selected_peers:
    insight = retriever.get_insight(
        base_institution_name=base_institution,
        peer_name=peer,
    )

    if not insight:
        st.info(f"No approved insight available for {peer}.")
        continue

    st.markdown(f"**{peer}**")
    st.write(f"**Takeaway:** {insight.get('takeaway', 'Not available')}")
    st.write(
        "**Recommendation:** "
        f"{insight.get('recommendation', 'Not available')}"
    )
    st.caption(f"Confidence: {insight.get('confidence', 'Unknown')}")

    source_id = insight.get("source_id")

    if source_id:
        sources = retriever.get_sources([str(source_id)])
        if sources:
            st.markdown("**Sources:**")
            for source in sources:
                st.code(source, language="text")
