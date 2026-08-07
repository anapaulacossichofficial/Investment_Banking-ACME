import streamlit as st


def render_competitive_filters(
    institutions: list[str],
    peers: list[str],
) -> tuple[str, str]:
    st.sidebar.markdown("### Analysis Scope")

    base_institution = st.sidebar.selectbox(
        "Base Institution",
        options=institutions,
        key="competitive_base_institution",
    )

    top_peer = st.sidebar.selectbox(
        "Peer Benchmark",
        options=peers,
        key="competitive_top_peer",
    )

    return base_institution, top_peer