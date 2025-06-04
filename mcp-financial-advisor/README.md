# MCP Financial Advisor Assistant
This project shows a simple MCP-compatible financial assistant that aggregates bank and investment data.

## Features

- Simulated bank balances and transactions
- Simulated investment portfolio
- Context-aware financial summary response

### Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

### Test Endpoint
POST http://127.0.0.1:8000/mcp/financial-summary

### JSON body example:
```json
{
  "request_id": "abc123",
  "action": "get_financial_summary",
  "user_id": "user_001"
}
```