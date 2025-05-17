# 再帰使いそう

N, M = map(int, input().split())

ans = []
A = []
def dfs(A, idx, depth):
    # 数列の長さが N に達したら打ち切り
    if len(A) == N:
        print(A)
        if A[-1] <= M:
            ans.append(A[:])
            return
        else:
            return
    for v in range(idx, M - 10 * (N - 1 - depth) + 1):
        if len(A) != 0:
            v += 10
        A.append(v)

        dfs(A, v, depth + 1)
        A.pop()

dfs(A, 1, 0)
# print(len(ans))
# for a in ans:
#     print(*a)