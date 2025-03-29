# TLE
# 
N, Q = map(int, input().split())
nest = dict()
pigeon_position = dict()

for i in range(1, N + 1):
    nest[i] = {i}
    pigeon_position[i] = i

for _ in range(Q):
    query = list(map(int, input().split()))
    op = query[0]
    if op == 1:
        a = query[1]
        b = query[2]
        
        nest[pigeon_position[a]].remove(a)
        nest[b].add(a)
        pigeon_position[a] = b
    elif op == 2:
        a = query[1]
        b = query[2]
        
        temp = nest[a]
        nest[a] = nest[b]
        nest[b] = temp
        
        for nest_a in nest[a]:
            pigeon_position[nest_a] = a
        for nest_b in nest[b]:
            pigeon_position[nest_b] = b
        
    elif op == 3:
        a = query[1]
        print(pigeon_position[a])
