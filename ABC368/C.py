N = int(input())
H = list(map(int, input().split()))

count = 0

for i in H:
    count += (i // 5) * 3
    i -= (i // 5) * 5

    while i > 0:
        count += 1
        if count % 3 == 0:
            i -= 3
        else:
            i -=1

print(count)