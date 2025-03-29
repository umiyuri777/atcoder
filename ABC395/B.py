N = int(input())

G = [["."] * N for _ in range(N)]

for i in range(1, N + 1):
    j = N + 1 - i
    if i <= j:
        # #で塗りつぶす
        if i % 2 != 0:
            for row in range(i-1, j):
                for column in range(i-1, j):
                    G[row][column] = "#"
        if i % 2 == 0:
            for row in range(i-1, j):
                for column in range(i-1, j):
                    G[row][column] = "."
for g in G:
    print("".join(g))