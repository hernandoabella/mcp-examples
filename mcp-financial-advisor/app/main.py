from fastapi import FastAPI
from app.bank_api import get_account_balances, get_recent_transactions
from app.investment_api import get_portfolio_summary
from app.mcp_schemas import MCPRequest, MCPResponse
import uuid

app = FastAPI()

@app.post("/mcp/financial-summary")
async def financial_summary(request: MCPRequest):
    # In a real app, use request.user_id or auth token to fetch user data
    # Here we simulate for demo user "user_001"
    user_id = request.user_id if hasattr(request, 'user_id') else "user_001"

    balances = await get_account_balances(user_id)
    transactions = await get_recent_transactions(user_id)
    portfolio = await get_portfolio_summary(user_id)

    summary = {
        "balances": balances,
        "recent_transactions": transactions,
        "investment_portfolio": portfolio
    }

    log_id = str(uuid.uuid4())
    return MCPResponse(
        request_id=request.request_id,
        result={
            "summary": summary,
            "log_id": log_id
        }
    )
