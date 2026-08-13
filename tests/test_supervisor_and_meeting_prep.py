from agents.meeting_prep_agent import MeetingPrepAgent
from agents.supervisor_agent import SupervisorAgent


def test_supervisor_routes_intents():
    supervisor = SupervisorAgent()

    meeting = supervisor.route_intent("Prepare meeting briefing for client")
    assert meeting["intent"] == "MEETING_PREP"
    assert meeting["requires_crm"] is True
    assert meeting["requires_knowledge"] is True

    doc = supervisor.route_intent("research document summary")
    assert doc["intent"] == "DOCUMENT_SUMMARY"

    general = supervisor.route_intent("show account info")
    assert general["intent"] == "GENERAL_INQUIRY"


def test_meeting_prep_agent_generates_hybrid_grounded_briefing():
    agent = MeetingPrepAgent(
        client_id="ACC-001",
        client_name="QUANTUM INVESTMENTS",
    )

    briefing = agent.generate_briefing()

    assert isinstance(briefing, str)
    assert len(briefing) > 0
    assert "CRM Snapshot:" in briefing
    assert "Evidence Context:" in briefing
    assert "Approved knowledge sources available:" in briefing
    assert "Validation Guardrail:" in briefing
    assert "The briefing is grounded in account-specific CRM records and approved knowledge sources." in briefing
