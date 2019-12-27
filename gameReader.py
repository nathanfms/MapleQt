import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32gui
import win32con

import io
import os
from google.cloud import vision
from google.cloud.vision import types

def findTop(img):
    template = cv2.imread('assets/top.png', 0)
    w, h = template.shape[::-1]
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left

def findBottom(img):
    template = cv2.imread('assets/bot.png', 0)
    w, h = template.shape[::-1]
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return bottom_right

def findPdd(img):
    template = cv2.imread('assets/pdd.png', 0)
    w, h = template.shape[::-1]
    img2 = img.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    loc = np.where(res >= 0.8)
    found = False
    if np.array(loc).shape[1] > 0:
        found = True

    
    return (top_left, bottom_right, found)

def screen_record():
    client = vision.ImageAnnotatorClient()
    i = 0
    while(True):
        # printscreen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        winder = win32gui.FindWindow(None, "Maplestory")
        win32gui.SetWindowPos(winder, win32con.HWND_NOTOPMOST, 0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        loc = win32gui.GetWindowPlacement(winder)[-1]
        fullImg = ImageGrab.grab(loc)
        # print(fullImg)
        fullWindow = np.array(fullImg)
        # top = findTop(fullWindow)
        # bot = findBottom(fullWindow)

        pdd = findPdd(fullWindow)
        
        if(pdd[2] == True):
            pddCoords = (loc[0] + pdd[0][0], loc[1] + pdd[0][1], loc[0] + pdd[1][0], loc[1] + pdd[1][1])
            reducedSearchCoords = (pddCoords[0] - 20, loc[1], pddCoords[0] + 260, loc[3])
            reducedSearchImg = ImageGrab.grab(reducedSearchCoords)
            reducedSearchWindow = np.array(reducedSearchImg)
            top = findTop(reducedSearchWindow)
            bot = findBottom(reducedSearchWindow)
            equipCoords = (reducedSearchCoords[0] + top[0], reducedSearchCoords[1] + top[1], reducedSearchCoords[0] + bot[0], reducedSearchCoords[1] + bot[1])
            equipImg = ImageGrab.grab(bbox=equipCoords)
            print(equipImg)
            if(equipImg.width > 0 and equipImg.height > 0):
                equipWindow = np.array(equipImg)
                color = cv2.cvtColor(equipWindow, cv2.COLOR_BGR2RGB)
                # cv2.imshow('window',color)
                cv2.imwrite('found.png', color)

                read_file = os.path.abspath('found.png')
                with io.open(read_file, 'rb') as image_file:
                    content = image_file.read()
                image = types.Image(content=content)
                response = client.text_detection(image=image)
                texts = response.text_annotations
                print(texts[0].description)
                # for text in texts:
                #     print(text.description)
                cv2.destroyAllWindows()
                break
            # cv2.imshow('window',cv2.cvtColor(reducedSearchWindow, cv2.COLOR_BGR2RGB))
        # pddImg = ImageGrab.grab(bbox=pddCoords)
        # pddWindow = np.array(pddImg)

        #loc.x + top.x, loc.y + top.y, bot.x - top.x, bot.y - top.y
        # equipCoords = (loc[0] + top[0], loc[1] + top[1], loc[0] + bot[0], loc[1] + bot[1])
        # equipImg = ImageGrab.grab(bbox=equipCoords)
        # equipWindow = np.array(equipImg)
        # cv2.imshow('window',cv2.cvtColor(fullWindow, cv2.COLOR_BGR2RGB))
        # if(equipImg.width == 261):
        #     cv2.imshow('window',cv2.cvtColor(equipWindow, cv2.COLOR_BGR2RGB))
            
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # print(i, pdd[2])
        # i += 1


# winder = win32gui.FindWindow(None, "MapleStory")

# #x, y, x+w, y+h
# loc = win32gui.GetWindowPlacement(winder)[-1]
# print(loc)

# image = np.array(ImageGrab.grab(loc))
# cv2.imshow('window',cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# cv2.waitKey(0)

screen_record()

