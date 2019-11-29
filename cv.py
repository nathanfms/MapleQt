import cv2
import numpy as np 
from matplotlib import pyplot
import pytesseract

def findBottom():
    img = cv2.imread('test2.png', 0)
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

def findTop():
    img = cv2.imread('test2.png', 0)
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

img = cv2.imread('test2.png', 0)
# img2 = img.copy()
# templateTop = cv2.imread('assets/top.png', 0)
# templateBot = cv2.imread('assets/bot.png', 0)
# w, h = templateTop.shape[::-1]

# img = img2.copy()
# method = cv2.TM_CCOEFF

# res = cv2.matchTemplate(img, templateTop, method)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h + 200)

cv2.rectangle(img, findTop(), findBottom(), 255, 2)

# print(top_left)
# print(bottom_right)

# pyplot.subplot(121),pyplot.imshow(res, cmap='gray')
# pyplot.title('Matching Result'), pyplot.xticks([]), pyplot.yticks([])
# pyplot.subplot(122),pyplot.imshow(img,cmap='gray')
# pyplot.title('Detected Point'),pyplot.xticks([]),pyplot.yticks([])
# pyplot.suptitle(cv2.TM_CCOEFF)

# pyplot.show()

print(findTop())
print(findBottom())

top = findTop()
bot = findBottom()

x = top[0]
y = top[1]

w = bot[0] - top[0]
h = bot[1] - top[1]

cropped = img[y:y+h, x:x+w].copy()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(cropped, lang="Arial"))

cv2.imshow("cropped", cropped)
cv2.waitKey(0)

# countStars()