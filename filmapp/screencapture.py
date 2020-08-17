from PIL import Image
import PIL.ImageGrab as ss
import pytesseract
import subprocess
import keyboard
import pyperclip
import os
import re
# import cv2


def getKeyFromImage():
    regexPattern = "[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}"
    filename = f"C:\\Users\\{os.getlogin()}\\Pictures\\Screenshots\\d4565ddyt54s4s3.png"
    x, y = 1321, 853
    height, width = 100, 550
    screenshot = ss.grab()
    cropped = screenshot.crop((x, y, x+width, y+height))
    cropped.save(filename)
    # image = cv2.imread(filename)
    # graycol = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(filename, graycol)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

while True:
    try:
        if keyboard.is_pressed('q'):
            rawKey = getKeyFromImage()
            key = re.search("[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}", rawKey).group()
            print(key)
            pyperclip.copy(key)
        elif keyboard.is_pressed('w'):
            break
    except:
        break
