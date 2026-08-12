"""
Observability Contract Tests (ib-agent-demo)

Validates the local telemetry schema and KPI calculations used
to demonstrate Agentforce observability requirements.
"""

import json
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parent.parent
FIXTURE_FILE = ROOT_DIR / "tests" / "fixtures" / "observability_events.jsonl"


def load_events():
    """Loads telemetry events from the deterministic JSONL fixture."""
    assert FIXTURE_FILE.is_file(), (
        f"Missing telemetry fixture: {FIXTURE_FILE}"
    )

    return [
        json.loads(line)
        for line in FIXTURE_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def group_sessions(events):
    """Groups telemetry events by session identifier."""
    sessions = {}

    for event in events:
        session_id = event["session_id"]
        sessions.setdefault(session_id, []).append(event)

    return sessions


def response_events(sessions):
    """Returns response_completed events independently of event position."""
    return [
        event
        for events in sessions.values()
        for event in events
        if event["event"] == "response_completed"
    ]


def test_observability_fixture_exists():
    """Validates that the telemetry fixture exists."""
    assert FIXTURE_FILE.is_file()


def test_required_event_schema():
    """Validates mandatory fields for every telemetry event."""
    events = load_events()
    required_fields = {"event", "session_id", "timestamp_ms"}

    for event in events:
        assert required_fields.issubset(event), (
            f"Telemetry event is missing required fields: {event}"
        )


def test_grounded_answer_rate():
    """Validates the proportion of eligible grounded responses."""
    sessions = group_sessions(load_events())
    responses = response_events(sessions)

    grounded_count = sum(
        bool(event.get("grounded", False))
        for event in responses
        if not event.get("fallback", False)
    )

    eligible_count = sum(
        not event.get("fallback", False)
        for event in responses
    )

    assert eligible_count > 0

    grounded_answer_rate = grounded_count / eligible_count

    assert grounded_answer_rate == pytest.approx(2 / 3)


def test_fallback_rate():
    """Validates the proportion of responses using fallback."""
    sessions = group_sessions(load_events())
    responses = response_events(sessions)

    assert responses

    fallback_count = sum(
        bool(event.get("fallback", False))
        for event in responses
    )

    fallback_rate = fallback_count / len(responses)

    assert fallback_rate == pytest.approx(1 / 4)


def test_citation_coverage():
    """Validates the proportion of claims with citations."""
    sessions = group_sessions(load_events())
    responses = response_events(sessions)

    total_claims = sum(
        event.get("claim_count", 0)
        for event in responses
    )

    cited_claims = sum(
        event.get("cited_claim_count", 0)
        for event in responses
    )

    assert total_claims > 0

    citation_coverage = cited_claims / total_claims

    assert citation_coverage == pytest.approx(7 / 8)


def test_session_latency():
    """Validates start-to-completion latency for every session."""
    sessions = group_sessions(load_events())
    latencies = []

    for session_id, events in sessions.items():
        started = next(
            event
            for event in events
            if event["event"] == "session_started"
        )

        completed = next(
            event
            for event in events
            if event["event"] == "session_completed"
        )

        latency = (
            completed["timestamp_ms"]
            - started["timestamp_ms"]
        )

        assert latency >= 0, (
            f"Negative latency detected for session {session_id}"
        )

        latencies.append(latency)

    assert latencies == [800, 200, 500, 100]


def test_supervisor_route_trace():
    """Validates traceability of Supervisor routing transitions."""
    sessions = group_sessions(load_events())

    for session_id, events in sessions.items():
        route_events = [
            event
            for event in events
            if event["event"] == "supervisor_route"
        ]

        for route_event in route_events:
            assert route_event["from"] == "SUPERVISOR", (
                f"Invalid route origin in session {session_id}"
            )
            assert route_event.get("to"), (
                f"Missing route target in session {session_id}"
            )
            assert route_event.get("timestamp_ms") is not None


def test_guardrail_event_is_traceable():
    """Validates that guardrail activation is recorded."""
    sessions = group_sessions(load_events())

    guardrail_events = [
        event
        for events in sessions.values()
        for event in events
        if event["event"] == "guardrail_triggered"
    ]

    assert len(guardrail_events) == 1
    assert guardrail_events[0]["guardrail"] == "hallucination_rejection"