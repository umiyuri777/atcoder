S = [list(input()) for _ in range(8)]

result = [["."] * 8 for _ in range(8)]

count = 0

for row in range(8):
    for column in range(8):
        if S[row][column] == "#":
            for i in range(8):
                result[i][column] = "#"
                result[row][i] = "#"

for row in range(8):
    for column in range(8):
        if result[row][column] == ".":
            count += 1


print(count)