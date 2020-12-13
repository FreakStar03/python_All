#network automation-script

import os
import time
import pyautogui


os.system('xdg-open http://192.168.1.1/login.html')

time.sleep(5)

pyautogui.typewrite("admin")
pyautogui.press("enter")

while 1:
	if pyautogui.locateOnScreen('/mnt/0CF2710AF270F972/CodeByFreak/python/screenshot.png', region =(300,230,1000,1000)) != None:
		print("I can see it")
		time.sleep(0.5)
	else:
		print("I can't see you?")
		time.sleep(0.5)
