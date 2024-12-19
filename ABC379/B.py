N, K = map(int, input().split())
S = input()

count = 0

ans = 0

for i in range(N):
    if S[i] == "O":
        count += 1
    elif S[i] == "X":
        ans += count // K
        count = 0
else:
    ans += count // K
print(ans)
