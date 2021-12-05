file = open("day4.txt").read().split("\n")
inputs = file[0]

class Board:
    def __init__(self, i):
        self.real = i.copy()
        self.nums = i.copy()
        self.won = False

    def checkwin(self, n):
        self.showboard(self.nums)
        no = 0
        for i in range(5):
            for j in range(5):
                if n != self.nums[i][j]:
                    no += (1/5)
                else:
                    self.real[i][j] = "X"
        if no == 5:
            return False
        
        #rows
        for i in range(5):
            print(self.real[i].count("X"))
            if self.real[i].count("X") == 5:
                self.rwin(n)
                return True
        
        #columns
        for i in range(5):
            col = 0
            for j in range(5):
                if self.real[j][i] == "X":
                    col += 1
            if col == 5:
                self.rwin(n)
                return True
        
        #diagonals
        d1 = 0
        d2 = 0
        for i in range(5):
            if self.real[i][i] == "X":
                d1 += 1
            if self.real[i][len(self.real[i]) - i - 1] == "X":
                d2 += 1
        if d1 == 5 or d2 == 5:
            self.rwin(n)
            return True
                
    def rwin(self, n):
        tot = 0
        for i in range(5):
            for j in range(5):
                if self.real[i][j] != "X":
                    tot += self.real[i][j]
        print(tot * n, n)
        
        self.won = True
    
    def showboard(self, b):
        for l in b:
            print(l)


bs = []
for i in range(2, len(file), 6):
    t = file[i:i+5]
    f = []
    for j in range(5):
        f.append([])
        for k in range(5):
            f[j].append(int(t[j][(k*3):((k+1)*3)]))
    b = Board(f)
    bs.append(b)

print(len(bs))
for i in inputs.split(","):
    l = 0
    for b in bs:
        if b.won == False:
            l += 1
            b.checkwin(int(i))
    print("left: " + str(l))

        