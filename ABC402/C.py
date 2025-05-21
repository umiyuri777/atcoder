N, M = map(int, input().split())


ng_food = []
manu = []
food_list = [[] for _ in range(N + 1)]

ans = 0

for i in range(M):
    k, *arg = list(map(int, input().split()))
    ng_food.append(k)
    manu.append(arg)
    for a_i in arg:
        food_list[a_i].append(i)

B = list(map(int, input().split()))

for b in B:
    for i in food_list[b]:
        ng_food[i] -= 1
        if ng_food[i] == 0:
            ans += 1
    print(ans)
