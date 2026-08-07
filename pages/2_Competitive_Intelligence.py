import streamlit as st

from app.templates.citation_panel import render_citation_panel
from app.templates.filter_panel import render_competitive_filters
from app.templates.insight_panel import render_insight_panel
from app.templates.metric_cards import render_competitive_metrics
from app.templates.page_header import render_page_header


st.set_page_config(
    page_title="Competitive Intelligence",
    page_icon="📊",
    layout="wide",
)

render_page_header(
    title="ACME_Banking Competitive Intelligence",
    subtitle=(
        "Institutional peer benchmarking and relationship coverage support."
    ),
)

base_institution, top_peer = render_competitive_filters(
    institutions=[
        "ACME_Banking",
        "QUANTUM INVESTMENTS",
        "GLOBALTRUST CAPITAL",
    ],
    peers=[
        "Peer benchmark pending",
        "Institutional peer 1",
        "Institutional peer 2",
    ],
)

st.caption(
    f"Analysis scope: {base_institution} versus {top_peer}"
)

render_competitive_metrics(
    market_share="Pending",
    growth="Pending",
    momentum="Pending",
)

st.markdown("---")

render_insight_panel(
    takeaway=(
        "Competitive evidence will be displayed after the approved "
        "competitive CSV templates are populated."
    ),
    recommendation=(
        "Use the CRM relationship context as the primary source until "
        "competitive evidence is available."
    ),
    confidence="Low — template only",
)

st.markdown("---")

render_citation_panel(
    citations=[
        "[Source: Competitive CSV — pending]",
        "[Source: CRM records — available in main workspace]",
    ]
)