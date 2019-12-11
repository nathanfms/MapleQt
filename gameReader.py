import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32gui
import win32con

def findTop(img):
    template = cv2.imread('assets/top.png', 0)
    w, h = template.shape[::-1]
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left

def findBottom(img):
    template = cv2.imread('assets/bot.png', 0)
    w, h = template.shape[::-1]
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return bottom_right

def screen_record():
    while(True):
        # printscreen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        winder = win32gui.FindWindow(None, "MapleStory")
        win32gui.SetWindowPos(winder, win32con.HWND_NOTOPMOST, 0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        loc = win32gui.GetWindowPlacement(winder)[-1]
        fullImg = ImageGrab.grab(loc)
        # print(fullImg)
        fullWindow = np.array(fullImg)
        top = findTop(fullWindow)
        bot = findBottom(fullWindow)
        #loc.x + top.x, loc.y + top.y, bot.x - top.x, bot.y - top.y
        equipCoords = (loc[0] + top[0], loc[1] + top[1], loc[0] + bot[0], loc[1] + bot[1])
        equipImg = ImageGrab.grab(bbox=equipCoords)
        equipWindow = np.array(equipImg)
        # print(equipWindow)
        # print("Full: ", fullWindow, " | Equip: ", equipWindow, "DONE")
        # cv2.imshow('window',cv2.cvtColor(fullWindow, cv2.COLOR_BGR2RGB))
        # print(equipCoords)
        if(equipImg.getbbox() is not None):
            # equipWindow = np.array(ImageGrab.grab(equipCoords))
            # print(equipWindow)
            cv2.imshow('window',cv2.cvtColor(equipWindow, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# winder = win32gui.FindWindow(None, "MapleStory")

# #x, y, x+w, y+h
# loc = win32gui.GetWindowPlacement(winder)[-1]
# print(loc)

# image = np.array(ImageGrab.grab(loc))
# cv2.imshow('window',cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# cv2.waitKey(0)

screen_record()

