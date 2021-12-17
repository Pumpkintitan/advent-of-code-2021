import numpy as np
file = open("day16.txt").read().split("\n")
htob = {"0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111", }
bin = ""
for c in file[0]:
    bin += htob[c]
b = True
bs = 0
codes = []


def pLiteral(bs):
    s = ""
    c = 1
    while bin[bs] == "1":
        P = bin[bs+1:bs+5]
        s += P
        bs += 5
        c += 1
    P = bin[bs+1:bs+5]
    s += P
    return int(s, 2), 5 * c


def pOperator(BT, bs):
    OI = bin[bs]
    ll = 0
    TT = []
    nums = []
    if OI == "0":
        L = int(bin[bs+1:bs+16], 2)
        bs += 16
        ll += 16
        c = 0
        temp = []
        while c < L:
            tt = []
            V = int(bin[bs:bs+3], 2)
            tt.append(V)
            T = int(bin[bs+3:bs+6], 2)
            tt.append(T)
            bs += 6
            ll += 6
            if T == 4:
                t, l = pLiteral(bs)
                c += 6 + l
                bs += l
                ll += l
                nums.append(t)
                tt.append(t)
            else:
                t, l = pOperator(T, bs)
                c += 6 + l
                bs += l
                ll += l
                tt.append(t)
                nums.append(t)
            temp.append(tt)
        TT = temp
    if OI == "1":
        L = int(bin[bs+1:bs+12], 2)
        bs += 12
        ll += 12
        c = 0
        temp = []
        while c < L:
            tt = []
            V = int(bin[bs:bs+3], 2)
            tt.append(V)
            T = int(bin[bs+3:bs+6], 2)
            tt.append(T)
            bs += 6
            ll += 6
            if T == 4:
                t, l = pLiteral(bs)
                c += 1
                bs += l
                ll += l
                tt.append(t)
                nums.append(t)
            else:
                t, l = pOperator(T, bs)
                c += 1
                bs += l
                ll += l
                tt.append(t)
                nums.append(t)
            temp.append(tt)
        TT = temp
    if BT == 0:
        print("Sum", nums)
        return (sum(nums), ll)
    elif BT == 1:
        print("Product", nums)
        return (np.prod(nums), ll)
    elif BT == 2:
        print("Min", nums)
        return (min(nums), ll)
    elif BT == 3:
        print("Max", nums)
        return (max(nums), ll)
    elif BT == 5:
        print("Greater", nums)
        return (1 if nums[0] >= nums[1] else 0, ll)
    elif BT == 6:
        print("Less", nums)
        return (1 if nums[0] <= nums[1] else 0, ll)
    elif BT == 7:
        print("Equal", nums)
        return (1 if nums[0] == nums[1] else 0, ll)


while len(bin[bs:]) > 10:
    curr = []
    V = int(bin[bs:bs+3], 2)
    curr.append(V)
    T = int(bin[bs+3:bs+6], 2)
    curr.append(T)
    bs += 6
    if T == 4:
        t, l = pLiteral(bs)
        curr.append(t)
        bs += l
    else:
        t, l = pOperator(T, bs)
        curr.append(t)
        bs += l

    codes.append(curr)
print(codes[0][2])


# low 19325021544106
# low 19323190162616


# def gettot(d):
#     if isinstance(d, list) and len(d) == 1:
#         return gettot(d[0])
#     else:
#         t = 0
#         if isinstance(d[2], list):
#             for dd in d[2]:
#                 t += gettot(dd)
#             return t + d[0]
#         else:
#             return d[0]


# tot = 0
# for d in codes:
#     tot += gettot(d)
# print(tot)
