N, W = map(int, input().split())
blocks_pos = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

column_block_num = [0] * W

has_block_column_count = 0
islined = False
lined_limit = 99999

for pos in blocks_pos:
    if column_block_num[pos[0] - 1] == 0:
        has_block_column_count += 1
    column_block_num[pos[0] - 1] += 1
    lined_limit = min(lined_limit, column_block_num[pos[0] - 1])

if has_block_column_count == W:
    islined = True

for time, block in query:
    
    current_block_pos = blocks_pos[block - 1]
    
    if islined == True:
        if time <= lined_limit:
            if column_block_num[current_block_pos[1] - 1] + 1 >= time:
                print("Yes")
            else:
                print("No")
        else:
            if column_block_num[current_block_pos[1] - 1] + 1 >= lined_limit:
                print("Yes")
            else:
                print("No")
    else:
        print("Yes")