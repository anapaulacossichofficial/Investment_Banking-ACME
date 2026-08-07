"""
Supervisor Agent (Local Laboratory Blueprint)
Responsible for intent decomposition and routing queries for ACME INVESTMENTS.
"""
from typing import Dict

class SupervisorAgent:
    """
    Lightweight rule-based intent router.
    Maps a natural language query to one of three supported intents:
    MEETING_PREP, DOCUMENT_SUMMARY, or GENERAL_INQUIRY.
    """
    MEETING_PREP_KEYWORDS = ("meeting", "briefing", "prep")
    DOCUMENT_SUMMARY_KEYWORDS = ("document", "research")

    def __init__(self):
        print("[SupervisorAgent] Initialized intent router for institutional banking.")

    def route_intent(self, user_query: str) -> Dict[str, object]:
        """
        Routes a query to the correct intent based on keyword matching.
        Priority order: MEETING_PREP > DOCUMENT_SUMMARY > GENERAL_INQUIRY.
        """
        query_lower = user_query.lower()

        # 1. Highest Priority: Meeting Preparation
        matched_keyword = next(
            (kw for kw in self.MEETING_PREP_KEYWORDS if kw in query_lower), None
        )
        if matched_keyword:
            return {
                "intent": "MEETING_PREP",
                "target_account": "ACME INVESTMENTS",
                "requires_crm": True,
                "requires_knowledge": True,
                "matched_keyword": matched_keyword,
            }

        # 2. Medium Priority: Document & Research
        matched_keyword = next(
            (kw for kw in self.DOCUMENT_SUMMARY_KEYWORDS if kw in query_lower), None
        )
        if matched_keyword:
            return {
                "intent": "DOCUMENT_SUMMARY",
                "target_account": "ACME INVESTMENTS",
                "requires_crm": False,
                "requires_knowledge": True,
                "matched_keyword": matched_keyword,
            }

        # 3. Fallback: General CRM Inquiry
        return {
            "intent": "GENERAL_INQUIRY",
            "target_account": "ACME INVESTMENTS",
            "requires_crm": True,
            "requires_knowledge": False,
            "matched_keyword": None,
        }