N, X, Y = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

A_sum = 0
B_sum = 0

for idx in range(N):
    A_sum += A[idx]
    B_sum += B[idx]
    if A_sum > X or B_sum > Y:
        break
print(idx + 1)