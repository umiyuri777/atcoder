"""
無限数列だが、Aの合計値でSを破ることで、A * 2だけ見ればいい

"""

N, S = map(int, input().split())

A = list(map(int, input().split()))

sum_A = sum(A)

# Aの合計がSより大きいなら、余りを計算して
if sum_A < S:
    p, remain = divmod(S, sum_A)
    S = remain

A = A * 2

l = 0
r = 0
total = A[0]
while l < 2 * N:
    if total > S:
        total -= A[l]
        l += 1
    elif total < S:
        r += 1
        if r >= len(A):
            break
        total += A[r]
    else:
        print("Yes")
        exit()

print("No")