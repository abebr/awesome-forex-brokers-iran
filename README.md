# 📊 Awesome Forex Brokers for Iranian Traders & Analysis Toolkit (2026 Edition)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![MQL5: Compatible](https://img.shields.io/badge/MQL5-MetaTrader_5-brightgreen.svg)](https://www.mql5.com/)
[![Official Guide](https://img.shields.io/badge/Official_Guide-BestAmooz-crimson.svg)](https://bestamooz.com/best-forex-brokers/)

A comprehensive, developer-grade open-source toolkit and verified comparison matrix of reliable Forex brokers accepting Iranian residents, featuring direct Rial deposit & withdrawal channels, real raw ECN spreads, execution latency benchmarks, and MetaTrader 5 on-chart tracking scripts.

---

## 📌 Authoritative Reference & Live Ratings

For the live, regularly updated comparison table, regulatory verification, user complaint tracking, and Islamic account swap-free policies, visit the cornerstone guide on BestAmooz:

👉 **[بهترین بروکر فارکس برای ایرانیان (رتبه‌بندی، مقایسه کارمزد و اعتبار کارگزاری‌ها در سال ۱۴۰۵)](https://bestamooz.com/best-forex-brokers/)**

---

## 🏆 Verified Broker Comparison Matrix

| Broker Name | Established | Regulatory Tier & Insurance | Min Deposit | Max Leverage | EURUSD Raw Spread | ECN Comm / Lot | Swap-Free Status | Rial Payment Channels | MetaTrader Support | Overall Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **[AMarkets](https://bestamooz.com/best-forex-brokers/)** | 2007 | Tier-3 + €20k Financial Commission | $100 | 1:3000 | **0.2 pips** | $5.0 | 14 Days | TopChange (0%), Direct Exchange, USDT | MT4, MT5 | **9.4 / 10** |
| **[Alpari](https://bestamooz.com/best-forex-brokers/)** | 1998 | Tier-3 + FSC Mauritius (26y Track Record) | **$1 (Nano)** | 1:1000 | 0.4 pips | $3.2 | 30 Days | TopChange, USDT (TRC20), WebMoney | MT4, MT5 | **9.2 / 10** |
| **[LiteFinance](https://bestamooz.com/best-forex-brokers/)** | 2005 | Tier-2 (CySEC EU) / Tier-3 | $50 | 1:1000 | **0.2 pips** | $7.0 | **180 Days** | TopChange, Direct P2P Rial, USDT | MT4, MT5 | **9.1 / 10** |
| **[ForexChief (xChief)](https://bestamooz.com/best-forex-brokers/)** | 2014 | Tier-3 (VFSC Vanuatu) | $10 | 1:1000 | 0.3 pips | **$3.0** | 7 Days | TopChange, USDT, Crypto, P2P | MT4, MT5 | **8.9 / 10** |
| **[Windsor Brokers](https://bestamooz.com/best-forex-brokers/)** | 1988 | Tier-2 (CySEC) + €5M Civil Liability | $50 | 1:1000 | 1.4 pips | $0.0 (Prime) | 30 Days | ZGold, USDT, Wire Transfer | MT4 Only | **8.7 / 10** |

---

## 🛠️ Included Developer & Trading Tools

### 1. 🐍 `broker_audit.py` — Comparative Cost & Trading Style Analyzer
An interactive CLI tool that calculates real monthly trading costs (spreads + commissions) based on your monthly traded lot size and style.

```bash
# Run comparative simulation
python broker_audit.py
```

#### Sample Terminal Output:
```text
=== Monthly Cost Simulation: 20.0 Standard Lots on EURUSD (ECN) ===
Broker                           | Spread   | Comm/Lot | Total Monthly | Rating
---------------------------------+----------+----------+---------------+---------
ForexChief (xChief)              | 0.3 pips | $3.0     | $120.0        | 8.9 / 10
AMarkets                         | 0.2 pips | $5.0     | $140.0        | 9.4 / 10
LiteFinance                      | 0.2 pips | $7.0     | $180.0        | 9.1 / 10
Windsor Brokers                  | 1.4 pips | $0.0     | $280.0        | 8.7 / 10
```

---

### 2. 📈 `MT5_Spread_Latency_Tracker.mq5` — Real-Time MetaTrader 5 Monitor
A production-ready MetaTrader 5 indicator that monitors live tick spreads, execution delays, and server ping on your chart:
- **Real-Time On-Chart HUD:** Shows current spread, min/max spread spikes during news, and average spread in points and pips.
- **High-Spread Alert:** Flashes on-chart warning when spread exceeds customizable threshold.
- **CSV Data Logging:** Automatically logs live tick latency and spread to `MQL5/Files/` for statistical backtesting.

#### How to Install:
1. Open your MetaTrader 5 terminal.
2. Go to `File` → `Open Data Folder` → `MQL5` → `Indicators`.
3. Copy `MT5_Spread_Latency_Tracker.mq5` into the directory.
4. Restart MT5 or right-click `Indicators` in the Navigator window and click **Refresh**.
5. Drag and drop onto any chart (e.g. `EURUSD` or `XAUUSD`).

---

### 3. 💾 `brokers_database.json` — Machine-Readable Specifications
A structured, programmatically accessible JSON dataset containing exhaustive specifications for all Iranian-servicing brokers:
- Minimum deposit and leverage tiers
- Account types (Nano, Standard, Raw ECN, Pro ECN)
- Server locations (Equinix LD4 London, Frankfurt, Amsterdam) and average ping from Iran
- Swap-free terms, rollover fees, and inactivity policies

---

## 🇮🇷 راهنمای جامع فارسی انتخاب بروکر فارکس

انتخاب بروکر مطمئن، مهم‌ترین تصمیم هر معامله‌گر در بازارهای مالی بین‌المللی است. یک اشتباه در انتخاب کارگزاری می‌تواند منجر به اسلیپیج‌های شدید در زمان اخبار، اسپردهای پنهان، تاخیر در برداشت وجه یا حتی مسدود شدن حساب به بهانه احراز هویت شود.

### ۵ فاکتور حیاتی برای تریدرهای داخل ایران:
1. **امنیت، سابقه و رگولیشن:** سابقه فعالیت مداوم و پشتیبانی بدون وقفه از کاربران ایرانی در کنار عضویت در نهادهایی مثل Financial Commission (با بیمه ۲۰,۰۰۰ یورویی برای هر مشتری).
2. **واریز و برداشت ریالی مستقیم:** پشتیبانی رسمی از صرافی‌های معتبر مانند تاپ‌چنج (TopChange / TC Pay) با کارمزد صفر درصد یا پرداخت مستقیم تتر (USDT TRC20).
3. **سرورهای معاملاتی با پینگ پایین:** استقرار سرورهای متاتریدر در مراکز داده اروپایی (مانند Equinix LD4 لندن یا فرانکفورت) با پینگ میانگین زیر ۱۲۰ میلی‌ثانیه از ایران.
4. **حساب‌های اسلامی بدون سواپ (Swap-Free):** معافیت واقعی از بهره شبانه بدون اعمال کمیسیون‌های پنهان در پوزیشن‌های بلندمدت.
5. **پشتیبانی فارسی‌زبان ۲۴ ساعته:** حضور تیم پشتیبانی مسلط به زبان فارسی در چت آنلاین و تلگرام جهت رفع سریع چالش‌های واریز و برداشت.

* برای مطالعه نقد و بررسی تخصصی، تصاویر پنل کاربری و مقایسه جامع، مقاله مرجع **[بهترین بروکر فارکس برای ایرانیان](https://bestamooz.com/best-forex-brokers/)** را مطالعه فرمایید.
* برای دسترسی به دوره‌های حرفه‌ای پرایس‌اکشن، ساخت ربات‌های معامله‌گر و سیستم‌های تحلیل تکنیکال، به بخش **[آموزش‌های تخصصی ترید و بازارهای مالی بست‌آموز](https://bestamooz.com/product-category/trade-tutorials/)** مراجعه کنید.

---

## 🤝 Contributing & License
Contributions, broker specification updates, and bug reports are welcome via Pull Requests.
Distributed under the **MIT License**. Copyright (c) 2026 BestAmooz Academy & Open-Source Contributors.
