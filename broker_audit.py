#!/usr/bin/env python3
"""
Forex Broker Comparative Audit & Cost Analyzer for Iranian Traders
Author: BestAmooz Academy & Open-Source Contributors
Website: https://bestamooz.com/best-forex-brokers/
License: MIT
"""

import sys, json, os
from pathlib import Path

DB_FILE = Path(__file__).parent / "brokers_database.json"

def load_brokers():
    if not DB_FILE.exists():
        print(f"Error: Database file '{DB_FILE}' not found.", file=sys.stderr)
        sys.exit(1)
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["brokers"]

def calculate_monthly_trading_cost(broker, symbol="EURUSD", monthly_lots=10.0, account_type="ecn"):
    # Determine spread and commission
    acc = broker.get("account_types", {}).get(account_type)
    if not acc:
        # fallback to standard or first available
        acc = next(iter(broker.get("account_types", {}).values()))
        
    spread_pips = broker.get("average_spreads", {}).get(symbol, 1.0)
    comm_per_lot = acc.get("commission_per_lot", 0.0)
    
    # 1 pip on EURUSD for 1 standard lot = $10.0
    pip_val = 10.0 if "JPY" not in symbol else 6.7
    if symbol in ["XAUUSD", "GOLD"]:
        pip_val = 10.0  # 1 pip on gold (0.10) = $10/lot
        
    spread_cost_month = spread_pips * pip_val * monthly_lots
    commission_month = comm_per_lot * monthly_lots
    total_cost = spread_cost_month + commission_month
    
    return {
        "broker": broker["name"],
        "account_type": account_type,
        "spread_pips": spread_pips,
        "commission_lot": comm_per_lot,
        "monthly_spread_usd": round(spread_cost_month, 2),
        "monthly_comm_usd": round(commission_month, 2),
        "total_cost_usd": round(total_cost, 2),
        "rating": broker["rating_overall"],
        "min_deposit": broker["min_deposit_usd"],
        "max_leverage": broker["max_leverage"],
        "ping_iran": broker["avg_ping_iran_ms"],
        "swap_free_days": broker["swap_free"]["duration_days"],
        "deposit_channels": ", ".join(broker["payment_methods"][:2])
    }

def print_table(rows, headers):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val)))
            
    header_str = " | ".join(f"{h:<{widths[i]}}" for i, h in enumerate(headers))
    separator = "-+-".join("-" * widths[i] for i in range(len(headers)))
    print(header_str)
    print(separator)
    for row in rows:
        print(" | ".join(f"{str(val):<{widths[i]}}" for i, val in enumerate(row)))

def main():
    brokers = load_brokers()
    
    print("=" * 80)
    print("🏆 BESTAMOOZ FOREX BROKER COMPARATIVE AUDIT (2026 EDITION)")
    print("Authoritative Guide: https://bestamooz.com/best-forex-brokers/")
    print("=" * 80)
    
    # Simulation: 20 lots EURUSD per month on ECN
    print("\n📊 1. Monthly Cost Simulation: 20.0 Standard Lots on EURUSD (ECN Accounts)")
    sim_rows = []
    for b in brokers:
        res = calculate_monthly_trading_cost(b, symbol="EURUSD", monthly_lots=20.0, account_type="ecn")
        sim_rows.append([
            res["broker"],
            f"{res['spread_pips']} pips",
            f"${res['commission_lot']}",
            f"${res['monthly_spread_usd']}",
            f"${res['monthly_comm_usd']}",
            f"${res['total_cost_usd']}",
            f"{res['rating']} / 10"
        ])
        
    sim_rows.sort(key=lambda x: float(x[5].replace("$", "")))
    print_table(sim_rows, ["Broker", "Spread", "Comm/Lot", "Spread Cost", "Comm Cost", "Total Monthly", "Rating"])

    # 2. Key Operational Specs Matrix
    print("\n🌐 2. Operational Specs & Iran Direct Payment Channels")
    specs_rows = []
    for b in brokers:
        specs_rows.append([
            b["name"],
            f"${b['min_deposit_usd']}",
            b["max_leverage"],
            f"{b['avg_ping_iran_ms']} ms",
            f"{b['swap_free']['duration_days']} Days",
            ", ".join(b["platforms"][:2]),
            ", ".join(b["payment_methods"][:2])
        ])
        
    print_table(specs_rows, ["Broker", "Min Dep", "Leverage", "Avg Ping", "Swap-Free", "Platforms", "Primary Channels"])

    print("\n💡 Verdict & Best Fit by Trading Style:")
    print("  • Best for Raw Scalping & Low Spreads: AMarkets (ECN) & ForexChief (DirectFX)")
    print("  • Best for Social Copy Trading & Web Terminal: LiteFinance")
    print("  • Best for Beginners & Micro Accounts ($1 Cent): Alpari (Nano Account)")
    print("  • Best for Swing Trading & Institutional Safety: Windsor Brokers (€5M Insurance)")
    print("\nFull ratings & live user feedback: https://bestamooz.com/best-forex-brokers/\n")

if __name__ == "__main__":
    main()
