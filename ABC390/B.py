N = int(input())
A = list(map(int, input().split()))

for idx in range(N - 1):
    if A[idx + 1] * A[0] != A[idx] * A[1]:
        print("No")
        exit()
print("Yes")