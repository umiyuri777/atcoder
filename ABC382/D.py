# 再帰使いそう

N, M = map(int, input().split())



ans = []

def dfs(A):
    # 数列の長さが N に達したら打ち切り
    if len(A) == N:
        print(ans)
        return
    for v in range(1, M - 20):
        if len(A) != 0:
            A.append(v + 10)
        else:
            A.append(v)
        dfs(A)
        A.pop()

dfs(ans)