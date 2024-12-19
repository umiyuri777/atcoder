N = int(input())

S_list = [list(input()) for _ in range(N)]

len_list = []

max_index = 0

max_column = 0

def bigger_check(lenlist, check_num):
    for l in lenlist:
        if l - 1 >= check_num:
            return True
    return False

for i, s in enumerate(S_list):
    len_list.append(len(s))
    if len(s) > max_column:
        max_index = i
        max_column = len(s)

for column in range(max_column):
    for row in range(N - 1, -1, -1):
        if column >= len(S_list[row]):
            temp = len_list[:row]
            if not bigger_check(temp, column):
                continue
            print("*", end="")
            continue
        print(S_list[row][column], end="")
    print("")


































# N = int(input())
# S_list = [list(input()) for _ in range(N)]

# temp = []
# for S in S_list:
#     temp.append(len(S))

# max_len = max(temp)

# for column in range(max_len):
#     for row in range(N - 1, -1, -1):
#         if column < len(S_list[row]):
#             print(S_list[row][column], end="")
#         else:
#             if column == max_len - 1:
#                 for i in range(N - 1, row + 1, -1):
#                     if temp[i] > temp[row]:
#                         print("*", end="")
#                     else:
#                         print(" ", end="")
#             else:
#                 print("*", end="")
#     print("")
