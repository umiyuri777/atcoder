N = int(input())

R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)


ave_R = (min(R) + max(R)) // 2
ave_C = (min(C) + max(C)) // 2

max_distance_x = 0
max_distance_y = 0

for p in pos:
    x, y = p
    max_distance_x = max(max_distance_x, abs(x - ave_x))
    max_distance_y = max(max_distance_y, abs(y - ave_y))
    
print(max_distance_x + max_distance_y)