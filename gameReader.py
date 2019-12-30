import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32gui
import win32con
from Equip import Equip
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

def updateEquipValues(text, eqp, statName, isPotential):
    if isPotential:
        if '%' in text:
            val = text[text.find('+') + 1:text.find('%')]
            val = float(int(val) * 0.01)
        else:
            val = int(text[text.find('+') + 1:])
        curr = eqp.mpot.get(statName)
        if type(curr) is list:
            eqp.mpot.get(statName).append(val)
        elif curr is None:
            eqp.mpot.update({statName : val})
        else:
            arr = [curr, val]
            eqp.mpot.update({statName : arr})
    elif '(' in text:
        #Has a base AND flame/star value
        substring = text
        if text.count('+') == 3:
            substring = text[:text.rfind('+')]
        eqp.base.update({statName : text[text.find('(') + 1:substring.rfind('+')]})
    else:
        val = text[text.find('+') + 1:]
        if '%' in val:
            val = val[:val.find('%')]
        eqp.base.update({statName : int(val)})

def parseEquip(ocrString):
    partition = ocrString.split('\n')
    idx = 0
    name = partition[idx]
    while('*' in name):
        name = partition[idx]
        idx += 1
    name = name.replace('•', '')
    # print(ocrString)

    eqp = Equip()
    eqp.name = name

    isPotential = False
    for word in partition[idx:]:
        if 'Type' in word:
            eqp.eqpType = word
        elif 'Potential' in word:
            isPotential = True
        elif 'STR' in word and 'REQ' not in word and 'REO' not in word:
            updateEquipValues(word, eqp, 'STR', isPotential)
        elif 'DEX' in word and 'REQ' not in word and 'REO' not in word:
            updateEquipValues(word, eqp, 'DEX', isPotential)
        elif ('INT' in word or 'NT' in word or '\'NT' in word or 'lNT' in word) and 'REQ' not in word and 'REO' not in word:
            updateEquipValues(word, eqp, 'INT', isPotential)
        elif 'LUK' in word and 'REQ' not in word and 'REO' not in word:
            updateEquipValues(word, eqp, 'LUK', isPotential)
        elif 'Power' in word or 'ATT' in word and 'INCREASE' not in word and ',' not in word and '/' not in word and 'M.' not in word:
            updateEquipValues(word, eqp, 'ATK', isPotential)
        elif 'Magic Attack' in word:
            updateEquipValues(word, eqp, 'MATK', isPotential)
        elif 'HP' in word:
            updateEquipValues(word, eqp, 'HP', isPotential)
        elif 'MP' in word:
            updateEquipValues(word, eqp, 'MP', isPotential)
        elif 'Defense' in word:
            updateEquipValues(word, eqp, 'DEF', isPotential)
        elif 'Speed' in word and 'Attack' not in word:
            updateEquipValues(word, eqp, 'SPEED', isPotential)
        elif 'Jump' in word:
            updateEquipValues(word, eqp, 'JUMP', isPotential)
        elif 'Critical Rate' in word:
            updateEquipValues(word, eqp, 'CRITRATE', isPotential)
        elif 'Critical Damage' in word:
            updateEquipValues(word, eqp, 'CRITDMG', isPotential)
        elif 'Boss' in word:
            updateEquipValues(word, eqp, 'BOSSDMG', isPotential)
        elif 'Damage' in word and 'Boss' not in word:
            updateEquipValues(word, eqp, 'DMG', isPotential)
        elif 'Ignore' in word:
            updateEquipValues(word, eqp, 'IGNORE', isPotential)
        elif 'AI' in word or 'Al' in word or 'All' in word or 'AlI' in word or 'AIl' in word:
            updateEquipValues(word, eqp, 'ALL', isPotential)
    print(eqp.base)
    print(eqp.mpot)
    # for word in partition[idx:]:
    #     if 'Type' in word:
    #         print(word)
    #     elif 'LEV' in word:
    #         print(word)
    #     elif 'STR' in word and 'REQ' not in word and 'REO' not in word:
    #         print(word)
    #     elif 'DEX' in word and 'REQ' not in word and 'REO' not in word:
    #         print(word)
    #     elif ('INT' in word or 'NT' in word or '\'NT' in word or 'lNT' in word) and 'REQ' not in word and 'REO' not in word:
    #         print(word)
    #     elif 'LUK' in word and 'REQ' not in word and 'REO' not in word:
    #         print(word)
    #     elif 'Attack Power' in word:
    #         print(word)
    #     elif 'Magic' in word:
    #         print(word)
    #     elif 'Defense' in word:
    #         print(word)
    #     elif 'Speed' in word:
    #         print(word)
    #     elif 'Jump' in word:
    #         print(word)
    #     elif 'AI' in word or 'Al' in word or 'All' in word or 'AlI' in word or 'AIl' in word:
    #         print(word)


def screen_record():
    client = vision.ImageAnnotatorClient()
    i = 0
    lastCursorPos = win32gui.GetCursorInfo()[2]
    while(i < 2):
        cursorPos = win32gui.GetCursorInfo()[2]
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
        if(pdd[2] == True and (lastCursorPos[0] + 20  < cursorPos[0] or cursorPos[0] < lastCursorPos[0] - 20 
                            or lastCursorPos[1] + 20 < cursorPos[1] or cursorPos[1] < lastCursorPos[1] - 20)):
            pddCoords = (loc[0] + pdd[0][0], loc[1] + pdd[0][1], loc[0] + pdd[1][0], loc[1] + pdd[1][1])
            reducedSearchCoords = (pddCoords[0] - 20, loc[1], pddCoords[0] + 260, loc[3])
            reducedSearchImg = ImageGrab.grab(reducedSearchCoords)
            reducedSearchWindow = np.array(reducedSearchImg)
            top = findTop(reducedSearchWindow)
            bot = findBottom(reducedSearchWindow)
            equipCoords = (reducedSearchCoords[0] + top[0], reducedSearchCoords[1] + top[1], reducedSearchCoords[0] + bot[0], reducedSearchCoords[1] + bot[1])
            equipImg = ImageGrab.grab(bbox=equipCoords)
            # print(equipImg)
            if(equipImg.width > 0 and equipImg.height > 0):
                equipWindow = np.array(equipImg)
                color = cv2.cvtColor(equipWindow, cv2.COLOR_BGR2RGB)
                # cv2.imshow('window',color)
                cv2.imwrite('./temp-vision-files/found.png', color)

                iconCoords = (pddCoords[0], pddCoords[1] - 83, pddCoords[0] + 80, pddCoords[1] - 3)
                icon = ImageGrab.grab(iconCoords)
                iconImg = np.array(icon)
                colorIcon = cv2.cvtColor(iconImg, cv2.COLOR_BGR2RGB)
                cv2.imwrite('./temp-vision-files/itemIcon.png', colorIcon)

                read_file = os.path.abspath('./temp-vision-files/found.png')
                with io.open(read_file, 'rb') as image_file:
                    content = image_file.read()
                image = types.Image(content=content)
                response = client.text_detection(image=image)
                texts = response.text_annotations
                # print(texts[0].description)
                parseEquip(texts[0].description)
                # for text in texts:
                    # print(text)
                cv2.destroyAllWindows()
                i += 1
                lastCursorPos = cursorPos
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

