import asyncio

# Simulated bank data
BANK_ACCOUNTS = {
    "user_001": {
        "checking": 3250.50,
        "savings": 15800.75,
    }
}

BANK_TRANSACTIONS = {
    "user_001": [
        {"date": "2025-06-01", "amount": -120.0, "desc": "Groceries"},
        {"date": "2025-06-02", "amount": -50.0, "desc": "Gas"},
        {"date": "2025-06-03", "amount": 1500.0, "desc": "Paycheck"},
    ]
}

async def get_account_balances(user_id: str):
    # Simulate API latency
    await asyncio.sleep(0.1)
    return BANK_ACCOUNTS.get(user_id, {})

async def get_recent_transactions(user_id: str):
    await asyncio.sleep(0.1)
    return BANK_TRANSACTIONS.get(user_id, [])
