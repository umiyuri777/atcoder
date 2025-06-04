H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


ans = 0

def dfs(x, y, visited):
    stack = [(x, y)]
    
    visited.add((x, y, visited))
    while stack:
        x, y, visited = stack.pop()
        
        
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited:
                if A[nx][ny] == ans:
                    visited.add((nx, ny))
                    stack.append((nx, ny))

visited = set()
dfs(0,0, visited)
print(ans)