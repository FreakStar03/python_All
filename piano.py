from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1.2)

# pyautogui.displayMousePosition()

#X: 1071 Y:  450 RGB: ( 90,  92, 118)
#X: 1155 Y:  450 RGB: (  0,   0,   0)
#X: 1243 Y:  450 RGB: ( 85,  87, 117)
#X: 1328 Y:  450 RGB: ( 78,  81, 115)

def click(x, y):
	win32api.SetCursorPos((x, y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#16 20 19 lightgrey
#54 159 198 lightblue


while  keyboard.is_pressed('q') == False:


	if pyautogui.pixel(1071,370)[54, 159, 198] == [54, 159, 198]:
		click(1071,370)
	if pyautogui.pixel(1071,370)[0] == 0:
		click(1071, 370)
	elif pyatogui.pixel(1071,370)[16, 20, 19] == [16, 20, 19]:
		click(1071, 370)

	if pyautogui.pixel(1155,400)[0] == 0:
		click(1155, 400)
	elif pyatogui.pixel(1155, 400)[16, 20, 19] == [16, 20, 19]:
		click(1155, 400)

	if pyautogui.pixel(1243,400)[0] == 0:
		click(1243, 400)
	elif pyatogui.pixel(1243, 400)[16, 20, 19] == [16, 20, 19]:
		click(1243, 400)

	if pyautogui.pixel(1328,370)[0] == 0:
		click(1328, 370)
	elif pyatogui.pixel(1328, 370)[16, 20, 19] == [16, 20, 19]:
		click(1328, 370)

	