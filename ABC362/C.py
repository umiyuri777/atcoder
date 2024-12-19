N = int(input())
L = [0] * N
R = [0] * N

for i in range(N):
    L[i], R[i] = map(int, input().split())

if sum(L) > 0 or sum(R) < 0:
    print("No")
    exit()

S = sum(L)
ans = []
sum_a = -S
for i in range(N):
    a = min(R[i] - L[i], sum_a)
    x = L[i] + a
    ans.append(x)
    sum_a -= a
print('Yes')
print(*ans)