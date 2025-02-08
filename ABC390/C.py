H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

min_H = 999999
max_H = 0
min_W = 999999
max_W = 0

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            min_H = min(min_H, h)
            max_H = max(max_H, h)
            min_W = min(min_W, w)
            max_W = max(max_W, w)

for h in range(min_H, max_H + 1):
    for w in range(min_W, max_W + 1):
        if S[h][w] == ".":
            print("No")
            exit()
print("Yes")