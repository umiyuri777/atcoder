N, D = map(int, input().split())

hebi = [list(map(int, input().split())) for _ in range(N)]

for k in range(1, D + 1):
    ans = 0
    for h in hebi:
        hebi_weight = h[0] * (h[1] + k)
        ans = max(ans, hebi_weight)
    print(ans)
