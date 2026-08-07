import streamlit as st


def render_page_header(
    title: str,
    subtitle: str,
    page_icon: str = "📊",
) -> None:
    st.title(f"{page_icon} {title}")
    st.markdown(subtitle)
    st.markdown("---")