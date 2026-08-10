from src.orchestration.handoff_contract import HandoffContract

def test_handoff_contract_generation():
    contract = HandoffContract(
        source_agent="Supervisor",
        target_agent="MeetingPrepAgent",
        context_payload={"account_name": "Quantum"},
        allowed_tools=["crm_retriever", "knowledge_retriever"]
    )
    
    data = contract.to_dict()
    assert data["event"] == "A2A_HANDOFF"
    assert data["target_agent"] == "MeetingPrepAgent"
    assert data["context_payload"]["account_name"] == "Quantum"
    assert "crm_retriever" in data["allowed_tools"]
    assert isinstance(data["trace_id"], str)
    assert len(data["trace_id"]) > 0