import cv2
import numpy as np 
from matplotlib import pyplot
import pytesseract

def findBottom(file):
    img = cv2.imread(file, 0)
    img2 = img.copy()
    template = cv2.imread('assets/bot.png', 0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = cv2.TM_CCOEFF
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return bottom_right

def findTop(file):
    img = cv2.imread(file, 0)
    img2 = img.copy()
    template = cv2.imread('assets/top.png', 0)
    w, h = template.shape[::-1]
    img = img2.copy()
    method = cv2.TM_CCOEFF
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left

def countStars():
    img_rgb = cv2.imread('test2.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

    template = cv2.imread('assets/star.png', 0)
    w, h = template.shape[::-1]
    
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.imwrite('res.png',img_rgb)

file = 'test-images/test2.png'

img = cv2.imread(file, 0)

cv2.rectangle(img, findTop(file), findBottom(file), 255, 2)

top = findTop(file)
bot = findBottom(file)

print(top)
print(bot)

x = top[0]
y = top[1]

w = bot[0] - top[0]
h = bot[1] - top[1]

cropped = img[y:y+h, x:x+w].copy()


cv2.imshow("cropped", cropped)
cv2.waitKey(0)

# countStars()