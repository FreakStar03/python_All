#ai
import pyautogui
from time import sleep

sleep(5)

t = open("text.txt",'r')

f = 0
while True:
	f = f + 1
	m = "Binod (text number = "+ (str(f)) +" )"
	k = "life is strange."

	count = (str(f))
	for letter in m:
		pyautogui.typewrite(letter)
	pyautogui.press("enter")


	# for sentence in t:
	# 	pyautogui.typewrite(sentence)	
	# 	pyautogui.press("enter")
