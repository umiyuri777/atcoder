N = int(input())
A = list(map(int, input().split()))

ans = 0
sum = 0

for i in range(N):
    ans += sum * A[i]
    sum += A[i]
print(ans)
