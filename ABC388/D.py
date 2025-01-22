from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

front_zero_count = defaultdict(int)

ans = [0] * N

zero_count = 0

for idx in range(N):
    zero_count += front_zero_count[idx]
    max_ans = A[idx] + idx - zero_count
    
    ans[idx] = max(0, max_ans - (len(A) - idx - 1))
    front_zero_count[idx + max_ans + 1] += 1

print(*ans)