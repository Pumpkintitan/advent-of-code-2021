file = open("day13.txt").read().split("\n")
holes = [] 
insts = [] 
for line in file:
    if "," in line:
        l = line.split(",")
        holes.append([int(l[0]), int(l[1])])
    elif line:
        i = line.split(" ")
        inst = i[2]
        insts.append((inst[0], int(inst[2:])))
for i in insts:
    uniques = {}
    if i[0] == "y":
        for h in holes:
            if h[1] > i[1]:
                h[1] = i[1] - (h[1] - i[1])
            if str(h) in uniques:
                uniques[str(h)] += 1
            else:
                uniques[str(h)] = 1
    else:
        for h in holes:
            if h[0] > i[1]:
                h[0] = i[1] - (h[0] - i[1])
            if str(h) in uniques:
                uniques[str(h)] += 1
            else:
                uniques[str(h)] = 1
b = [["." for i in range(40)] for j in range(7)]
for h in holes:
    b[h[1]][h[0]] = "#"
for l in b:
    s = ""
    for c in l:
        s += c
    print(s)

