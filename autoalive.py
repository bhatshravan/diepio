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

iter=0
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
play_background = np.array([0, 0, 205], dtype=np.uint8) #Background --- RGB-205 205 205
border = np.array([0, 0, 185], dtype=np.uint8) #RGB-185 185 185

OFFSET=60
Asplit=3
SLEEP_TIME=1
pyautogui.click(300,300)
FIND_FOOD_LIMIT=4
FOOD_NEAR_OFFSET=200
NEAR_BORDER_LIMIT=30000


global coorden
global coordborder

global enemy
enemy=red_team

global PANIC_MODE
PANIC_MODE=False

global TIME_MOVE
TIME_MOVE=0.1

global TEST_MODE
TEST_MODE=False

global BORDER_FOUND
BORDER_FOUND=False
#USER PLEASE GIVE ALL INITIALIZATIONS HERE-------------------------------------------------


#NO TEST VALUES
BROWSER_SCREEN_WIDTH=screenWidth #800
BRWOSER_SCREEN_HEIGHT=screenHeight #720
OFFSETX=0
OFFSETY=0
CENTER_X=(BROWSER_SCREEN_WIDTH/2)-(OFFSETX/2) #776/2 or 388
CENTER_Y=(BRWOSER_SCREEN_HEIGHT/2)-(OFFSETY/2) #410 or 392


#TEST VALUES
if(TEST_MODE==True):
	BROWSER_SCREEN_WIDTH=800 #800
	BRWOSER_SCREEN_HEIGHT=650#720
	OFFSETX=0
	OFFSETY=0
	CENTER_X=367
	CENTER_Y=387

TARGET=(CENTER_X,CENTER_Y)

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
	quadpos=quad
	print("In moveQuad , quadrant is {0}".format(quadpos))
	if(quadpos==1):
		print("Moving up right")
		pyautogui.keyDown('right')
		pyautogui.keyDown('up')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('right')
		pyautogui.keyUp('up')
		press=0
		
	elif(quadpos==2):
		print("Moving up left")
		pyautogui.keyDown('left')
		pyautogui.keyDown('up')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('left')
		pyautogui.keyUp('up')
		press=0
		
	elif(quadpos==3):
		print("Moving down left")
		pyautogui.keyDown('left')
		pyautogui.keyDown('down')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('left')
		pyautogui.keyUp('down')
		press=0
		
	elif(quadpos==4):
		print("Moving down right")
		pyautogui.keyDown('right')
		pyautogui.keyDown('down')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('right')
		pyautogui.keyUp('down')
		press=0
		
	elif(quadpos==5):
		print("Moving up")
		pyautogui.keyDown('up')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('up')
		press=0
		
	elif(quadpos==6):
		print("Moving left")
		pyautogui.keyDown('left')
		time.sleep(TIME_MOVE)
		pyautogui.keyUp('left')
		press=0
		
	elif(quadpos==7):
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
	team=1
	enemy=blue_team
	print("Red Team")
else:
	team=0
	enemy=red_team
	print("Blue team")
enemy=red_team


if(screenWidth>1000):
	Asplit=4


def Calcpos():
	global quad
	LAST_FOOD_FOUND=0
	global TIME_MOVE
	global PANIC_MODE
	global iter
	global BORDER_FOUND
	
	while(runningg):
		print("\n-------\n")
		
		quad=random.randint(8, 20)
		
		pyautogui.moveTo(random.randint(CENTER_X, BROWSER_SCREEN_WIDTH-200),random.randint(100, BRWOSER_SCREEN_HEIGHT-100))
		
		if(quad>4):
			quad=5
		else:
			quad=7
		time.sleep(random.randint(1, 3))
		moveQuad()		
			
			
if __name__ == '__main__':
	Thread(target = Calcpos).start()
	cv2.destroyAllWindows()