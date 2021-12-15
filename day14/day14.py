file = open("day14.txt").read().split("\n")
poly = file[0]
template = {}
poly2 = {}
for i in range(2, len(file)):
    l = file[i].split(" -> ")
    template[l[0]] = l[1]
    poly2[l[0]] = 0

for i in range(len(poly) - 1):
    pair = poly[i:i+2]
    poly2[pair] += 1


def p1():
    for i in range(10):
        print(i)
        temp = ""
        for j in range(len(poly) - 1):
            pair = poly[j:j+2]
            if pair in template:
                temp += pair[0] + template[pair]
        poly = temp + poly[-1]

    counts = {}
    for c in poly:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    cs = sorted(counts, key=counts.get)
    print(counts[cs[-1]] - counts[cs[0]])

counts = {}
for c in poly:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

print(poly2)
for i in range(40):
    print(i)
    polytemp = poly2.copy()
    for j in poly2:
        if poly2[j] > 0:
            ns1 = j[0] + template[j]
            ns2 = template[j] + j[1]
            polytemp[ns1] += poly2[j]
            polytemp[ns2] += poly2[j]
            polytemp[j] -= poly2[j]
            if template[j] in counts:
                counts[template[j]] += poly2[j]
            else:
                counts[template[j]] = poly2[j]
    poly2 = polytemp.copy()
cs = sorted(counts, key=counts.get)
print(counts[cs[-1]], counts[cs[0]])
print(counts[cs[-1]] - counts[cs[0]])