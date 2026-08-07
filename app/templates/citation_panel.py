import streamlit as st


def render_citation_panel(citations: list[str]) -> None:
    st.subheader("Sources & Citations")

    if not citations:
        st.info("No approved source citations are available yet.")
        return

    for citation in citations:
        st.code(citation, language="text")