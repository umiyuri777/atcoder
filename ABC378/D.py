# キューをインポート
from collections import deque

# 入力を受け取る。座標の調整のため、スタート地点とゴール地点の座標を-1する。
H, W, K = map(int, input().split())

# 迷路の情報を配列Gで受け取る
G = [input() for _ in range(H)]

ans = 0

flag = False

for row in range(H):
    for column in range(W):
        # キューをQに入れ、スタート地点を追加

        if G[row][column] == "#":
            continue

        Q = deque()
        Q.append([row, column])

        # 未訪問と始点からの距離を管理するdistを定義。スタート地点に0を代入。
        dist = [[-1]*W for _ in range(H)]
        dist[row][column] = 0

        # 今回は移動する４方向を事前に用意した。
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        print("--------")
        # キューの要素がなくなるまで処理を繰り返す。
        while len(Q) > 0:
            y, x = Q.popleft()

            # 移動先で繰り返し処理
            for dy, dx in dirc:
                y2 = y + dy
                x2 = x + dx

                # 移動先が迷路の範囲内でなければ、continue
                if not (0 <= y2 < H and 0 <= x2 < W):
                    count = dist[y][x]
                    if count == K:
                        ans += 1
                    continue

                # 移動先が壁だったら、continue
                if G[y2][x2] == "#":
                    continue

                # 移動先が未訪問なら移動前の距離＋１をdistに入れて、キューに移動先の座標を追加
                if dist[y2][x2] == -1:
                    count = dist[y][x]
                    dist[y2][x2] = count + 1
                    Q.append([y2, x2])
                print("count: ",count)
                if count == K:
                    ans += 1
                    flag = True
                    break

            if flag == True:
                flag = False
                break

print(dist)
print(ans)
