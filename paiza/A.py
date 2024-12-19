import sys
# 再起回数の上限を上げておく
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())

planes = [list(map(int, input().split())) for _ in range(H)]
ans = [0]

def dfs(row, column, count):
    # 一番下まで行ったら答え格納して再帰終わり
    if row == H:
        ans[0] = max(ans[0], count)
        return

    # 答え計算
    count += planes[row][column]

    # 左手前、手前、右手前の順で再帰
    for i in range(3):

        # 右端 or 左端よりも外に出たら飛ばす
        if (column + (i - 1) == W) or (column + (i - 1) < 0):
            continue

        # 再帰
        dfs(row + 1, column + (i - 1), count)


for column in range(W):
    max_sum = dfs(row = 0, column = column, count = 0)

print(ans[0])
