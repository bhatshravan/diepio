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
red_team = np.array([121, 172, 241], dtype=np.uint8) #Red Players --- RGB-241,78,84
blue_team = np.array([24, 255, 225], dtype=np.uint8) #Blue players --- RGB-0,178,225

OFFSET=60
MOUSE_OFFSET_X=0
MOUSE_OFFSET_Y=0
Asplit=3
SLEEP_TIME=1
pyautogui.click(100,100)
FIND_FOOD_LIMIT=4
enemy=red_team
PANIC_MODE=False
TIME_MOVE=0.1

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
CENTER_X=BROWSER_SCREEN_WIDTH/2 #776/2 or 388
CENTER_Y=BRWOSER_SCREEN_HEIGHT/2 #410 or 392




#SOME FUNCTION INITIALIZATIONS--------------------------------------------------------------
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    #print(pyautogui.pixel(pt.x, pt.y))
    return { "x": pt.x, "y": pt.y}
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
	

def moveQuad():
	if(quad==1):
		print("Moving up right")
		pyautogui.keyDown('right')
		pyautogui.keyDown('up')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('right')
		pyautogui.keyUp('up')
		press=0
		
	elif(quad==2):
		print("Moving up left")
		pyautogui.keyDown('left')
		pyautogui.keyDown('up')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('left')
		pyautogui.keyUp('up')
		press=0
		
	elif(quad==3):
		print("Moving down left")
		pyautogui.keyDown('left')
		pyautogui.keyDown('down')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('left')
		pyautogui.keyUp('down')
		press=0
		
	elif(quad==4):
		print("Moving down right")
		pyautogui.keyDown('right')
		pyautogui.keyDown('down')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('right')
		pyautogui.keyUp('down')
		press=0
		
	elif(quad==5):
		print("Moving up")
		pyautogui.keyDown('up')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('up')
		press=0
		
	elif(quad==6):
		print("Moving left")
		pyautogui.keyDown('left')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('left')
		press=0
		
	elif(quad==7):
		print("Moving down")
		pyautogui.keyDown('down')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('down')
		press=0
		
	else:
		print("Moving right")
		pyautogui.keyDown('right')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('right')
		press=0
	


	
	
#DETERMINE OUR CURRENT TEAM------------------------------------------------------------------

im = pyautogui.screenshot()
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((CENTER_X, CENTER_Y))
print(r, g, b)
if(r==0 and g==178 and b==225):
	team=0
	print("Blue Team")
else:
	team=1
	enemy=blue_team
	print("Red team")
	


if(screenWidth>1000):
	Asplit=4
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
		#cv2.imshow('mask',mask)
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
		xx=0
		yy=0
		Asplit2=Asplit
		try:
		
			#Extract food cordinate value
			firstps=coord[0].astype(int)
			print("Cordinates needed: {0}".format(firstps))
			data=str(firstps[0]).replace("[", "").replace("]", "")
			datalen=len(data)
			if(datalen<8):
				Asplit2=3
			data=replace_str_index(data,Asplit2,',')
			s3=data.split(",")
			s4=s3[0].replace(" ","")
			xx=int(s4)
			s4=s3[1].replace(" ","")
			yy=int(s4)
			
			
			#Print coordinates to terminal
			print("Cordinates we get: {0},{1}".format(xx,yy))
			pyautogui.moveTo(xx+MOUSE_OFFSET_X, yy+MOUSE_OFFSET_Y)
			pos = queryMousePosition()
			print("Mouse position moved: {0}".format(pos))
			#time.sleep(2)
			
			
			#Square is found
			not2=0
			
			global quad
			#Get last square found quadrant location
			if(yy<CENTER_Y and xx<CENTER_X+OFFSET and xx>CENTER_X-OFFSET):  #FOOD IS ABOVE
				quad=5
			elif(xx<CENTER_X and yy<CENTER_Y+OFFSET and yy>CENTER_Y-OFFSET): #FOOD IS LEFT
				quad=6
			elif(yy>CENTER_Y and xx<CENTER_X+OFFSET and xx>CENTER_X-OFFSET): #FOOD IS DOWN
				quad=7
			elif(xx>CENTER_X and yy<CENTER_Y+OFFSET and yy>CENTER_Y-OFFSET): #FOOD IS RIGHT
				quad=8
			elif(xx>CENTER_X and yy<CENTER_Y):								 #FOOD IS TOP RIGHT
				quad=1
			elif(xx<CENTER_X and yy<CENTER_Y):								 #FOOD IS TOP LEFY
				quad=2
			elif(xx<CENTER_X and yy>CENTER_Y):								 #FOOD IS DOWN LEFT
				quad=3
			else:								 							 #FOOD IS DOWN RIGHT
				quad=4
			print("Found in quadrant {0}".format(quad))
			
			
		except Exception as e: 
		
			#NO FOOD FOUND
			firstp="[[  0 0]]"
			not2=not2+1
				
			#Since no food is found,move to random location
			if(not2>FIND_FOOD_LIMIT):
				quad=random.randint(1, 8)
				not2=0
				
				
			#MOVE TO NEAREST FOOD QUADRANT
			"""
			if(quad==1):
				print("Moving up right")
				pyautogui.keyDown('right')
				pyautogui.keyDown('up')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('right')
				pyautogui.keyUp('up')
				press=0
				
			elif(quad==2):
				print("Moving up left")
				pyautogui.keyDown('left')
				pyautogui.keyDown('up')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('left')
				pyautogui.keyUp('up')
				press=0
				
			elif(quad==3):
				print("Moving down left")
				pyautogui.keyDown('left')
				pyautogui.keyDown('down')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('left')
				pyautogui.keyUp('down')
				press=0
				
			elif(quad==4):
				print("Moving down right")
				pyautogui.keyDown('right')
				pyautogui.keyDown('down')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('right')
				pyautogui.keyUp('down')
				press=0
				
			elif(quad==5):
				print("Moving up")
				pyautogui.keyDown('up')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('up')
				press=0
				
			elif(quad==6):
				print("Moving left")
				pyautogui.keyDown('left')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('left')
				press=0
				
			elif(quad==7):
				print("Moving down")
				pyautogui.keyDown('down')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('down')
				press=0
				
			else:
				print("Moving right")
				pyautogui.keyDown('right')
				time.sleep(SLEEP_TIME)
				pyautogui.keyUp('right')
				press=0
			"""
			moveQuad()

			
			
if __name__ == '__main__':
	Thread(target = getBox).start()
	Thread(target = Calcpos).start()
	cv2.destroyAllWindows()