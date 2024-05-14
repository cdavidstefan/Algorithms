from time import time
import MetaTrader5 as mt5


mt5.initialize()


# class CTrade:
#     pass
#
#
# class CPositionInfo:
#     def Profit(self):
#         pass
#
#     def PriceOpen(self):
#         pass
#
#
# class AccountInfo:
#     @staticmethod
#     def Double(ACCOUNT_BALANCE):
#         pass
#
#
# def Print(message):
#     print(message)
#
#
# def EventSetTimer(timeToGo):
#     pass
#
#
# def EventKillTimer():
#     pass
#
#
# def PositionsTotal():
#     return 0
#
#
# def PositionGetTicket(index):
#     return 0
#
#
# def PositionSelectByTicket(ticket):
#     pass
#
#
# def SymbolInfoDouble(symbol, symbol_type):
#     return 0
#
#
# def iRSI(symbol, timeframe, period, price_type):
#     return 0
#
#
# def ExtTrade_PositionOpen(symbol, order_type, volume, price, sl, tp):
#     return True
#
#
# def ExtTrade_PositionClose(ticket, deviation):
#     return True
#
#
# def TimeCurrent():
#     return int(time())
#
#
# def PeriodSeconds(period):
#     return 3600
#
#
# def GetLastError():
#     return 0
#
#
# # Constants
# deviation = 3
# timeToGo = 1
# defaultvolume = 0.20
# takeProfit = 30
# maxPositions = 10
#
# # Callback functions
# def OnInit():
#     Print("OnInit!")
#     x = AccountInfo.Double("ACCOUNT_BALANCE")
#     EventSetTimer(timeToGo)
#     return True
#
# def OnDeinit(reason):
#     Print("OnDeInit!")
#     EventKillTimer()
#
# def OnTick():
#     pass
#
# def OnTimer():
#     ActionNeeded()
#     AnalizeOrders()
#
#
# def AnalizeOrders():
#     for i in range(PositionsTotal() - 1, -1, -1):
#         t = PositionGetTicket(i)
#         AnalizeOrder(t)
#     return True
#
# def AnalizeOrder(ticket):
#     if not PositionSelectByTicket(ticket):
#         Print("Eroare la selectarea poziției cu ticket-ul ", ticket)
#         return False
#     profit = pos.Profit()
#     priceOpen = pos.PriceOpen()
#     current = SymbolInfoDouble("_Symbol", "SYMBOL_ASK")
#     difference = (current - priceOpen) * 10000
#     if difference > 50 or profit < -100:
#         ClosePosition(ticket)
#     return True
#
# def ActionNeeded():
#     if not RecentPositions():
#         ask = SymbolInfoDouble("_Symbol", "SYMBOL_ASK")
#         bid = SymbolInfoDouble("_Symbol", "SYMBOL_BID")
#         rsiValue = iRSI("_Symbol", 0, 10, "PRICE_CLOSE")
#         if rsiValue > 70:
#             if ExtTrade_PositionOpen("_Symbol", "ORDER_TYPE_SELL", defaultvolume, bid, 0, 0):
#                 Print("Pozitie de BUY deschisa cu succes")
#         elif rsiValue < 30:
#             if ExtTrade_PositionOpen("_Symbol", "ORDER_TYPE_BUY", defaultvolume, ask, 0, 0):
#                 Print("Pozitie de BUY deschisa cu succes")
#         else:
#             return False
#         return False
#     return True
#
# def PossitionsOpen():
#     return PositionsTotal()
#
# def RecentPositions():
#     currentTime = TimeCurrent()
#     halfHourAgo = currentTime - (PeriodSeconds("PERIOD_H1") / 12)
#     if PositionsTotal() > maxPositions:
#         return True
#     for i in range(PositionsTotal() - 1, -1, -1):
#         t = PositionGetTicket(i)
#         PositionSelectByTicket(t)
#         openPos = PositionGetInteger("POSITION_TIME")
#         if openPos >= halfHourAgo:
#             return True
#     return False
#
# def ClosePosition(ticket):
#     if ExtTrade_PositionClose(ticket, deviation):
#         return True
#     else:
#         Print("A apărut o eroare la închiderea poziției cu ticketul ", ticket, ". Codul de eroare: ", GetLastError())
#         return False
#
