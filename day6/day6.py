file = open("day6.txt").read().split("\n")
l = [int(i) for i in file[0].split(",")]

days = 256

counts = {}
for i in range(9):
    counts[i] = 0

for n in l:
    counts[n] += 1

tot = 0

for i in range(days):
    temp = counts[0]
    for i in range(8):
        counts[i] = counts[i + 1]
    counts[8] = temp
    counts[6] += temp

for key in counts:
    tot += counts[key]

print(tot)