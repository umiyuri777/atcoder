N, M = map(int, input().split())

koma = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

result = []

count = N ** 2

result_set = set()

for row, column in koma:
    if (row, column) not in result_set:
        result_set.add((row, column))
        count -= 1

    if 0 <= row + 2 < N and 0 <= column + 1 < N:
        if (row + 2, column + 1) not in result_set:
            result_set.add((row + 2, column + 1))
            count -= 1

    if 0 <= row + 1 < N and 0 <= column + 2 < N:
        if (row + 1, column + 2) not in result_set:
            result_set.add((row + 1, column + 2))
            count -= 1

    if 0 <= row - 1 < N and 0 <= column + 2 < N:
        if (row - 1, column + 2) not in result_set:
            result_set.add((row - 1, column + 2))
            count -= 1

    if 0 <= row - 2 < N and 0 <= column + 1 < N:
        if (row - 2, column + 1) not in result_set:
            result_set.add((row - 2, column + 1))
            count -= 1

    if 0 <= row - 2 < N and 0 <= column - 1 < N:
        if (row - 2, column - 1) not in result_set:
            result_set.add((row - 2, column - 1))
            count -= 1

    if 0 <= row - 1 < N and 0 <= column - 2 < N:
        if (row - 1, column - 2) not in result_set:
            result_set.add((row - 1, column - 2))
            count -= 1

    if 0 <= row + 1 < N and 0 <= column - 2 < N:
        if (row + 1, column - 2) not in result_set:
            result_set.add((row + 1, column - 2))
            count -= 1

    if 0 <= row + 2 < N and 0 <= column - 1 < N:
        if (row + 2, column - 1) not in result_set:
            result_set.add((row + 2, column - 1))
            count -= 1

result = [list(pos) for pos in result_set]

print(count)
