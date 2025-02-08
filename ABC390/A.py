import copy

A = list(map(int, input().split()))

sorted_A = [1, 2, 3 ,4, 5]

flag = True
for i in range(4):
    l = copy.deepcopy(A)
    l[i], l[i + 1] = l[i + 1], l[i]
    if l == sorted_A:
        print("Yes")
        exit()
print("No")
