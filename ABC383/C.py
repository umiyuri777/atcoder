from collections import deque

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()

for row in range(H):
    for column in range(W):
        if S[row][column] == "H":
            q.append((row, column, 0))

explored_floors = set()

ans = len(q)

while len(q) > 0:
    row, column, count = q.popleft()

    for dif_row, dif_column in direction:
        if (row + dif_row < 0 or H - 1 < row + dif_row) or (column + dif_column < 0 or W - 1 < column + dif_column) or ((row + dif_row, column + dif_column) in explored_floors) or count + 1 > D:
            continue
        if S[row + dif_row][column + dif_column] == ".":
            explored_floors.add((row + dif_row , column + dif_column))
            q.append((row + dif_row, column + dif_column, count + 1))
            ans += 1
print(ans)