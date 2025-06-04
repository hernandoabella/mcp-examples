import asyncio

# Simulated investment portfolio data
INVESTMENT_PORTFOLIOS = {
    "user_001": {
        "stocks": {
            "AAPL": {"shares": 50, "current_price": 180.0},
            "TSLA": {"shares": 20, "current_price": 650.0},
        },
        "bonds": 10000,
    }
}

async def get_portfolio_summary(user_id: str):
    await asyncio.sleep(0.1)
    portfolio = INVESTMENT_PORTFOLIOS.get(user_id, {})
    total_stock_value = sum(
        shares["shares"] * shares["current_price"] for shares in portfolio.get("stocks", {}).values()
    )
    total_value = total_stock_value + portfolio.get("bonds", 0)
    return {
        "stocks": portfolio.get("stocks", {}),
        "bonds": portfolio.get("bonds", 0),
        "total_value": total_value
    }
