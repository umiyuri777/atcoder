import math
N = int(input())

for p in range(1, min(N+1, 10**6 + 1)):
    if N % p != 0:
        continue
    q = N // p
    if p ** 2 >= q:
        continue
    if (q - p ** 2) % 3 != 0:
        continue
    x_multi_y = (q - p ** 2) // 3
    x_minus_y = p
    x_plus_y_2 = p ** 2 + 4 * x_multi_y
    x_plus_y = math.sqrt(x_plus_y_2)
    if not x_plus_y.is_integer():
        continue

    x = int((x_plus_y + x_minus_y) // 2)
    y = int((x_plus_y - x_minus_y) // 2)
    print(f"{x} {y}")
    exit()
print(-1)