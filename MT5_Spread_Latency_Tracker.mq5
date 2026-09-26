//+------------------------------------------------------------------+
//|                                  MT5_Spread_Latency_Tracker.mq5   |
//|                    Copyright 2026, BestAmooz Academy              |
//|                     https://bestamooz.com/best-forex-brokers/    |
//+------------------------------------------------------------------+
#property copyright "Copyright 2026, BestAmooz Academy"
#property link      "https://bestamooz.com/best-forex-brokers/"
#property version   "1.00"
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

//--- Input Parameters
input group "=== Tracker Settings ==="
input bool     InpLogToFile       = true;        // Log metrics to CSV file in MQL5/Files
input int      InpUpdateInterval  = 1;           // Screen update interval (seconds)
input color    InpTextColor       = clrWhite;    // Dashboard Text Color
input color    InpWarningColor    = clrRed;      // High Spread / Alert Color
input int      InpMaxAcceptSpread = 25;          // Alert Threshold in Points (2.5 pips)

//--- Global Variables
string         g_fileName;
int            g_fileHandle = INVALID_HANDLE;
double         g_minSpread = 999999.0;
double         g_maxSpread = 0.0;
double         g_sumSpread = 0.0;
ulong          g_tickCount = 0;
datetime       g_lastUpdateTime = 0;

//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
int OnInit()
{
   EventSetTimer(InpUpdateInterval);
   
   if(InpLogToFile)
   {
      g_fileName = "BestAmooz_Spread_Log_" + _Symbol + "_" + TimeToString(TimeCurrent(), TIME_DATE) + ".csv";
      StringReplace(g_fileName, ".", "-");
      StringReplace(g_fileName, ":", "-");
      
      g_fileHandle = FileOpen(g_fileName, FILE_WRITE|FILE_CSV|FILE_ANSI|FILE_COMMON, ",");
      if(g_fileHandle != INVALID_HANDLE)
      {
         FileWrite(g_fileHandle, "Timestamp", "Symbol", "Bid", "Ask", "Spread_Points", "Spread_Pips", "Server_Latency_ms");
      }
   }
   
   CreateDashboard();
   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Custom indicator deinitialization function                       |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   EventKillTimer();
   
   if(g_fileHandle != INVALID_HANDLE)
   {
      FileClose(g_fileHandle);
      g_fileHandle = INVALID_HANDLE;
   }
   
   ObjectsDeleteAll(0, "BA_Spread_");
   Comment("");
}

//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
{
   MqlTick lastTick;
   if(SymbolInfoTick(_Symbol, lastTick))
   {
      double currentSpreadPoints = (lastTick.ask - lastTick.bid) / _Point;
      double currentSpreadPips   = currentSpreadPoints / 10.0;
      
      if(currentSpreadPoints < g_minSpread) g_minSpread = currentSpreadPoints;
      if(currentSpreadPoints > g_maxSpread) g_maxSpread = currentSpreadPoints;
      
      g_sumSpread += currentSpreadPoints;
      g_tickCount++;
      
      // Log to CSV
      if(InpLogToFile && g_fileHandle != INVALID_HANDLE && (g_tickCount % 5 == 0))
      {
         ulong latency = (ulong)(GetTickCount64() - lastTick.time_msc);
         FileWrite(g_fileHandle, TimeToString(lastTick.time, TIME_DATE|TIME_SECONDS),
                   _Symbol, 
                   DoubleToString(lastTick.bid, _Digits), 
                   DoubleToString(lastTick.ask, _Digits),
                   DoubleToString(currentSpreadPoints, 1),
                   DoubleToString(currentSpreadPips, 2),
                   latency);
         FileFlush(g_fileHandle);
      }
   }
   
   return(rates_total);
}

//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
{
   UpdateDashboard();
}

//+------------------------------------------------------------------+
//| Helper: Create On-Chart Dashboard UI                            |
//+------------------------------------------------------------------+
void CreateDashboard()
{
   string name = "BA_Spread_Dashboard";
   if(ObjectFind(0, name) < 0)
   {
      ObjectCreate(0, name, OBJ_RECTANGLE_LABEL, 0, 0, 0);
      ObjectSetInteger(0, name, OBJPROP_XDISTANCE, 20);
      ObjectSetInteger(0, name, OBJPROP_YDISTANCE, 30);
      ObjectSetInteger(0, name, OBJPROP_XSIZE, 240);
      ObjectSetInteger(0, name, OBJPROP_YSIZE, 130);
      ObjectSetInteger(0, name, OBJPROP_BGCOLOR, C'20,24,36');
      ObjectSetInteger(0, name, OBJPROP_BORDER_TYPE, BORDER_FLAT);
      ObjectSetInteger(0, name, OBJPROP_COLOR, C'225,29,72');
      ObjectSetInteger(0, name, OBJPROP_WIDTH, 1);
      ObjectSetInteger(0, name, OBJPROP_CORNER, CORNER_LEFT_UPPER);
   }
}

//+------------------------------------------------------------------+
//| Helper: Update Dashboard Text                                    |
//+------------------------------------------------------------------+
void UpdateDashboard()
{
   MqlTick lastTick;
   if(!SymbolInfoTick(_Symbol, lastTick)) return;
   
   double curPoints = (lastTick.ask - lastTick.bid) / _Point;
   double curPips   = curPoints / 10.0;
   double avgPoints = g_tickCount > 0 ? (g_sumSpread / g_tickCount) : curPoints;
   
   string serverName = AccountInfoString(ACCOUNT_SERVER);
   long pingMs       = TerminalInfoInteger(TERMINAL_PING_LAST) / 1000;
   
   string text = StringFormat(
      "=== BESTAMOOZ BROKER AUDIT ===\n" +
      "Server: %s (%d ms)\n" +
      "Current Spread: %.1f pts (%.2f pips)\n" +
      "Avg Spread: %.1f pts (Min: %.1f | Max: %.1f)\n" +
      "Recorded Ticks: %d\n" +
      "Status: %s",
      serverName, pingMs,
      curPoints, curPips,
      avgPoints, g_minSpread == 999999.0 ? curPoints : g_minSpread, g_maxSpread,
      g_tickCount,
      curPoints > InpMaxAcceptSpread ? "HIGH SPREAD WARNING!" : "NORMAL"
   );
   
   Comment(text);
}
//+------------------------------------------------------------------+
