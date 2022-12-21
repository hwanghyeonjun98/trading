@echo off
setlocal enabledelayedexpansion

call C:\Users\USER\Anaconda3\Scripts\activate.bat

@REM 삼성전자: 005930
@REM 현대차: 005380
@REM 카카오: 035720

# 20221208
1. python main.py --mode train --ver v3 --name 005930 --stock_code 005930 --rl_method a2c --net lstm --start_date 20211201 --end_date 20211231
2. python main.py --mode train --ver v3 --name 005930 --stock_code 005930 --rl_method a3c --net lstm --start_date 20210101 --end_date 20210131
3. python main.py --mode train --ver v3 --name 005930 --stock_code 005930 --rl_method a3c --net lstm --start_date 20210101 --end_date 20210131