setlocal enabledelayedexpansion

call d:
call C:\ProgramData\Anaconda3\Scripts\activate.bat

call conda activate tf2
call cd D:\systrader-dev\trading
call python final_tf.py
cmd /k