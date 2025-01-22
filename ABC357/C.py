N = int(input())
N3 = 3 ** N
ans = [["#"] * 3 ** N for _ in range(3 ** N)]

def change_tile(k, x, y):
    if k == 0:
        return
    for i in range(3 ** (k - 1)):
        for j in range(3 ** (k - 1)):
            ans[x + i + 3 ** (k - 1)][y + j + 3 ** (k - 1)] = "."
    for dx in range(3):
        for dy in range(3):
            if dx == 1 and dy == 1:
                continue
            change_tile(k - 1, x + dx * 3 ** (k - 1), y + dy * 3 ** (k - 1))

change_tile(N, 0, 0)

for a in ans:
    print("".join(a))