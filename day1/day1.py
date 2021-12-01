file = open("day1.txt").read().split("\n")
nums = [int(num) for num in file if num]
#part 1
prev = 0
tot = 0
for n in nums:
    if prev != 0:
        if n > prev:
            tot += 1
    prev = n
print(tot)
#part 2
prev = 0
tot = 0
for i in range(0, len(nums) - 2):
    s = nums[i] + nums[i+1] + nums[i+2]
    if prev != 0:
        if s > prev:
            tot += 1
    prev = s
print(tot)