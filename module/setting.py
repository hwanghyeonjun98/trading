import win32com.client

instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
instCpCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
instStockChart = win32com.client.Dispatch('CpSysDib.StockChart')
instCpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
instCpTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")
instCpTd6033 = win32com.client.Dispatch("CpTrade.CpTd6033")
instCpTdNew5331A = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
instCpTd5339 = win32com.client.Dispatch('CpTrade.CpTd5339')