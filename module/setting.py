import win32com.client

instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
instCpCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
instStockChart = win32com.client.Dispatch('CpSysDib.StockChart')
instCpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
instCPTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")