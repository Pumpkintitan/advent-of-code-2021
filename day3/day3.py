file = open("day3.txt").read().split("\n")
g = ""
e = ""
#part 1
for i in range(len(file[0])):
    ones = 0
    zeros = 0
    for j in range(len(file)):
        if file[j][i] == "0":
            zeros += 1
        if file[j][i] == "1":
            ones += 1
    if ones > zeros:
        g += "1"
        e += "0"
    else:
        e += "1"
        g += "0"
print(int(g,2)*int(e,2))
#part 2
o = []
c = []
file.sort()
for j in range(len(file)):
    if file[j][0] == "1":
        if j >= len(file)/2:
            c = file[j:]
            o = file[:j]
        else:
            o = file[j:]
            c = file[:j]
        break

for i in range(1,len(file[0])):
    if len(o) == 1:
        break
    o.sort()
    for j in range(len(o)):
        if o[j][i] == "1":
            print(i,j, j >= len(o)/2)
            if j == len(o)/2:
                o = o[j:]
            elif j >= len(o)/2:
                o = o[:j]
            else:
                o = o[j:]
            break

for i in range(1,len(file[0])):
    if len(c) == 1:
        break
    c.sort()
    for j in range(len(c)):
        if c[j][i] == "1":
            print(i,j, j >= len(c)/2)
            if j == len(c)/2:
                c = c[:j]
            elif j >= len(c)/2:
                c = c[j:]
            else:
                c = c[:j]
            break
print(int(o[0],2) * int(c[0],2))

a = [1,2,3,4,5]
print(a[:2], a[2:])
            
    