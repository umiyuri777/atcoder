def plus_count(A : list):
    count = 0
    for i in A:
        if i >= 1:
            count += 1
    return count

N = int(input())

A = list(map(int, input().split()))

count = 0

while True:
    tmp = 0
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    count += 1

    if plus_count(A) <= 1:
        print(count)
        exit()
