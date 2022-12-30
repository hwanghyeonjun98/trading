setlocal enabledelayedexpansion

call d:
call C:\ProgramData\Anaconda3\Scripts\activate.bat
call taskkill /im CpStart.exe
call conda activate py39_32
call cd D:\systrader-dev\trading
call python final_login.py
call cd D:\systrader-dev\trading
call python final_ds.py
call conda deactivate
call taskkill /im CpStart.exe
cmd /k