N = int(input())
P = list(map(int, input().split()))

ans = 0

for i in range(N - 3):
    a, b, c, d = P[i], P[i+1], P[i+2], P[i+3]
    # 1. 先頭2つが昇順
    if not (a < b):
        continue
    # 2. 山と谷の位置を調べる
    # 山: x < y > z
    # 谷: x > y < z
    peak = 0
    valley = 0
    seq = [a, b, c, d]
    for j in range(1, 3):
        if seq[j-1] < seq[j] > seq[j+1]:
            peak += 1
        if seq[j-1] > seq[j] < seq[j+1]:
            valley += 1
    if peak == 1 and valley == 1:
        ans += 1

print(ans)
