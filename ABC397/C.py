from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

left = defaultdict(int)
right = defaultdict(int)

for a in A:
    right[a] += 1

left[A[0]] += 1
right[A[0]] -= 1
if right[A[0]] == 0:
    right.pop(A[0])

ans = len(left) + len(right)

for i in range(1, N - 1):
    right[A[i]] -= 1
    left[A[i]] += 1
    if right[A[i]] == 0:
        right.pop(A[i])

    ans = max(ans, len(left) + len(right))
print(ans)