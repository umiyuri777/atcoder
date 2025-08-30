N, K, X = map(int, input().split())

S = [input() for _ in range(N)]

collections = []


def dfs(A):
    if len(A) == K:
        collections.append("".join(A))
        return
    
    for v in range(N):
        A.append(S[v])
        dfs(A)
        A.pop()

dfs([])

collections.sort()

print(collections[X - 1])