N, Q = map(int, input().split())
A = list(map(int, input().split()))

grid = [False] * (N + 2)

count = 0

for a in A:
        if not grid[a - 1] and grid[a]:
            count -= 1

        if grid[a] and not grid[a + 1]:
            pass

        if grid[a] != grid[a-1]:
            count -= 1

        if grid[a] != grid[a+1]:
            count -= 1

        grid[a] = not grid[a]

        if grid[a] != grid[a-1]:
            count += 1

        if grid[a] != grid[a+1]:
            count += 1

        print(count // 2)