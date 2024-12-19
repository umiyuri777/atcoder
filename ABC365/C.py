N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

MAX = 2 * 10 ** 14 + 1

# 二分探索
left = 0
right = MAX + 1

while right - left > 1:
    mid = (left + right) // 2

    cost = 0
    for a in A:
        if a < mid:
            cost += a
        else:
            cost += mid

    if cost <= M:
        left = mid
    else:
        right = mid

if left == MAX:
    print("infinite")
else:
    print(left)
