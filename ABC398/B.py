from collections import Counter

A = map(int, input().split())

C = Counter(A)

over_Triple_num = 0

double_num = 0

for v in C.values():
    if v >= 3:
        over_Triple_num += 1
    if v == 2:
        double_num += 1

if over_Triple_num == 1 and double_num >= 1:
    print("Yes")
elif over_Triple_num >= 2:
    print("Yes")
else:
    print("No")
