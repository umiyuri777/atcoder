"""
幅優先探索
1. マス一つ一つに対して幅優先探索してって、消せるマスを消す
2. できるだけ下にずらす

これを繰り返してく
マスの大きさは 5*10 だから多分間に合う
"""

from collections import deque

H = int(input())

S = [list(input()) for _ in range(H)]

direction = [(0,1), (0,-1), (1,0), (-1,0)]

while True:
    # 消せるブロック探す
    delete_blocks = []
    for row in range(H):
        for column in range(5):

            common_blocks = []
            isDelete = True

            # 各マスに対して四方向探索する
            for dy, dx in direction:
                y2 = row + dy
                x2 = column + dx

                # 範囲外なら飛ばす
                if not (0 <= y2 < H and 0 <= x2 < 5):
                    continue

                if S[y2][x2] == ".":
                    isDelete = False
                    break

                if S[y2][x2]!= S[row][column]:
                    isDelete = False
                    break

                common_blocks.append((y2, x2))
            if isDelete == True:
                delete_blocks.append((row, column))
                delete_blocks.extend(common_blocks)
    if len(delete_blocks) == 0:
        for i in S:
            print(''.join(i))
        exit()

    # 空いたブロック分だけ下に下げる
    for column in range(5):
        temp = []
        for row in range(H):
            if S[row][column] != ".":
                if (row, column) not in delete_blocks:
                    temp.append(S[row][column])
                S[row][column] = "."

        temp_count = 0
        for row in range(H - len(temp), H):
            S[row][column] = temp[temp_count]
            temp_count += 1
