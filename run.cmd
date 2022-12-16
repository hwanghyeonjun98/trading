setlocal enabledelayedexpansion

call d:
call C:\ProgramData\Anaconda3\Scripts\activate.bat
call conda activate py39_32
call cd D:\systrader-dev\trading
call python final_ds.py
call conda deactivate
call conda activate tf2
call cd D:\systrader-dev\trading
call python final_tf.py
