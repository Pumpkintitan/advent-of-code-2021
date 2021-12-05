import numpy as np
file = open("day5.txt").read().split("\n")

class Board:
    def __init__(self):
        self.bi = [np.zeros(1000) for x in range(1000)]
    
    def addline(self, x1, y1, x2, y2):
        if x1 == x2:
            my = min(y1, y2)
            mmy = max(y1, y2)
            for i in range(mmy - my + 1):
                self.bi[my + i][x1] += 1
        elif y1 == y2:
            mx = min(x1, x2)
            mmx = max(x1, x2)
            for i in range(mmx - mx + 1):
                self.bi[y1][mx + i] += 1
        else:
            cx = 1
            cy = 1
            if x1 > x2:
                cx = -1
            if y1 > y2:
                cy = -1
            for i in range(abs(x1 - x2) + 1):
                self.bi[y1 + (cy * i)][x1 + (cx * i)] += 1
    
    def checkdanger(self):
        tot = 0
        for i in range(len(self.bi)):
            for j in range(len(self.bi)):
                if self.bi[i][j] >= 2:
                    tot += 1
        return tot

    def pboard(self):
        for i in range(len(self.bi)):
            print(self.bi[i])

b = Board()
for line in file:
    line.replace(" ","")
    l = line.split("->")
    l1 = l[0].split(",")
    l2 = l[1].split(",")
    b.addline(int(l1[0]), int(l1[1]), int(l2[0]), int(l2[1]),)

b.pboard()
print(b.checkdanger())