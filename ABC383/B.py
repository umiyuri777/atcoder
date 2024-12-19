H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

floors = []

for row in range(H):
    for column in range(W):
        if S[row][column] == ".":
            floors.append((row, column))

ans = 0

for i in range(len(floors)):
    for j in range(len(floors)):
        
        count = 0
        
        if i == j:
            continue
        humidifier1 = floors[i]
        humidifier2 = floors[j]
        
        for row in range(H):
            for column in range(W):
                if S[row][column] == ".":
                    if abs(row - humidifier1[0]) + abs(column - humidifier1[1]) <= D or abs(row - humidifier2[0]) + abs(column - humidifier2[1]) <= D:
                        count += 1
        ans = max(ans, count)
print(ans)