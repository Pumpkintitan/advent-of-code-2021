file = open("day7.txt").read().split("\n")
l = [int(i) for i in file[0].split(",")]
l.sort()
n = l[round(len(l)/2)]
print(n)
tot = 0
for num in l:
    tot += abs(num - n)
print(tot)

min = 999999999999999
for i in range(max(l)):
    print(i/max(l))
    tot = 0
    for num in l:
        b = abs(num - i)
        for j in range(b+1):
            tot += j
    if tot <= min:
        min = tot
print(min)
# low  99962223.5
# high 100148861
