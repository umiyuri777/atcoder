import itertools

N, M = map(int, input().split())

ga = [[0] * N for _ in range(N)]
gb = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    
    u -= 1
    v -= 1
    ga[u][v] = ga[v][u] = 1

for _ in range(M):
    u, v = map(int, input().split())
    
    u -= 1
    v -= 1
    gb[u][v] = gb[v][u] = 1

ans = False

for p in list(itertools.permutations(range(N))):
    flag = True
    for i in range(N):
        for j in range(N):
            if ga[i][j] != gb[p[i]][p[j]]:
                flag = False
    
    if flag == True:
        ans = True
        break

if ans:
    print("Yes")
else:
    print("No")