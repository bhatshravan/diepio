import sys
import numpy as np
import cv2
from ctypes import windll, Structure, c_long, byref
import pyautogui

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

"""
blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]  
 
color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
 
hue = hsv_color[0][0][0]
 
print("Lower bound is :"),
print("[" + str(hue-10) + ", 100, 100]\n")
 
print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")
"""

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
	
def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    print(pyautogui.pixel(pt.x, pt.y))
    return { "x": pt.x, "y": pt.y}

green = np.uint8([[[0,178,225 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

data=str(hsv_green).replace("[", "").replace("]", "")
#data[3]=','

print(data)
data=replace_str_index(data,3,',')
data=replace_str_index(data,7,',')
print(data)
s3=data.split(",")

s4=s3[0].replace(" ","")
xx=int(s4)
	
s4=s3[1].replace(" ","")
yy=int(s4)

s4=s3[2].replace(" ","")
zz=int(s4)

print("np.array([{0}, {1}, {2}], dtype=np.uint8) #RGB-{3}".format(xx,yy,zz,str(green).replace("[", "").replace("]", "")))

"""
xx=int(s4)			
s4=s3[1].replace(" ","")
yy=int(s4)
print(xx)


xx=int(s4)
	
s4=s3[1].replace(" ","")
yy=int(s4)

s4=s3[2].replace(" ","")
yy=int(s4)



s3=s2.split(" ")
s4=s3[0].replace(" ","")
print("np.array([{0}, {1}, {2}], dtype=np.uint8 #RGB-{4}".format(xx,yy,zz,str(green).replace("[", "").replace("]", "")))

"""