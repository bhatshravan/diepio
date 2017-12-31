from ctypes import windll, Structure, c_long, byref
import pyautogui
import threading
from threading import Thread
import win32api, win32con
import keyboard
import pyautogui
from PIL import Image
import cv2
from PIL import ImageGrab
import numpy as np


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

green = np.uint8([[[241,119,221 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
data=str(hsv_green).replace("[", "").replace("]", "")


data=replace_str_index(data,3,',')
data=replace_str_index(data,7,',')
s3=data.split(",")
s4=s3[0].replace(" ","")
xx=int(s4)
s4=s3[1].replace(" ","")
yy=int(s4)
s4=s3[2].replace(" ","")
zz=int(s4)


range =  np.array([xx, yy, zz], dtype=np.uint8)
#upper_range =  np.array([5, 236, 252], dtype=np.uint8)

triangle = np.array([120, 136, 252], dtype=np.uint8) #RGB=252,118,119
squares = np.array([95, 150, 255], dtype=np.uint8) #RGB=255,232,105
polygon = np.array([5, 136, 252], dtype=np.uint8) #RGB-118 141 252

im = pyautogui.screenshot()
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((776/2, 410))
print(r, g, b)

"""
if(r==0 and g==178 and b==225):
	lower_range = np.array([80, 100, 100], dtype=np.uint8)
	upper_range = np.array([255, 255, 255], dtype=np.uint8)
	print("Blue Team")
else:
	lower_range = np.array([90, 100, 100], dtype=np.uint8)
	upper_range = np.array([105, 255, 255], dtype=np.uint8)
	print("Red team")
"""
while(True):
		img2 = ImageGrab.grab(bbox=(70,70,800,720))
		img = np.array(img2)
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
		"""
		mask1 = cv2.inRange(hsv, triangle, triangle)
		mask2 = cv2.inRange(hsv, squares, squares) 
		mask3 = cv2.inRange(hsv, polygon, polygon) 
		
		fmask1 = cv2.add(mask1,mask2)
		mask = cv2.add(fmask1,mask3)
		"""
		mask = cv2.inRange(hsv, range, range) 
		
		cv2.imshow('mask',mask)
		
		global coord
		coord=cv2.findNonZero(mask)
		
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
			runningg=False
			break

#CENTER-388,392
#END-769,513

"""
im = pyautogui.screenshot()
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((776/2, 410))
print(r, g, b)
"""

#BY DEFAULT FIREFOX= X-776, Y-413
