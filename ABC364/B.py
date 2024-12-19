H, W = map(int, input().split())
current_x, current_y = map(int, input().split())

G = [list(input()) for _ in range(H)]

X = list(input())

for do in X:
    if do == "U":
        if current_x - 1 < 1:
            continue
        if G[current_x - 1 - 1][current_y - 1] == ".":
            current_x -= 1
    elif do == "D":
        if current_x + 1 > H:
            continue
        if G[current_x - 1 + 1][current_y - 1] == ".":
            current_x += 1
    elif do == "L":
        if current_y - 1 < 1:
            continue
        if G[current_x - 1][current_y - 1 - 1] == ".":
            current_y -= 1
    elif do == "R":
        if current_y + 1 > W:
            continue
        if G[current_x - 1][current_y - 1 + 1] == ".":
            current_y += 1

print(current_x, current_y)