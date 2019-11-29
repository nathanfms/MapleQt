from PIL import Image

height = 1080
width = 1920

def borderCheck(firstPix, secondPix):
    tolerance = 10
    val = 235
    if(firstPix[0] <= val + tolerance and firstPix[0] >= val - tolerance and
    firstPix[1] <= val + tolerance and firstPix[1] >= val - tolerance and
    firstPix[2] <= val + tolerance and firstPix[2] >= val - tolerance and
    secondPix[0] <= val + tolerance and secondPix[0] >= val - tolerance and
    secondPix[1] <= val + tolerance and secondPix[1] >= val - tolerance and
    secondPix[2] <= val + tolerance and secondPix[2] >= val - tolerance):
        return True
    return False

def findTop(pixList, num):
    tolerance = 20
    val = 230
    while(num >= 0):
        counter = 0
        pix = pixList[num]
        while(pix[0] <= val + tolerance and pix[0] >= val - tolerance and
        pix[1] <= val + tolerance and pix[1] >= val - tolerance and 
        pix[2] <= val + tolerance and pix[2] >= val - tolerance):
            counter += 1
            if(counter >= 5):
                return num
        num -= width
    return 0

def findBottom(pixList, num):
    tolerance = 10
    val = 235
    while(num <= len(pixList)):
        counter = 0
        pix = pixList[num]
        while(pix[0] <= val + tolerance and pix[0] >= val - tolerance and
        pix[1] <= val + tolerance and pix[1] >= val - tolerance and 
        pix[2] <= val + tolerance and pix[2] >= val - tolerance):
            counter += 1
            if(counter >= 5):
                return num
        num += width
    return 0




im = Image.open('test2.png', 'r')
pix_val = list(im.getdata())


row = 0
for num, pix in enumerate(pix_val):
    if(num % width == 0):
        row += 1
    if (num % width) <= width - 260:        #1920 * 1080 resolution. 1660 + 259 = 1919 (259 = equip window width)
        nextPix = pix_val[num + 258]
        if(borderCheck(pix, nextPix)):
            counter = 1
            while(borderCheck(pix_val[num + (width * counter)], pix_val[num + 258 + (width * counter)])):
                counter += 1
            if(counter >= 10):
                # print("row: ", row, " col: ", num % width, "pix: ", pix, " nextPix: ", nextPix, " counter: ", counter)
                break


midPix = pix_val[num + 129]
counter = 0


left = num % width
right = (num % width) + 259
top = findTop(pix_val, num + 129) / width
bottom = findBottom(pix_val, num + 129) / width + 1 

im1 = im.crop((left, top, right, bottom))
im1.show()
            



        