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
quad=0

not3=0
press=0

global runningg
runningg=True

team=0 #Team= 0 if blue team otherwise red team is 1
triangle = np.array([120, 136, 252], dtype=np.uint8) #Triangles --- RGB=252,118,119
squares = np.array([95, 150, 255], dtype=np.uint8) #Squares --- RGB=255,232,105
polygon = np.array([5, 136, 252], dtype=np.uint8) #Polygons --- RGB-118 141 252
red_team = np.array([121, 172, 241], dtype=np.uint8) #Red Players --- RGB-241,78,84
blue_team = np.array([24, 255, 225], dtype=np.uint8) #Blue players --- RGB-0,178,225
patrol = np.array([145, 129, 241], dtype=np.uint8) #RGB-241 119 221

OFFSET=60
Asplit=3
SLEEP_TIME=1
pyautogui.click(100,100)
FIND_FOOD_LIMIT=4

global coorden

global enemy
enemy=red_team

global PANIC_MODE
PANIC_MODE=False

global TIME_MOVE
TIME_MOVE=0.1

global TEST_MODE
TEST_MODE=False

#USER PLEASE GIVE ALL INITIALIZATIONS HERE-------------------------------------------------


#NO TEST VALUES
BROWSER_SCREEN_WIDTH=screenWidth #800
BRWOSER_SCREEN_HEIGHT=screenHeight #720
OFFSETX=28
OFFSETY=0
CENTER_X=(BROWSER_SCREEN_WIDTH/2)-(OFFSETX/2) #776/2 or 388
CENTER_Y=(BRWOSER_SCREEN_HEIGHT/2)-(OFFSETY/2) #410 or 392


#TEST VALUES
if(TEST_MODE==True):
	BROWSER_SCREEN_WIDTH=800 #800
	BRWOSER_SCREEN_HEIGHT=650#720
	OFFSETX=0
	OFFSETY=0
	CENTER_X=776/2
	CENTER_Y=410



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
	global enemy
	global runningg
	global coorden
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
		
		#FIND CORDINATES OF ALL FOOD AND ENEMIES
		global coord
		coord=cv2.findNonZero(mask)
		
		patrolMask = cv2.inRange(hsv, patrol, patrol) 
		panicmask=cv2.inRange(hsv, enemy, enemy) 
		
		fmask2 = cv2.add(patrolMask,panicmask)
		coorden=cv2.findNonZero(fmask2)
		
		
		#SHOW OUTPUT,UNCOMMENT THIS TO ENABLE IT
		if(TEST_MODE==True):
			cv2.imshow('mask',panicmask)
		
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			runningg=False
			break
			
def Calcpos():
	global quad
	not2=0
	global TIME_MOVE
	global PANIC_MODE
	
	while(runningg):
		print("\n-------\n")
		next=0
		next2=0
		xx=0
		yy=0
		Asplit2=Asplit
		try:
		
			try:
				firstps=coorden[0].astype(int)
				PANIC_MODE=True
				print("PANIC MODE!! RUNNING AWAY FROM ENEMY")
					
			except Exception as EE:
				firstps=coord[0].astype(int)
				PANIC_MODE=False
				
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
			pyautogui.moveTo(xx+OFFSETX, yy+OFFSETY)
			pos = queryMousePosition()
			print("Mouse position moved: {0}".format(pos))
			#time.sleep(2)
			
			
			#Square is found
			not2=0
			
			global quad
			#Get last square found quadrant location
			if(PANIC_MODE):
				if(yy<CENTER_Y and xx<CENTER_X+OFFSET and xx>CENTER_X-OFFSET):  #ENEMY IS ABOVE
					quad=7
				elif(xx<CENTER_X and yy<CENTER_Y+OFFSET and yy>CENTER_Y-OFFSET): #ENEMY IS LEFT
					quad=8
				elif(yy>CENTER_Y and xx<CENTER_X+OFFSET and xx>CENTER_X-OFFSET): #ENEMY IS DOWN
					quad=5
				elif(xx>CENTER_X and yy<CENTER_Y+OFFSET and yy>CENTER_Y-OFFSET): #ENEMY IS RIGHT
					quad=6
				elif(xx>CENTER_X and yy<CENTER_Y):								 #ENEMY IS TOP RIGHT
					quad=8
				elif(xx<CENTER_X and yy<CENTER_Y):								 #ENEMY IS TOP LEFY
					quad=6
				elif(xx<CENTER_X and yy>CENTER_Y):								 #ENEMY IS DOWN LEFT
					quad=6
				else:								 							 #ENEMY IS DOWN RIGHT
					quad=8
					
			else:
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
			
			
			if(PANIC_MODE==True):
				TIME_MOVE=1
				moveQuad()
			else:
				TIME_MOVE=0.2
				Thread(target = moveQuad).start()
				
				
		except Exception as e: 
		
			#NO FOOD FOUND
			firstp="[[  0 0]]"
			not2=not2+1
				
			#Since no food is found,move to random location
			if(not2>FIND_FOOD_LIMIT):
				if(PANIC_MODE==False):
					quad=random.randint(1, 8)
					TIME_MOVE=1
				else:
					TIME_MOVE=0.5
				not2=0
			
				
			#MOVE TO NEAREST FOOD QUADRANT
			
			moveQuad()
			
			
if __name__ == '__main__':
	Thread(target = getBox).start()
	Thread(target = Calcpos).start()
	cv2.destroyAllWindows()