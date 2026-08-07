import streamlit as st


def render_competitive_metrics(
    market_share: str,
    growth: str,
    momentum: str,
) -> None:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Market Share", market_share)

    with col2:
        st.metric("Growth", growth)

    with col3:
        st.metric("Momentum", momentum)