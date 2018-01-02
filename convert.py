import sys
import numpy as np
import cv2
from ctypes import windll, Structure, c_long, byref
import pyautogui

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

im = pyautogui.screenshot()
rgb_im = im.convert('RGB')

global r,g,b
global xx
global yy
def queryMousePosition():
    global r,g,b
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    print(pyautogui.pixel(pt.x, pt.y))
    r, g, b = rgb_im.getpixel((pt.x, pt.y))
    print(r, g, b)
    return { "x": pt.x, "y": pt.y}



queryMousePosition()
green = np.uint8([[[r,g,b ]]])
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


