import win32com.client

instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
instCpStockCode = win32com.client.Dispatch('CpUtil.CpStockCode')
instCpCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
instStockChart = win32com.client.Dispatch('CpSysDib.StockChart')