N = list(input())

count_1 = 0
count_2 = 0
count_3 = 0

for n in N:
    if n == "1":
        count_1 += 1
    if n == "2":
        count_2 += 1
    if n == "3":
        count_3 += 1

if count_1 == 1 and count_2 == 2 and count_3 == 3:
    print("Yes")
else:
    print("No")