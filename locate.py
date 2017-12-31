import win32api, win32con
import keyboard
import pyautogui
import time
import cv2
import numpy as np
from PIL import Image
import time
import cv2
import random
from PIL import ImageGrab
import numpy as np
 
#(118, 141, 252) 
#img = cv2.imread('circles.png', 1)
from ctypes import windll, Structure, c_long, byref
import pyautogui

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]




def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    #print(pyautogui.pixel(pt.x, pt.y))
    return { "x": pt.x, "y": pt.y}

quad=1

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(screenWidth,screenHeight)
not3=0
pyautogui.click(100,100)
press=0
while(True):
	print("\n-------\n")
	next=0
	next2=0
	not2=0
	xx=0
	yy=0
	img2 = ImageGrab.grab(bbox=(70,70,800,650))
	img = np.array(img2)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_range = np.array([90, 100, 100], dtype=np.uint8)
	upper_range = np.array([105, 255, 255], dtype=np.uint8)
	mask = cv2.inRange(hsv, lower_range, upper_range)
	cv2.imshow('mask',mask)
	#time.sleep(2)
	
	coord=cv2.findNonZero(mask)
	
	try:
		for lop in coord:
			firstp=lop
		firstps=firstp.astype(int)
		
		print("Cordinates needed: {0}".format(firstps))
		
		data=str(firstps[0]).replace("[", "").replace("]", "")
		#data[3]=','
		
		#n=len(data)
		s = list(data)
		s2="".join(s)
		s3=s2.split(" ")
		s4=s3[0].replace(" ","")
		xx=int(s4)
		
		s4=s3[1].replace(" ","")
		yy=int(s4)
		
		print("Cordinates we get: {0},{1}".format(xx,yy))
		pyautogui.moveTo(xx+75, yy+72)
		pos = queryMousePosition()
		print("Mouse position moved: {0}".format(pos))
		time.sleep(2)
		not2=0
		#CENTER-388,392
		if(xx>388 and yy<392):
			quad=1
		elif(xx<388 and yy<392):
			quad=2
		elif(xx<388 and yy>392):
			quad=3
		else:
			quad=4
		print("Found in quadrant {0}".format(quad))
		
		
	except:
		firstp="[[  0 0]]"
		not2=not2+1
		if(not2>3):
			quad=random.randint(1, 4)
		if(quad==1):
			print("Moving up right")
			pyautogui.keyDown('right')
			pyautogui.keyDown('up')
			time.sleep(3)
			pyautogui.keyUp('right')
			pyautogui.keyUp('up')
			press=0
			
		elif(quad==2):
			print("Moving up left")
			pyautogui.keyDown('left')
			pyautogui.keyDown('up')
			time.sleep(3)
			pyautogui.keyUp('left')
			pyautogui.keyUp('up')
			press=0
			
		elif(quad==3):
			print("Moving down left")
			pyautogui.keyDown('left')
			pyautogui.keyDown('down')
			time.sleep(3)
			pyautogui.keyUp('left')
			pyautogui.keyUp('down')
			press=0
			
		else:
			print("Moving down right")
			pyautogui.keyDown('right')
			pyautogui.keyDown('down')
			time.sleep(3)
			pyautogui.keyUp('right')
			pyautogui.keyUp('down')
			press=0
			time.sleep(3)
	
	
	#pyautogui.click(firstp)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
 
cv2.destroyAllWindows()