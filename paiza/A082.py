# キューをインポート
from collections import deque
import copy

H, W = map(int, input().split())

G = [list(input()) for _ in range(H)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(temp_G, row, column):
    Q = deque()
    Q.append([row, column])


    while len(Q) > 0:
        y, x = Q.popleft()

        for dy, dx in direction:
            y2 = y + dy
            x2 = x + dx

            if not (0 <= y2 < H and 0 <= x2 < W):
                continue

            if temp_G[y2][x2] == ".":
                continue

            if visited[y2][x2] == False:
                visited[y2][x2] = True
                Q.append([y2, x2])

    for i in range(H):
        for j in range(W):
            if temp_G[i][j] == "#" and visited[i][j] == False:
                return False
    return True



count = 0
for row in range(H):
    for column in range(W):
        # 空いてるとこを数える
        if G[row][column] == ".":
            count += 1

        # 湖なら分断しないか判定
        elif G[row][column] == "#":
            for dr, dc in direction:
                row2 = row + dr
                column2 = column + dc
                if not (0 <= row2 < H and 0 <= column2 < W):
                    continue
                if G[row2][column2] == "#":
                    visited = [[False]*W for _ in range(H)]
                    temp_G = copy.deepcopy(G)
                    temp_G[row][column] = "."

                    if bfs(temp_G, row + dr, column + dc):
                        count += 1
                        break
                    else:
                        break

print(count)

