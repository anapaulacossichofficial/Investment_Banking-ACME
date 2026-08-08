from agents.meeting_prep_agent import MeetingPrepAgent
from agents.supervisor_agent import SupervisorAgent


def test_supervisor_routes_intents():
    supervisor = SupervisorAgent()

    meeting = supervisor.route_intent("Prepare meeting briefing for client")
    assert meeting["intent"] == "MEETING_PREP"

    doc = supervisor.route_intent("research document summary")
    assert doc["intent"] == "DOCUMENT_SUMMARY"

    general = supervisor.route_intent("show account info")
    assert general["intent"] == "GENERAL_INQUIRY"


def test_meeting_prep_agent_generates_briefing():
    agent = MeetingPrepAgent(client_id="ACC-001", client_name="QUANTUM INVESTMENTS")
    briefing = agent.generate_briefing()
    assert isinstance(briefing, str)
    assert len(briefing) > 0