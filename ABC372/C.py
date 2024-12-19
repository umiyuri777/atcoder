import re

N, Q = map(int, input().split())
S = list(input())
query = [list(map(str, input().split())) for _ in range(Q)]

ans = 0

for i in range(N - 2):
    if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        ans += 1

for x, c in query:
    x = int(x) - 1
    for i in range(2, -1, -1):
        if x - i  < 0 or x - i + 2 >= N:
            continue
        if S[x - i] == "A" and S[x - i + 1] == "B" and S[x - i + 2] == "C":
            ans -= 1
            continue

    S[x] = c

    for i in range(2, -1, -1):
        if x - i  < 0 or x - i + 2 >= N:
            continue
        if S[x - i] == "A" and S[x - i + 1] == "B" and S[x - i + 2] == "C":
            ans += 1
            continue 

    print(ans)