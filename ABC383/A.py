N = int(input())

ans = 0

before_time = 0

for i in range(N):
    time, water = map(int, input().split())
    if i == 0:
        ans += water
        before_time = time
    else:
        ans = max(ans - (time - before_time), 0)
        ans += water
        before_time = time
print(ans)