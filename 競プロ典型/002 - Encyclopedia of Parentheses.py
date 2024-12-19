N = int(input())

if N % 2 != 0:
    exit()


for shift in range(1 << N):

    kakko_list = []
    count = 0

    for i in range(N - 1, -1, -1):
        if 1 & (shift >> i):
            kakko_list.append(")")
        else:
            kakko_list.append("(")
    
    for kakko in kakko_list:
        if kakko == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print(*kakko_list, sep = '')

