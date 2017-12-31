from ctypes import windll, Structure, c_long, byref
import pyautogui

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]





screenWidth, screenHeight = pyautogui.size()
print("{0}, {1}".format(screenWidth,screenHeight))

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    print(pyautogui.pixel(pt.x, pt.y))
    return { "x": pt.x, "y": pt.y}


pos = queryMousePosition()
print(pos)

im = pyautogui.screenshot()

#pyautogui.moveTo(776/2, 411)

print("Pixel color:{0}".format(im.getpixel((776/2, 410))))




#CENTER-388,392
#END-769,513