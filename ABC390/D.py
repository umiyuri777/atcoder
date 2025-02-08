# N = int(input())
# A = list(map(int, input().split()))

# xors = set()

# def xor(arr):
#     ret = 0
#     for i in arr:
#         ret ^= i
#     return ret


# def dfs(groups, n):
#     if n == N:
#         xors.add(xor(groups))
#         return
    
#     for i in range(len(groups) + 1):
#         if i == len(groups):
#             dfs(groups + [A[n]], n + 1)
#         else:
#             groups[i] += A[n]
#             dfs(groups, n + 1)
#             groups[i] -= A[n]
# dfs([], 0)

# print(len(xors))

nums = [7, 13,17,24]
for i in range(4):
    nums[i] = nums[i] ** 7 % 33
print(*nums)

for i in range(4):
    nums[i] = nums[i] ** 3 % 33
print(*nums)