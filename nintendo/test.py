from collections import defaultdict

N = int(input())
codes = [list(map(str, input().split())) for _ in range(N)]


for row in range(N):
    dic = defaultdict(int)
    for code in codes[row]:
        lowered_code = code.lower()
        if lowered_code not in dic.keys():
            dic[code.lower()] += 1
        else:
            dic[code.lower()] += 100
    print(dic) 
