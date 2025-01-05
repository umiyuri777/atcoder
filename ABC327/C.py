A = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    row_check = set()
    column_check = set()
    for j in range(9):
        row_check.add(A[i][j])
        column_check.add(A[j][i])
    if len(row_check) != 9 or len(column_check) != 9:
        print("No")
        exit()

for i in range(3):
    for j in range(3):
        checkset = set()
        
        for row in range(3):
            for column in range(3):
                checkset.add(A[row + i * 3][column + j * 3])
        if len(checkset) != 9:
            print("No")
            exit()

print("Yes")