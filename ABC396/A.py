N = int(input())
A = list(map(int, input().split()))

for i in range(0, N - 2):
    tmp = set(A[i:i + 3])

    if len(tmp) == 1:
        print("Yes")
        exit()
print("No")