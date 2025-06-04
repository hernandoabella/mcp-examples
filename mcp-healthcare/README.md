# MCP Healthcare AI Tooling

This project demonstrates how to build an MCP-compatible healthcare assistant using FastAPI.

## Features
- AI-assisted clinical advice
- Simulated EHR database
- Modular and testable architecture

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload


Sample Request (using curl or Postman):
POST http://127.0.0.1:8000/mcp/clinical-advice

JSON body:

```json
{
  "request_id": "12345",
  "action": "get_clinical_advice",
  "patient_id": "patient_001"
}
```