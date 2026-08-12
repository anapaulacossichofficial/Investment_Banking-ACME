from dataclasses import dataclass, asdict
from typing import Any, Dict, List
import uuid

@dataclass
class HandoffContract:
    event: str = "A2A_HANDOFF"
    source_agent: str = "Supervisor"
    target_agent: str = "MeetingPrepAgent"
    trace_id: str = ""
    context_payload: Dict[str, Any] = None
    allowed_tools: List[str] = None

    def to_dict(self):
        data = asdict(self)
        data["trace_id"] = data["trace_id"] or str(uuid.uuid4())
        data["context_payload"] = data["context_payload"] or {}
        data["allowed_tools"] = data["allowed_tools"] or []
        return data