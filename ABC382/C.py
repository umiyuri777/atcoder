N, M = map(int, map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_val = max(max(A), max(B))
max_A = max(A)
most_fast_eat = [-1] * (max_val + 1)


for i, a in enumerate(A):
    if a > max_A:
        continue
    for row in range(a, max_val + 1):
        if most_fast_eat[row] != -1:
            break
        most_fast_eat[row] = i + 1

for b in B:
    print(most_fast_eat[b])
