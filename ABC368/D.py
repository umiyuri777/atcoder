# 参考
# https://qiita.com/mattsunkun/items/686d98f71383ec29eaf7#%E6%9C%80%E5%BE%8C%E3%81%AB%E4%B8%80%E8%A8%80

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)

N, K = map(int, map(int, input().split()))

edge = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

V = list(map(int, input().split()))
for i in range(K):
    V[i] -= 1


W = [False] * N
for v in V:
    W[v] = True

ans = [False] * N

# v : 必要な頂点かどうかをみる対象
# p : どこの頂点から見にきたか
def rec(v, p):
    need = W[v]


    for u in edge[v]:
        if u == p:
            continue
        if rec(u, v):
            need = True
    
    if need:
        ans[v] = True

    return need

rec(V[0], -1)

print(ans.count(True))
