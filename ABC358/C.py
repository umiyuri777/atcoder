N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 999

for i in range(2 ** N):
    tmp = set()
    choiced_shop_num = 0
    for j in range(N):
        if ((i >> j) & 1):
            choiced_shop_num += 1
            for k in range(len(S[j])):
                if S[j][k] == "o":
                    tmp.add(k)
        if len(tmp) == M:
            ans = min(ans, choiced_shop_num)
print(ans)