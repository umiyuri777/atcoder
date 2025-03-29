N , M = map(int, input().split())

edge = [list(map(int, input().split())) for _ in range(M)]

node = [[] for _ in range(M + 1)]

for e in edge:
    node[e[1]].append(e[0])
    node[e[0]].append(e[1])

while 