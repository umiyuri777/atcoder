import math

N = int(input())
M = math.floor(math.log2(N))

ans = 0

for a in range(1, 3):
    max_b = int(math.sqrt(N // (2 ** a)))
    hoge = 0
    ans += max_b

print(ans)