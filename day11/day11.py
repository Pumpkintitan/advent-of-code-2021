file = open("day11.txt").read().split("\n")
board = []
for i in range(len(file)):
    t = []
    for j in range(len(file[i])):
        t.append(int(file[i][j]))
    board.append(t)
steps = 100

popped = []

def dothething(i,j):
    if board[i][j] > 9 and (i,j) not in popped:
        popped.append((i,j))
        lx = -1
        ly = -1
        mx = 1
        my = 1
        if i == 0:
            lx = 0
        if i == 9:
            mx = 0
        if j == 0:
            ly = 0
        if j == 9:
            my = 0
        for a in range(lx, mx + 1):
            for b in range(ly, my + 1):
                if not(a == 0 and b == 0):
                    board[i + a][j + b] += 1
        for a in range(lx, mx + 1):
            for b in range(ly, my + 1):
                if not(a == 0 and b == 0):
                    dothething(i+a, j+b)

def pboard():
    for l in board:
        print(l)

tot = 0

s = 0
while len(popped) < 100:
    popped = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            dothething(i,j)
    for cord in popped:
        board[cord[0]][cord[1]] = 0
    tot += len(popped)
    s += 1
    print(s)
print(tot)


        
