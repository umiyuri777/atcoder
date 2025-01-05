N, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

CHEESE_LIKE = 0
CHEESE_WEIGHT = 1

sorted_cheese = sorted(cheese, key=lambda x: x[0], reverse=True)

like_sum = 0

for cheese in sorted_cheese:
    if W >= cheese[CHEESE_WEIGHT]:
        W -= cheese[CHEESE_WEIGHT]
        like_sum += cheese[CHEESE_LIKE] * cheese[CHEESE_WEIGHT]
    else:
        like_sum += W * cheese[CHEESE_LIKE]
        break

print(like_sum)