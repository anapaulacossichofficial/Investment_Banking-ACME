import requests, json, os

SF_DOMAIN = os.getenv("SF_DOMAIN")
ACCESS_TOKEN = os.getenv("SF_ACCESS_TOKEN")
AGENT_ID = os.getenv("SF_AGENT_ID")

# Base endpoint for the Agent API
BASE_URL = f"{SF_DOMAIN}/services/data/v61.0/einstein/ai-agent/v1"

print(f"Starting session for Agent: {AGENT_ID}...")
session_resp = requests.post(
    f"{BASE_URL}/agents/{AGENT_ID}/sessions",
    headers={"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"},
    json={"externalSessionKey": "acme-test-session-002"}
)

if session_resp.status_code != 201 and session_resp.status_code != 200:
    print(f"Error creating session: {session_resp.status_code} - {session_resp.text}")
    exit(1)

session_id = session_resp.json()["sessionId"]
print(f"Session created successfully. ID: {session_id}")
print("Sending prompt to the API...")

msg_resp = requests.post(
    f"{BASE_URL}/sessions/{session_id}/messages",
    headers={"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"},
    json={"message": {"type": "Text", "text": "Generate the meeting briefing for QUANTUM INVESTMENTS."}}
)

if msg_resp.status_code != 201 and msg_resp.status_code != 200:
    print(f"Error sending message: {msg_resp.status_code} - {msg_resp.text}")
    exit(1)

data = msg_resp.json()
# Extracting the response safely
messages = data.get("messages", [])
if messages:
    reply = messages[0].get("message", "")
else:
    reply = str(data) # Fallback in case of unexpected JSON structure
    
print("\n=== AGENT RESPONSE ===")
print(reply)
print("======================\n")

# Expected sections mapped to English based on standard prompt instructions
expected = ["Executive Summary", "Risk Analysis", "Competitors"]
missing = [s for s in expected if s.lower() not in reply.lower()]

print("Sections Validation:")
if missing:
    print("Status: MISSING", missing)
else:
    print("Status: SUCCESS - All required sections are present.")
