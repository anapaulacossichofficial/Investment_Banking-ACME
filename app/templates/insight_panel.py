import streamlit as st


def render_insight_panel(
    takeaway: str,
    recommendation: str,
    confidence: str,
) -> None:
    st.subheader("Competitive Intelligence Insight")

    st.markdown(f"**Key takeaway**  \n{takeaway}")
    st.markdown(f"**Recommended action**  \n{recommendation}")

    st.caption(f"Confidence: {confidence}")