from  pywinauto.application  import  Application 
import pyautogui
import time

time.sleep(15)
app  =  Application(backend = "uia").start('C:\CREON\STARTER\coStarter.exe')

# Notepad.exe 프로세스 내부의 창 설명 
dlg_spec = app.CREONstarter
# 창이 실제로 열릴 때까지 기다리십시오 
time.sleep(3)
pyautogui.moveTo(1025, 605)
pyautogui.click()
dlg_spec.wait('visible')

pyautogui.moveTo(950, 310)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(950, 650)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(870, 490)
pyautogui.click()
pyautogui.typewrite('1q2w3e4r', interval=0.1)
time.sleep(3)
pyautogui.moveTo(970, 605)
pyautogui.click()
time.sleep(30)
pyautogui.moveTo(975, 575)
pyautogui.click()
time.sleep(3)