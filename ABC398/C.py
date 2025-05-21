from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

a_dict = defaultdict(int)
for i in range(N):
    if A[i] not in a_dict:
        a_dict[A[i]] = i
    else:
        a_dict[A[i]] = -1

tmp = {}

for k, v in a_dict.items():
    if v != -1:
        tmp[k] = v

if len(tmp) == 0:
    print(-1)
else:
    print(tmp[max(tmp.keys())] + 1)
