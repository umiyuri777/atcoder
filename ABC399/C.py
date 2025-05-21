N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

edge = [[] for _ in range(N)]
for row in range(N):
    for column in range(N):
        edge[row].append(column)
        edge[column].append(row)

# 頂点数:n
# edge[i]:頂点iと辺で結ばれる頂点の集合



def dfs(x,last=-1):
    if last!=-1:
        parent[x]=last
    come[x]=True
    for i in edge[x]:
        if i ==last:continue
        if come[i]:
            now=x
            loop.add((now,i))
            loop.add((i,now))
            while now!=i:
                loop.add((now,parent[now]))
                loop.add((parent[now],now))
                now=parent[now]
            return True
        else:
            if dfs(i,x):
                return True
    return False

def search_heiro(x):
    # 遷移元の頂点
    parent=[-1]*N
    # 閉路に含まれる辺の集合
    loop =set()
    # 既に探索した頂点か
    come=[False]*N
    if come[x]:
        return 0
    else:
        dfs(x)
        return len(loop)

for e in edge:
    (search_heiro(e[0]))
