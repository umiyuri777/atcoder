S = list(input())

count_flag =False

count = 0
ans = []
for char in S:
    if char == "|":
        if count_flag == False:
            count_flag = True 
        else:
            ans.append(count)
            count = 0
    else:
        if count_flag == True:
            count += 1
print(*ans)