file = open("day2.txt").read().split("\n")
#part 1
hor = 0
depth = 0
for line in file:
    l = line.split(" ")
    c = l[0][0]
    if c == "f":
        hor += int(l[1])
    elif c == "u":
        depth -= int(l[1])
    elif c == "d":
        depth += int(l[1])
print(hor*depth)
#part 2
hor = 0
depth = 0
aim = 0
for line in file:
    l = line.split(" ")
    c = l[0][0]
    if c == "f":
        hor += int(l[1])
        depth += (aim * int(l[1]))
    elif c == "u":
        aim -= int(l[1])
    elif c == "d":
        aim += int(l[1])
print(hor*depth)