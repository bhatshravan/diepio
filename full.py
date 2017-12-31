#DEFINE AND IMPORT ALL THINGS-----------------------------------------------------------------
import threading
from threading import Thread
import win32api, win32con
import keyboard
import pyautogui
import time
import cv2
from PIL import Image
import cv2
import random
from PIL import ImageGrab
import numpy as np
from ctypes import windll, Structure, c_long, byref
 
 
#INITIALIZE SOME VALUES---------------------------------------------------------------------
screenWidth, screenHeight = pyautogui.size()
global quad
not3=0
press=0
runningg=True
team=0 #Team= 0 if blue team otherwise red team is 1
triangle = np.array([120, 136, 252], dtype=np.uint8) #Triangles --- RGB=252,118,119
squares = np.array([95, 150, 255], dtype=np.uint8) #Squares --- RGB=255,232,105
polygon = np.array([5, 136, 252], dtype=np.uint8) #Polygons --- RGB-118 141 252





#USER PLEASE GIVE ALL INITIALIZATIONS HERE-------------------------------------------------

"""
#TEST VALUES
BROWSER_SCREEN_WIDTH=800 #800
BRWOSER_SCREEN_HEIGHT=720 #720
OFFSETX=0
OFFSETY=0
CENTER_X=776/2
CENTER_Y=410

"""
#NO TEST VALUES
BROWSER_SCREEN_WIDTH=screenWidth #800
BRWOSER_SCREEN_HEIGHT=screenHeight #720
OFFSETX=0
OFFSETY=0
CENTER_X=682 #776/2 or 388
CENTER_Y=388 #410 or 392


OFFSET=60
xx=0
yy=0

#SOME FUNCTION INITIALIZATIONS--------------------------------------------------------------
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    #print(pyautogui.pixel(pt.x, pt.y))
    global xx
    xx=pt.x
    global yy
    yy=pt.y
    return { "x": pt.x, "y": pt.y}
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


	
	
#DETERMINE OUR CURRENT TEAM------------------------------------------------------------------

	
#PROGRAM---------------------------------------------------------------------------------------
def getBox():
	while(True):
	
		#GRAB SCREEN
		img2 = ImageGrab.grab(bbox=(OFFSETX,OFFSETY,BROWSER_SCREEN_WIDTH,BRWOSER_SCREEN_HEIGHT))
		img = np.array(img2)
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
				
		#GET MASKS
		mask1 = cv2.inRange(hsv, triangle, triangle)
		mask2 = cv2.inRange(hsv, squares, squares) 
		mask3 = cv2.inRange(hsv, polygon, polygon) 
		
		fmask1 = cv2.add(mask1,mask2)
		mask = cv2.add(fmask1,mask3)
		
		#SHOW OUTPUT,UNCOMMENT THIS TO ENABLE IT
		cv2.imshow('mask',mask)
		global coord
		#FIND CORDINATES OF ALL FOOD AND ENEMIES
		coord=cv2.findNonZero(mask)
		
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			runningg=False
			break
def Calcpos():
	quad=1
	not2=0
	while(runningg):
		print("\n-------\n")
		next=0
		next2=0
		try:
			time.sleep(1)
			
			pos=queryMousePosition()
			#Print coordinates to terminal
			print("Cordinates we get: {0},{1}".format(xx,yy))
			
			#Square is found
			not2=0
			
			
			#Get last square found quadrant location
			if(yy<CENTER_Y and xx<CENTER_X+OFFSET and xx>CENTER_X-OFFSET):
				quad=5
				
			elif(xx<CENTER_X and yy<CENTER_Y+OFFSET and yy>CENTER_Y-OFFSET):
				quad=6
				
			elif(yy>CENTER_Y and xx<CENTER_X+OFFSET and xx>CENTER_X-OFFSET):
				quad=7
				
			elif(xx>CENTER_X and yy<CENTER_Y+OFFSET and yy>CENTER_Y-OFFSET):
				quad=8
			
			elif(xx>CENTER_X and yy<CENTER_Y):
				quad=1
			elif(xx<CENTER_X and yy<CENTER_Y):
				quad=2
			elif(xx<CENTER_X and yy>CENTER_Y):
				quad=3
			else:
				quad=4
			print("Found in quadrant {0}".format(quad))
			
			
		except Exception as e: 
		
			#NO FOOD FOUND
			firstp="[[  0 0]]"
			not2=not2+1
				
			#Since no food is found,move to random location
			if(not2>3):
				quad=random.randint(1, 4)
				not2=0
				
	

if __name__ == '__main__':
	Thread(target = Calcpos).start()
	cv2.destroyAllWindows()