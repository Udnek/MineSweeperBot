import pyautogui
from PIL import Image
#import os
import numpy as np
#import time

#inf = [colorNoInf, colorNull, colorFlag, color1, color2, color3, color4, color5, color6, color7, color8,
#       colorDiff, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize, saveScreens, screensFolder, step]

def screenshot(name, save, screensFolder, x, y, sizeX, sizeY, cellSize):
    screen = pyautogui.screenshot(region=(x, y, sizeX * cellSize, sizeY * cellSize))
    name = screensFolder + str(name) + '.png'
    if save:
        screen.save(name)
    return screen

def eacArrays(a,b, colorDiff):
    for i in range(len(a)):
        if abs(a[i] - b[i]) > colorDiff:
            return False
    return True

def eacImg(a,b, size):
    for i in range(size):
        for j in range(size):
            for k in range(3):
                if a[i][j][k] != b[i][j][k]:
                    return False
    return True

def getField(colorNoInf, colorNull, colorFlag, color1, color2, color3, color4, color5, color6,
             color7, color8, colorDiff, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize, saveScreens,
             screensFolder, step):

    field = [["n" for i in range(fSizeX)] for j in range(fSizeY)]

    s = screenshot(step, saveScreens, screensFolder, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize)
    img = np.array(s)


    for i in range(fSizeY):
        for j in range(fSizeX):
            a = int(i*cellSize+cellSize/2)
            b = int(j*cellSize+cellSize/2)

            if eacArrays(img[i*cellSize][j*cellSize], colorNoInf, colorDiff):
                if eacArrays(img[a][b], colorNull, colorDiff):
                    field[i][j] = "n"
                else:
                    field[i][j] = "f"
            else:
                if eacArrays(img[a][b], color8, colorDiff):
                    field[i][j] = 8
                elif eacArrays(img[a][b], colorNull, colorDiff):
                    field[i][j] = -1
                elif eacArrays(img[a][b], color1, colorDiff):
                    field[i][j] = 1
                elif eacArrays(img[a][b], color2, colorDiff):
                    field[i][j] = 2
                elif eacArrays(img[a][b], color3, colorDiff):
                    field[i][j] = 3
                elif eacArrays(img[a][b], color4, colorDiff):
                    field[i][j] = 4
                elif eacArrays(img[a][b], color5, colorDiff):
                    field[i][j] = 5
                elif eacArrays(img[a][b], color6, colorDiff):
                    field[i][j] = 6
                elif eacArrays(img[a][b], color7, colorDiff):
                    field[i][j] = 7

    return field

def checkWin(colorWin, colorLose, colorDiff, screensFolder, x, y, x2, y2):
    sSmile = screenshot("Smile", False, screensFolder, x, y, 1, 1, 1)
    imgSmile = np.array(sSmile)
    sGlasses = screenshot("GLasses", False, screensFolder, x2, y2, 1, 1, 1)
    imgGlasses = np.array(sGlasses)
    if eacArrays(imgSmile[0][0], colorLose, colorDiff):
        return "lose"
    elif eacArrays(imgGlasses[0][0], colorWin, colorDiff):
        return "win"
    else:
        return "cont"

def click(x,y,type):
    pyautogui.click(x,y,button=type)

def loadImage():
    try:
        img = Image.open('cell.png')
        return img

    except FileNotFoundError:
        print("File not found")
        return False

#time.sleep(1)
#print("aboba", findCorner("", 50, 225))