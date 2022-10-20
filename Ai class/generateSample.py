from random import seed
from random import randint
sd = int(input("Input random number: "))
fileName = input("Name this file: ")
xSize = input("X-axis size: ")
ySize = input("Y-axis size: ")
start = input("Start coordinate: ")
goal = input("Goal coordinate: ")

seed(sd)

f = open(fileName+".txt", "w+")
f.write(start+'\n')
f.write(goal+'\n')
f.write(xSize + ' ' + ySize + '\n')
for i in range(1, int(xSize)+1):
    for j in range(1, int(ySize)+1):
        filled = randint(0, 9)
        if filled != 1:
            filled = 0
        f.write(str(i) + ' ' + str(j) + ' ' + str(filled) + '\n')

