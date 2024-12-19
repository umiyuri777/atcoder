N = int(input())
A = list(map(int, input().split()))

sorted_A = A[:]
sorted_A.sort(reverse=True)

second_max_num = sorted_A[1]
for idx, a in enumerate(A):
    if a == second_max_num:
        print(idx + 1)
