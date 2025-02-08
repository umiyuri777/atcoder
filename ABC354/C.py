N = int(input())

cards = [list(map(int, input().split())) + [i + 1] for i in range(N)]

sorted_cards = sorted(cards, key=lambda x: x[1])

max_power = 0

remain_cards = []

for c in sorted_cards:
    if max_power < c[0]:
        max_power = c[0]
        remain_cards.append(c[2])
sorted_remain_cards = sorted(remain_cards)

print(len(sorted_remain_cards))
print(*sorted_remain_cards)