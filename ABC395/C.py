from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

num_position = defaultdict(list)
ans = 99999999999999
for idx in range(N):
    current_a = A[idx]
    if len(num_position[current_a]) != 0:
        ans = min(idx - num_position[current_a][-1], ans)
    num_position[current_a].append(idx)
if ans == 99999999999999:
    print(-1)
else:
    print(ans + 1)