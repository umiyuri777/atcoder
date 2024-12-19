N = int(input())

A = list(map(int, input().split()))

num_dict = {}

ans = []

for i, a in enumerate(A):
    if a not in num_dict.keys():
        ans.append(-1)
        num_dict[a] = i
    else:
        ans.append(num_dict[a] + 1)
        num_dict[a] = i

print(*ans)