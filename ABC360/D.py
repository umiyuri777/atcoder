from collections import defaultdict

N, T = map(int, input().split())
S = list(input())
X = list(map(int, input().split()))

list_0 = []
list_1 = []

for idx in range(N):
    if S[idx] == "0":
        list_0.append(X[idx])
    else:
        list_1.append(X[idx])

ans = 0

left = 0
right = 0

for pointer in range(len(list_1)):
    while left < len(list_0) and list_0[left] < list_1[pointer]:
        left += 1
    while right < len(list_0) and list_0[right] <= list_1[pointer] + 2 * T:
        right += 1
    print("left: ", left)
    print("right: ", right)
    ans += right - left
print(ans)
