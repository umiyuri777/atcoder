S = list(input())
S_riverse = [i.swapcase() for i in S]
print(S_riverse)
Q = int(input())

K = list(map(int, input().split()))

ans = []

for k in K:
    shou, amari = divmod(k, len(S))
    if (shou % 2 == 0 and amari != 0) or (shou % 2 == 1 and amari == 0):
        if amari == 0:
            ans.append(S[0])
        else:
            ans.append(S[amari - 1])
    else:
        if amari == 0:
            ans.append(S_riverse[0])
        else:
            ans.append(S_riverse[amari - 1])

print(*ans)
