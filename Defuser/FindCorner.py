import modules.Screen as sc
import numpy as np
import time

startX = 479
startY = 203

def findCorner(screenFolder, startX, startY):
    s = sc.screenshot("fullscreen", True, screenFolder, 0, 0, 1920, 1080, 1)
    print("screnned!")
    fs = np.array(s)
    cell = sc.loadImage()
    if cell == False:
        raise NameError

    cella = np.array(cell)

    for i in range(startY, 1080-cell.size[0]):
        for j in range(startX, 1920-cell.size[0]):
            p = []
            for m in range(len(cella)):
                k = []
                for n in range(len(cella)):
                    k.append(fs[i+m][j+n])
                p.append(k)
            if sc.eacImg(cella, p, cell.size[0]):
                return j, i
    return False

time.sleep(1)
print(findCorner('./screenshots/', startX, startY))