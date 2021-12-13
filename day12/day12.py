file = open("day12.txt").read().split("\n")
graph = {}
for line in file:
    l = line.split("-")
    if l[0] not in graph:
        graph[l[0]] = [l[1]]
    else:
        graph[l[0]].append(l[1])
    if l[1] not in graph:
        graph[l[1]] = [l[0]]
    else:
        graph[l[1]].append(l[0])

tot = 0

def go(name, v, p, s):
    b = 0
    if name != "start":
        p.append(name)
        if 97 <= ord(name[0]) <= 122:
            if name in v:
                v[name] += 1
                s = True
            else:
                v[name] = 1
    for n in graph[name]:
        if n == "end":
            p.append("end")
            # print(p)
            b += 1
        elif not s:
            if n not in v or v[n] < 2:
                b += go(n,v.copy(),p.copy(), s)
        elif s:
            if n not in v:
                b += go(n,v.copy(),p.copy(), s)
    return b

print(graph)
print(go("start", {"start":2}, ["start"], False))
#low 9824