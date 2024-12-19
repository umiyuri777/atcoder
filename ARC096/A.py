A, B, C, X, Y = map(int, input().split())

# 全部AピザとBピザで計算
sum = A * X + B * Y

for ABpizza in range(0, (max(X, Y) * 2) + 1, 2):

    tmp_X = X - ABpizza // 2
    tmp_Y = Y - ABpizza // 2

    tmp_sum = max(0, tmp_X) * A + max(0, tmp_Y) * B + ABpizza * C
    sum = min(sum, tmp_sum)
print(sum)
