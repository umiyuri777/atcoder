N = int(input())
D = list(map(int, input().split()))

count = 0

for idx in range(N):
    month = idx + 1
    max_day = D[idx]
    
    for day in range(1, max_day + 1):
        char_kind = set(str(month) + str(day))

        if len(char_kind) == 1:
            count += 1
            print(f"{month}月{day}日")

print(count)