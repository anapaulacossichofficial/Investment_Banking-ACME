import json
from pathlib import Path

def test_tool_contract_schema_validity():
    schema_path = Path("src/contracts/tool_contract.schema.json")
    assert schema_path.exists(), "Tool contract schema file is missing."
    
    with schema_path.open("r", encoding="utf-8") as f:
        schema = json.load(f)
        
    assert schema.get("title") == "ToolContract"
    assert "tool_name" in schema.get("required", [])
    assert "input_schema" in schema.get("required", [])