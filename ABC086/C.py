N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

current_x = 0
current_y = 0

current_t = 0

for t, x, y in G:
    step = t - current_t
    distance = abs(current_x - x) + abs(current_y - y)
    if step < distance or abs(distance - step) % 2 != 0:
        print("No")
        exit()
    current_x = x
    current_y = y
    current_t = t
print("Yes")