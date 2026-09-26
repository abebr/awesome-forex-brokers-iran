# Forex Broker Spread & Trading Cost Calculator
# Author: BestAmooz Academy & Contributors
# License: MIT

def calculate_trade_cost(symbol: str, lot_size: float, spread_pips: float, commission_per_lot_usd: float = 0.0) -> dict:
    """
    Calculates total round-turn trading cost (Spread + Commission) in USD for major Forex pairs and Gold.
    """
    pip_value = 10.0 * lot_size if "JPY" not in symbol else 6.7 * lot_size
    if symbol.upper() in ["XAUUSD", "GOLD"]:
        pip_value = 1.0 * lot_size * 10  # 1 pip in Gold = $10 per standard lot
        
    spread_cost_usd = spread_pips * pip_value
    commission_total = commission_per_lot_usd * lot_size
    total_cost_usd = spread_cost_usd + commission_total
    
    return {
        "symbol": symbol,
        "lot_size": lot_size,
        "spread_pips": spread_pips,
        "spread_cost_usd": round(spread_cost_usd, 2),
        "commission_usd": round(commission_total, 2),
        "total_cost_usd": round(total_cost_usd, 2)
    }

if __name__ == "__main__":
    brokers = [
        {"broker": "AMarkets (ECN)", "spread": 0.2, "commission": 5.0},
        {"broker": "Alpari (Pro ECN)", "spread": 0.4, "commission": 3.2},
        {"broker": "LiteFinance (Classic)", "spread": 1.4, "commission": 0.0},
        {"broker": "ForexChief (DirectFX)", "spread": 0.3, "commission": 3.0}
    ]
    
    print("=== EURUSD 1.0 Lot Round-Turn Cost Comparison ===")
    for b in brokers:
        res = calculate_trade_cost("EURUSD", 1.0, b["spread"], b["commission"])
        print(f"[{b['broker']}] Total Cost: ${res['total_cost_usd']} (Spread: ${res['spread_cost_usd']} + Comm: ${res['commission_usd']})")
