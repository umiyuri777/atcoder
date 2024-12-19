Q = int(input())
querys = [list(map(int, input().split())) for _ in range(Q)]

stock = {}

for q in querys:
    if q[0] == 1:
        if q[1] in stock.keys():
            stock[q[1]] += 1
        else:
            stock[q[1]] = 1
    if q[0] == 2:
        stock[q[1]] -= 1
        if stock[q[1]] == 0:
            stock.pop(q[1])
    if q[0] == 3:
        print(len(stock))