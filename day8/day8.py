file = open("day8.txt").read().split("\n")
#part 1
tot = 0
lens = [2,3,4,7]
for l in file:
    li = l.split("|")
    le = li[1].split(" ")
    for c in le:
        if len(c) in lens:
            tot += 1
print(tot)
#part 2
letters = {"[1, 1, 1, 0, 1, 1, 1]":"0",
"[0, 0, 1, 0, 0, 1, 0]":"1",
"[1, 0, 1, 1, 1, 0, 1]":"2",
"[1, 0, 1, 1, 0, 1, 1]":"3",
"[0, 1, 1, 1, 0, 1, 0]":"4",
"[1, 1, 0, 1, 0, 1, 1]":"5",
"[1, 1, 0, 1, 1, 1, 1]":"6",
"[1, 0, 1, 0, 0, 1, 0]":"7",
"[1, 1, 1, 1, 1, 1, 1]":"8",
"[1, 1, 1, 1, 0, 1, 1]":"9",}
tot = 0
for l in file:
    li = l.split("|")
    le = li[1].split(" ")
    lo = li[0].split(" ")
    lo.sort(key=len)
    lets = ["a", "b", "c", "d", "e", "f", "g"]
    #swap for 1
    for c in lo[1]:
        i = lets.index(c)
        if not(c == lets[2] or c == lets[5]):
            if not(lets[2] in lo[1]):
                lets[2], lets[i] = lets[i], lets[2]
            elif not(lets[5] in lo[1]):
                lets[5], lets[i] = lets[i], lets[5]
    #swap for 7, top is guarenteed
    for c in lo[2]:
        i = lets.index(c)
        if not(c in lo[1]):
            lets[0], lets[i] = lets[i], lets[0]
    #swap for 4
    for c in lo[3]:
        i = lets.index(c)
        if not(c in lo[1]):
            if not(c == lets[1] or c == lets[3]):
                if not(lets[1] in lo[3]):
                    lets[1], lets[i] = lets[i], lets[1]
                elif not(lets[3] in lo[3]):
                    lets[3], lets[i] = lets[i], lets[3]
    #find 9, bottom is guarenteed
    for n in lo[7:10]:
        temps = lets[:4] + [lets[5]]
        co = 0
        for cc in lo[3]:
            if cc in n:
                co += 1
        if co == 4:
            for c in n:
                i = lets.index(c)
                if not(c in temps):
                    lets[6], lets[i] = lets[i], lets[6]
            break
    #find 3, middle and [1] guarenteed
    for n in lo[4:7]:
        temps = lets[5:] + [lets[0]] + [lets[2]]
        co = 0
        for c in n:
            if c in temps:
                co += 1
        if co == 4:
            for c in n:
                if not(c in temps):
                    if not(c == lets[3]):
                        lets[3], lets[1] = lets[1], lets[3]
    #find 5, [2] and [5] guarenteed
    for n in lo[4:7]:
        temps = lets[0:2] + [lets[3]] + [lets[6]]
        co = 0
        for c in n:
            if c in temps:
                co += 1
        if co == 4:
            for c in n:
                if not(c in temps):
                    if not(c == lets[5]):
                        lets[2], lets[5] = lets[5], lets[2]
    #lets should be complete
    full = ""
    for num in le:
        if len(num) > 1:
            print(num, lets)
            t = [0, 0, 0, 0, 0, 0, 0]
            for i in range(len(lets)):
                if lets[i] in num:
                    t[i] = 1
            full += letters[str(t)]
    tot += int(full)
print(tot)