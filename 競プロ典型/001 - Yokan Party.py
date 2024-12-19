N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(mid):
    num = 0
    pre = 0
    for i in A:
        if i - pre >= mid:
            num += 1
            pre = i
    if L - pre >= mid:
        num += 1
    return num >= (K + 1)

left = -1
right = L + 1

while right - left > 1:
    mid = (left + right) // 2
    if check(mid) == True:
        left = mid
    else:
        right = mid
print(left)
