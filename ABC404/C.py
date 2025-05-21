N, M = map(int, input().split())

hands = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    hands[a].append(b)
    hands[b].append(a)

if N != M:
    print("No")
    exit()

for i in range(N):
    if len(hands[i]) != 2:
        print("No")
        exit()

def dfs(start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in hands[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited

visited = dfs(0, set())

if len(visited) == N:
    print("Yes")
else:
    print("No")
