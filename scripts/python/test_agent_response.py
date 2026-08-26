import requests, json, os

SF_DOMAIN = os.getenv("SF_DOMAIN")
ACCESS_TOKEN = os.getenv("SF_ACCESS_TOKEN")
AGENT_ID = os.getenv("SF_AGENT_ID")

session_resp = requests.post(
    f"{SF_DOMAIN}/services/data/v61.0/agents/{AGENT_ID}/sessions",
    headers={"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"},
    json={"externalSessionKey": "acme-test-session-001"}
)
session_resp.raise_for_status()
session_id = session_resp.json()["sessionId"]

msg_resp = requests.post(
    f"{SF_DOMAIN}/services/data/v61.0/agents/sessions/{session_id}/messages",
    headers={"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"},
    json={"message": {"type": "Text", "text": "Gere o briefing de reuniao para QUANTUM INVESTMENTS"}}
)
data = msg_resp.json()
reply = data.get("messages", [{}])[0].get("message", "")
print(reply)

expected = ["Resumo Executivo", "Analise de Risco", "Concorrentes"]
missing = [s for s in expected if s.lower() not in reply.lower()]
print("Missing sections:" if missing else "All sections present.", missing)
