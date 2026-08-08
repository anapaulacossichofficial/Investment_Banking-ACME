"""
Streamlit Local Laboratory UI (ib-agent-demo)

Visualizes the Agentforce Meeting Prep Agent workflow
for institutional accounts.
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

from agents.meeting_prep_agent import MeetingPrepAgent
from agents.supervisor_agent import SupervisorAgent
from retrieval.crm_retriever import CRMRetriever
from retrieval.knowledge_retriever import KnowledgeRetriever
from ui.styles import apply_bankiq_style


ROOT_DIR = Path(__file__).resolve().parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


DATA_DIR = ROOT_DIR / "data"
CRM_DIR = DATA_DIR / "crm"
KNOWLEDGE_DIR = DATA_DIR / "knowledge"


st.set_page_config(
    page_title="Agentforce PTA - Investment Banking Demo",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_bankiq_style()

# --- HERO HEADER ---
st.markdown(
    """
    <div class="enterprise-header">
        <h1>💼 ACME_Banking Intelligence Hub</h1>
        <p>
            Local Architecture — Agentforce Meeting Prep,
            CRM Grounding & Competitive Intelligence
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


ACCOUNT_OPTIONS = {
    "QUANTUM INVESTMENTS (ACC-001)": (
        "ACC-001",
        "QUANTUM INVESTMENTS",
    ),
    "GLOBALTRUST CAPITAL (ACC-002)": (
        "ACC-002",
        "GLOBALTRUST CAPITAL",
    ),
}


def get_selected_account():
    selected_label = st.session_state["selected_account_label"]
    return ACCOUNT_OPTIONS[selected_label]


def get_agents(client_id: str, client_name: str):
    """
    Initializes shared agents once per session.
    Recreates MeetingPrepAgent when the selected account changes.
    """
    if "supervisor" not in st.session_state:
        st.session_state.supervisor = SupervisorAgent()

    if "crm_retriever" not in st.session_state:
        st.session_state.crm_retriever = CRMRetriever()

    if "knowledge_retriever" not in st.session_state:
        st.session_state.knowledge_retriever = KnowledgeRetriever()

    if (
        "prep_agent" not in st.session_state
        or st.session_state.get("current_account_id") != client_id
        or st.session_state.get("current_account_name") != client_name
    ):
        st.session_state.prep_agent = MeetingPrepAgent(
            client_id=client_id,
            client_name=client_name,
        )
        st.session_state.current_account_id = client_id
        st.session_state.current_account_name = client_name

    return (
        st.session_state.supervisor,
        st.session_state.prep_agent,
        st.session_state.crm_retriever,
        st.session_state.knowledge_retriever,
    )


def load_preview_opportunities(client_id: str):
    opportunities_path = CRM_DIR / "opportunities.csv"

    if not opportunities_path.exists():
        return pd.DataFrame()

    opportunities = pd.read_csv(opportunities_path)

    if "AccountId" not in opportunities.columns:
        raise ValueError(
            "opportunities.csv must contain the AccountId column"
        )

    return opportunities[
        opportunities["AccountId"].astype(str).str.strip() == client_id
    ].copy()


def render_account_bundle(bundle):
    st.markdown("**Account**")
    st.dataframe(bundle["account"], width="stretch", hide_index=True)

    st.markdown("**Contacts**")
    st.dataframe(bundle["contacts"], width="stretch", hide_index=True)

    st.markdown("**Opportunities**")
    st.dataframe(bundle["opportunities"], width="stretch", hide_index=True)

    st.markdown("**Activities**")
    st.dataframe(bundle["activities"], width="stretch", hide_index=True)


def render_dynamic_citations(bundle, docs):
    opportunity_ids = (
        bundle["opportunities"]["OpportunityId"].dropna().astype(str).tolist()
        if "OpportunityId" in bundle["opportunities"].columns
        else []
    )

    activity_ids = (
        bundle["activities"]["ActivityId"].dropna().astype(str).tolist()
        if "ActivityId" in bundle["activities"].columns
        else []
    )

    if opportunity_ids:
        st.markdown("**CRM opportunity references:**")
        for opportunity_id in opportunity_ids:
            st.code(f"[Source: CRM {opportunity_id}]", language="text")

    if activity_ids:
        st.markdown("**CRM activity references:**")
        for activity_id in activity_ids:
            st.code(f"[Source: CRM {activity_id}]", language="text")

    if docs:
        st.markdown("**Knowledge-base documents:**")
        for doc in docs:
            st.code(f"[Document: {doc}]", language="text")


st.sidebar.caption(
    "Banker workspace: ACME_Banking"
)
with st.sidebar:
    selected_account_label = st.selectbox(
        "Select Institutional Account",
        options=list(ACCOUNT_OPTIONS.keys()),
        key="selected_account_label",
    )

    client_id, client_name = get_selected_account()

    action_trigger = st.selectbox(
        "Select Agent Task",
        [
            "Generate Executive Briefing",
            "Document Research Summary",
            "General CRM Inquiry",
        ],
        key="action_trigger",
    )

    run_btn = st.button("Execute Agent Flow", type="primary")


col1, col2 = st.columns([2, 1])


if run_btn:
    (
        supervisor,
        prep_agent,
        crm_retriever,
        knowledge_retriever,
    ) = get_agents(client_id, client_name)

    with st.spinner(
        "Executing multi-agent orchestration, CRM lookup, and knowledge grounding..."
    ):
        query_map = {
            "Generate Executive Briefing": (
                f"Prepare meeting briefing for {client_name}"
            ),
            "Document Research Summary": (
                f"Find research documents for {client_name}"
            ),
            "General CRM Inquiry": f"Show general info for {client_name}",
        }

        dynamic_query = query_map[action_trigger]
        routing = supervisor.route_intent(dynamic_query)

        st.sidebar.markdown("---")
        st.sidebar.success(f"Intent Routed: **{routing['intent']}**")

        if routing.get("matched_keyword"):
            st.sidebar.caption(
                f"Matched keyword: `{routing['matched_keyword']}`"
            )

        st.sidebar.caption(f"Target account: `{client_id}` — {client_name}")

        if routing["intent"] == "MEETING_PREP":
            briefing_output = prep_agent.generate_briefing()
            bundle = crm_retriever.get_account_bundle(client_id)
            docs = knowledge_retriever.list_documents()

            with col1:
                st.subheader("Executive Briefing")

                st.markdown("### Executive Snapshot")
                st.markdown(
                    f"- {client_name} is the institutional coverage target "
                    "for the upcoming meeting."
                )
                st.markdown(
                    "- Briefing synthesized only from CRM fixtures and "
                    "approved prompt guardrails."
                )

                st.markdown("### Pipeline Highlights")
                st.markdown(briefing_output)

                with st.expander("Show raw briefing text", expanded=False):
                    st.code(briefing_output, language="text")

            with col2:
                st.subheader("Grounding & Source Tracing")

                tab_crm, tab_research, tab_citations = st.tabs(
                    ["CRM", "Research", "Citations"]
                )

                with tab_crm:
                    st.metric(
                        "Active Opportunities",
                        len(bundle["opportunities"]),
                    )
                    st.metric(
                        "Related Contacts",
                        len(bundle["contacts"]),
                    )
                    st.metric(
                        "Recent Activities",
                        len(bundle["activities"]),
                    )

                    with st.expander(
                        "Account bundle details",
                        expanded=False,
                    ):
                        render_account_bundle(bundle)

                with tab_research:
                    if docs:
                        with st.expander(
                            "Available documents",
                            expanded=True,
                        ):
                            for doc in docs:
                                st.text(f"• [Document: {doc}]")
                    else:
                        st.warning(
                            "No documents found in knowledge base."
                        )

                with tab_citations:
                    render_dynamic_citations(bundle, docs)

        elif routing["intent"] == "DOCUMENT_SUMMARY":
            docs = knowledge_retriever.list_documents()

            with col1:
                st.subheader("Document Research Summary")

                st.markdown("### Knowledge Base Snapshot")
                st.markdown(
                    f"- {len(docs)} document(s) available for {client_name}."
                )
                st.markdown(
                    "- Retrieval scoped strictly to the approved "
                    "knowledge base (Zero Trust)."
                )

                st.markdown("### Available Documents")

                if docs:
                    for doc in docs:
                        st.markdown(f"- [Document: {doc}]")
                else:
                    st.warning("No documents found in knowledge base.")

            with col2:
                st.subheader("Grounding & Source Tracing")
                st.info(
                    "This route is document-only. No CRM lookup was "
                    "performed for this task."
                )

                with st.expander(
                    "Citation format used",
                    expanded=True,
                ):
                    for doc in docs:
                        st.code(
                            f"[Document: {doc}]",
                            language="text",
                        )

        elif routing["intent"] == "GENERAL_INQUIRY":
            bundle = crm_retriever.get_account_bundle(client_id)

            with col1:
                st.subheader("General CRM Inquiry")

                st.markdown("### Account Overview")
                st.dataframe(
                    bundle["account"],
                    width="stretch",
                    hide_index=True,
                )

                st.markdown("### Summary")
                st.markdown(
                    f"- Active Opportunities: "
                    f"{len(bundle['opportunities'])}"
                )
                st.markdown(
                    f"- Related Contacts: {len(bundle['contacts'])}"
                )
                st.markdown(
                    f"- Recent Activities: {len(bundle['activities'])}"
                )

            with col2:
                st.subheader("Related Records")

                tab_contacts, tab_opps, tab_acts = st.tabs(
                    ["Contacts", "Opportunities", "Activities"]
                )

                with tab_contacts:
                    st.dataframe(
                        bundle["contacts"],
                        width="stretch",
                        hide_index=True,
                    )

                with tab_opps:
                    st.dataframe(
                        bundle["opportunities"],
                        width="stretch",
                        hide_index=True,
                    )

                with tab_acts:
                    st.dataframe(
                        bundle["activities"],
                        width="stretch",
                        hide_index=True,
                    )

        else:
            with col1:
                st.warning(
                    f"Flow intercepted. The target route "
                    f"'{routing['intent']}' is not yet configured."
                )

else:
    with col1:
        st.info(
            "Select the institutional account in the sidebar and click "
            "**Execute Agent Flow** to run the briefing under Zero Trust rules."
        )

        st.subheader("CRM Data Preview")

        try:
            preview_opps = load_preview_opportunities(client_id)

            if preview_opps.empty:
                st.warning(
                    f"No opportunities found for {client_name} ({client_id})."
                )
            else:
                st.dataframe(
                    preview_opps,
                    width="stretch",
                    hide_index=True,
                )

        except Exception as exc:
            st.warning(f"Unable to load CRM opportunities: {exc}")

    with col2:
        st.subheader("Local Architecture Status")
        st.success("VSCode / WSL Lab: Active")
        st.success("Zero Trust Guardrails: Loaded")
        st.success("Citation Mapping: Enabled")


st.markdown("---")
st.caption(
    "Salesforce Agentforce PTA Assessment — "
    "Local Reference Architecture Blueprint"
)
