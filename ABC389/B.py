X = int(input())

num = 2
while True:
    count = num
    ans = 1
    
    while count > 0:
        ans *= count
        count -= 1
    if ans == X:
        print(num)
        exit()
    num += 1