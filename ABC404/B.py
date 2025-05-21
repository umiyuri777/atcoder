import copy
N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

if S == T:
    print(0)
    exit()

match_count = []

# 0度回転させて比較
count = 0
for row in range(N):
    for col in range(N):
        if S[row][col] == T[row][col]:
            count += 1
match_count.append(count)

# 90度回転させて比較
for i in range(3):
    rotate_s = []
    
    # 90度回転させる
    for x in zip(*S[::-1]):
        rotate_s.append(list(x))

    count = 0
    for row in range(N):
        for col in range(N):
            if rotate_s[row][col] == T[row][col]:
                count += 1
    match_count.append(count)

    S = copy.deepcopy(rotate_s)


total_operations = []
for idx, m in enumerate(match_count):
    operations = idx + (N**2 - m)
    total_operations.append(operations)

ans = min(total_operations)
print(ans)
