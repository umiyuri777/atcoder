import sys
sys.setrecursionlimit(10 ** 8)

N, K = map(int, input().split())

R = list(map(int, input().split()))

current = []
answers = []

def dfs(digit):
    # 再帰で最終桁までいったら
    if len(current) == N:
        if sum(current) % K == 0:
            answers.append(current[:])
        return

    # 再帰で全探索動かす
    max_r = R[digit-1]

    for i in range(1, max_r + 1):
        current.append(i)
        dfs(digit + 1)
        current.pop()

dfs(1)

for answer in answers:
    print(*answer)