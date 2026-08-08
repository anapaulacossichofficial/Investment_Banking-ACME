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
from ui.styles import apply_bankiq_style


st.set_page_config(
    page_title="ACME_Banking Competitive Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_bankiq_style()


@st.cache_resource
def get_retriever() -> CompetitiveIntelligenceRetriever:
    return CompetitiveIntelligenceRetriever()


@st.cache_resource
def get_agent(
    base_institution: str,
) -> CompetitiveIntelligenceAgent:
    return CompetitiveIntelligenceAgent(
        base_institution=base_institution,
    )


retriever = get_retriever()


st.markdown(
    """
    <div class="enterprise-header">
        <h1>📊 ACME_Banking Competitive Intelligence Hub</h1>
        <p>
            Institutional peer benchmarking, market metrics,
            and strategic positioning insights
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


institutions = retriever.get_institution_options()

if not institutions:
    st.error("No competitive institutions were found.")
    st.stop()


with st.sidebar:
    st.markdown("### ⚙️ Benchmark Configuration")
    st.caption(
        "Select the institutional base and peer comparison set."
    )
    st.markdown("---")

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
        help="Institution used as the primary benchmark reference.",
    )

    peer_options = retriever.get_peer_options(
        base_institution
    )

    if not peer_options:
        st.warning(
            f"No peer benchmarks found for {base_institution}."
        )
        st.stop()

    selected_peers = st.multiselect(
        "Peer Institutions",
        options=peer_options,
        default=[],
        key="competitive_peer_institutions",
        placeholder="Choose one or more peers",
        help="Select one or more institutions for comparison.",
    )

    generate_briefing = st.button(
        "Generate Competitive Briefing",
        type="primary",
        use_container_width=True,
    )


st.markdown(
    f"""
    <div class="scope-card">
        <strong>Active Analysis Scope:</strong>
        {base_institution}
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <strong>Peer Set:</strong>
        {
            ", ".join(selected_peers)
            if selected_peers
            else "None selected"
        }
    </div>
    """,
    unsafe_allow_html=True,
)


if not selected_peers:
    st.info(
        "Select at least one peer institution in the sidebar."
    )
    st.stop()


if not generate_briefing:
    st.info(
        "Click **Generate Competitive Briefing** "
        "to render the executive analysis."
    )
    st.stop()


agent = get_agent(base_institution)


tab_briefing, tab_metrics, tab_insights = st.tabs(
    [
        "📑 Executive Briefing",
        "📈 Peer Benchmarking",
        "💡 Strategic Insights & Sources",
    ]
)


with tab_briefing:
    st.subheader("Autonomous Briefing Synthesis")

    briefing = agent.generate_competitive_briefing(
        peer_institutions=selected_peers,
    )

    st.code(briefing, language="text")

    st.markdown(
        """
        <div class="guardrail-card">
            <strong>Validation note:</strong>
            The briefing is grounded in approved local competitive fixtures
            and should be validated against current CRM coverage context.
        </div>
        """,
        unsafe_allow_html=True,
    )


with tab_metrics:
    st.subheader("Key Financial & Market Metrics")

    for peer in selected_peers:
        st.markdown(
            f"""
            <div class="peer-card">
                <div class="peer-card-title">🏛️ {peer}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        metrics = retriever.get_metrics(
            base_institution_name=base_institution,
            peer_name=peer,
        )

        if not metrics:
            st.info("No metrics available.")
            continue

        columns = st.columns(len(metrics))

        for column, (metric_name, metric_value) in zip(
            columns,
            metrics.items(),
        ):
            column.metric(
                metric_name,
                metric_value,
            )


with tab_insights:
    st.subheader(
        "Approved Research & Compliance Insights"
    )

    for peer in selected_peers:
        insight = retriever.get_insight(
            base_institution_name=base_institution,
            peer_name=peer,
        )

        if not insight:
            st.info(
                f"No approved insights available for {peer}."
            )
            continue

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="peer-card-title">vs {peer}</div>
                <div>
                    <strong>Takeaway:</strong>
                    {insight.get("takeaway", "Not available")}
                </div>
                <div>
                    <strong>Recommendation:</strong>
                    {insight.get("recommendation", "Not available")}
                </div>
                <div>
                    <strong>Confidence:</strong>
                    {insight.get("confidence", "Unknown")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        source_id = insight.get("source_id")

        if not source_id:
            st.caption("No source identifier available.")
            continue

        sources = retriever.get_sources(
            [str(source_id)]
        )

        if not sources:
            st.caption(
                "No approved source labels available."
            )
            continue

        st.markdown("**Verified Sources**")

        for source in sources:
            st.markdown(
                f"""
                <div class="source-card">
                    ✓ {source}
                </div>
                """,
                unsafe_allow_html=True,
            )