N = int(input())

A = list(map(int, input().split()))

ans = 0

while True:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] //= 2
        else:
            print(ans)
            exit()
    ans += 1
