file = open("day9.txt").read().split("\n")
lows = []
traveled = []

basins = {}


def traverse(i, j):
    min = 10
    dir = 0
    n = int(file[i][j])
    if i > 0 and int(file[i-1][j]) <= n and int(file[i-1][j]) < min:
        min = int(file[i-1][j])
        dir = 1
    if i < len(file) - 1 and int(file[i+1][j]) <= n and int(file[i+1][j]) < min:
        min = int(file[i+1][j])
        dir = 3
    if j > 0 and int(file[i][j-1]) <= n and int(file[i][j-1]) < min:
        min = int(file[i][j-1])
        dir = 4
    if j < len(file[i]) - 1 and int(file[i][j+1]) <= n and int(file[i][j+1]) < min:
        min = int(file[i][j+1])
        dir = 2
    traveled.append((i, j))
    if dir == 0:
        return (i, j)
    if dir == 1:
        return traverse(i-1, j)
    if dir == 2:
        return traverse(i, j+1)
    if dir == 3:
        return traverse(i+1, j)
    if dir == 4:
        return traverse(i, j-1)


for i in range(len(file)):
    for j in range(len(file[i])):
        t = traverse(i, j)
        if int(file[i][j]) != 9:
            if t not in basins:
                basins[t] = 1
            else:
                basins[t] += 1
        if t not in lows:
            lows.append(t)

tot = 0
for l in lows:
    tot += int(file[l[0]][l[1]]) + 1
print(tot)

b = sorted(basins.items(), key=lambda x: x[1], reverse=True)

totm = 1
for i in range(3):
    totm *= b[i][1]
print(totm)
