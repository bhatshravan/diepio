import win32api, win32con
import keyboard
import pyautogui
import time

from PIL import Image
import time
import cv2


#FOr the while loop
running=1


#polygon=(118, 141, 252)	
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(screenWidth,screenHeight)
	
pyautogui.click(100,100)


press=0
while(running==1):
	buttonx=0
	buttony=0
	try:
		template = Image.open('images/polygon.png')
		buttonx, buttony = pyautogui.locateCenterOnScreen('images/polygon.png',grayscale=False)
		#pyautogui.click(buttonx, buttony)
		pyautogui.moveTo(buttonx, buttony)
		pyautogui.click(buttonx,buttony)
		print(buttonx,buttony)
	except:	
		print("No polygon found")
		try:
			template = Image.open('images/square.png')
			buttonx, buttony = pyautogui.locateCenterOnScreen(template,grayscale=False)
			#pyautogui.click(buttonx, buttony)
			pyautogui.moveTo(buttonx, buttony)
			pyautogui.click(buttonx,buttony)
			print(buttonx,buttony)
		except:
			print("No square found")
			if(press==1):
				print("Moving up")
				pyautogui.keyDown('up')
				time.sleep(2)
				pyautogui.keyUp('up')
				press=0
			else:
				print("Moving down")
				pyautogui.keyDown('down')
				time.sleep(2)
				pyautogui.keyUp('down')
				press=1
	time.sleep(2)
	print("Sleeping")
	
	"""
	pyautogui.moveTo(83, 425)
	pyautogui.click(83, 425)
	pyautogui.keyDown('down')
	print("Pointing down")
	time.sleep(1)
	pyautogui.keyUp('down')
	pyautogui.moveTo(715, 437)
	pyautogui.click(715,437)
	pyautogui.keyDown('up')
	time.sleep(1)
	print("Pointing up")
	pyautogui.keyUp('up')
	"""

	
	

#Click function//////DPEARCATED---------------------------------
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#--------------------------------------------------------------
#click(100,100)
