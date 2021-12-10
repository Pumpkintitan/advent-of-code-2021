file = open("day10.txt").read().split("\n")
inn = ["(", "[", "{", "<"]
out = [")", "]", "}", ">"]
vals = [3, 57, 1197, 25137]
sc = [1, 2, 3, 4]
errors = []
scores = []
for l in file:
    stack = []
    err = False
    for c in l:
        if c in inn:
            for i in range(len(inn)):
                if inn[i] == c:
                    stack.append(out[i])
        else:
            if c == stack[-1]:
                stack.pop(-1)
            else:
                err = True
                errors.append(c)
                break
    if not err:
        sco = 0
        stack.reverse()
        for s in stack:
            for i in range(len(out)):
                if s == out[i]:
                    sco *= 5
                    sco += sc[i]
        scores.append(sco)
    
tot = 0
for e in errors:
    for i in range(len(out)):
        if e == out[i]:
            tot += vals[i]
print(tot)
scores.sort()
print(scores[int(len(scores)/2 - 0.5)])