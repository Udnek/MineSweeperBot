import modules.Screen as sc
import time
import random as rd

colorNoInf = (255,255,255)
colorNull = (189,189,189)
colorFlag = (1,1,1)
color1 = (0,0,255)
color2 = (0, 123, 0)
color3 = (255,0,0)
color4 = (0,0,128)
color5 = (128,0,0)
color6 = (16, 133, 133)
color7 = (0,0,0)
color8 = (133, 133, 133)

black = (0,0,0)

colorDiff = 30

fUpLeftX = 514 #514 #705
fUpLeftY = 341 #341 #341
fSizeX = 40
fSizeY = 20
cellSize = 30

checkSmile = (1113, 291)
checkGlasses = (1113, 284)

saveScreens = False
screensFolder = './screenshots/'

timeBeforeStart = 1
timeBetweenSteps = 2


def flag(a, y, x):
    for i in range(x):
        for j in range(y):

            if a[i][j] == "f":

                for p in range(i - 1, i + 2):
                    for o in range(j - 1, j + 2):

                        if (-1 < p < x) and (-1 < o < y):
                            if not a[p][o] == "f":
                                if not a[p][o] == "n":
                                    if a[p][o] > 0:
                                        a[p][o] = a[p][o] - 1
    return a

def freeCells(a, k, l, x, y):
    result = []
    for i in range(k - 1, k + 2):
        for j in range(l - 1, l + 2):
            if (-1 < i < y) and (-1 < j < x):
                if not ((i == k) and (j == l)):
                    #if not (m[i][j] == -1):
                    if a[i][j] == "n":
                        result.append([i, j])

    return result

def chanceCount(a, chance, x, y):
    for r in range(x):
        for c in range(y):
            if not a[r][c] == "n" and not a[r][c] == -1 and not a[r][c] == "f":
                result = freeCells(a, r, c, fSizeX, fSizeY)
                for g in result:
                    if int(a[r][c]/len(result)*100) >= 100:
                        chance[g[0]][g[1]] = 1000
                    else:
                        chance[g[0]][g[1]] += int(a[r][c]/len(result)*100)

    return chance

def noChanceCount(a, chance, x, y):
    for r in range(y):
        for c in range(x):
            if a[r][c] == 0:
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if (-1 < i < y) and (-1 < j < x):
                            if not ((i == r) and (j == c)):
                                if a[i][j] == "n":
                                    chance[i][j] = -1

    return chance

def outputArray(a):
    for i in a:
        for j in i:
            if j == "n":
                print(".", end=" ")
            elif j == -1:
                print("*", end=" ")
            else:
                print(j, end=" ")
        print()

def decision(a, x, y):

    for i in range(y): ##NO BOMB
        for j in range(x):
            if a[i][j] == -1:
                return [i, j], "left"

    maxChance = 0
    maxChanceXY = [0,0]
    for i in range(y):  ##NO BOMB
        for j in range(x):
            if maxChance < a[i][j]:
                maxChance = a[i][j]
                maxChanceXY = [i,j]

    if maxChance < 100:
        return [rd.randint(0, y), rd.randint(0, x)], "left"

    return maxChanceXY, "right"

###########################################################
#step = 1

time.sleep(timeBeforeStart)
step = 0

def Game(id):
    #time.sleep(timeBeforeStart)
    step = 0
    result = ""
    clickType = "left"
    while True:
        game = sc.checkWin(black, black, colorDiff, screensFolder, checkSmile[0],
                           checkSmile[1], checkGlasses[0], checkGlasses[1]) #855 #291 #284
        if game == "win":
            #print("WIN")
            result = "w"
            sc.screenshot(id+"w", True, screensFolder, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize)
            break
        elif game == "lose":
            #print("LOSE")
            result = "l"
            sc.screenshot(id+"l", True, screensFolder, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize)
            if step < 5:
                result = "rl"
            break
        else:
            #if clickType == "left":
            #    f = sc.getField(colorNoInf, colorNull, colorFlag, color1, color2, color3, color4, color5, color6,
            #                 color7, color8, colorDiff, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize, saveScreens,
            #                 screensFolder, step)
            #else:
            #    f[coordsStep[0]][coordsStep[1]] = "f"

            f = sc.getField(colorNoInf, colorNull, colorFlag, color1, color2, color3, color4, color5, color6,
                                             color7, color8, colorDiff, fUpLeftX, fUpLeftY, fSizeX, fSizeY, cellSize, saveScreens,
                                             screensFolder, step)

            step+=1
            chance = [[0] * fSizeX for i in range(fSizeY)]
            f = flag(f, fSizeX, fSizeY)
            chance = chanceCount(f, chance, fSizeY, fSizeX)
            chance = noChanceCount(f, chance, fSizeX, fSizeY)
            coordsStep, clickType = decision(chance, fSizeX, fSizeY)
            sc.click(coordsStep[1] * cellSize + fUpLeftX, coordsStep[0] * cellSize + fUpLeftY, clickType)

            #outputArray(f)
            #print()
            #outputArray(chance)
            #print()
            #outputArray(chance)
            #time.sleep(timeBetweenSteps)

    return result

games = []
gamescount = 100

time.sleep(timeBeforeStart)
for g in range(gamescount):
    sc.click(checkSmile[0], checkSmile[1], "left")
    games.append(Game(str(g)+ "game"))
    print("win:",games.count("w"), "lose:", games.count("l"), "%win:",
          int(100/(g+1)*(games.count("w") - games.count("rl"))), "rand lose:", games.count("rl"))

print(games)
print(100/gamescount*games.count("w"))