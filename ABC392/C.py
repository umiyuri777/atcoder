N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = [0] * (N)

for i in range(N):
    current_zekken = Q[i]
    manazashi = P[i]
    ans[current_zekken - 1] = Q[manazashi - 1]
print(*ans)