N, M = map(int, input().split())

d = [1 for _ in range(M + 1)]

for i in range(N):
    l, r = map(int, input().split())
    d[r] = max(d[r], l + 1)

for R in range(1, M + 1):
    d[R] = max(d[R], d[R - 1])

count = 0

for i in range(M + 1):
    count += i - d[i] + 1

print(count)
