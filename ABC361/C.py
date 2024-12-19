N, K = map(int, input().split())

A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 99999999999999
for idx in range(K + 1):
    ans = min(ans, A[idx] - A[-K - 1 + idx])
print(ans)
