N = int(input())

num = []

for k in range(60, -1, -1):
    if N >= 2 ** k:
        num.append(k)
        N -= 2 ** k

num.reverse()

for i in range(2 ** len(num)):
    tmp = 0
    for j in range(len(num)):
        if ((i >> j) & 1):
            tmp += 2 ** num[j]
    print(tmp)