N, T = map(int, input().split())
A = list(map(int, input().split()))

row = [set() for _ in range(N)]
column = [set() for _ in range(N)]

slash = set()
backslash = set()

for n in range(N):
    slash.add(1 + (N + 1) * n)
    backslash.add(N + (N - 1) * n)

for i in range(T):
    # 横の列
    row[(A[i] - 1) // N].add(A[i])
    if len(row[(A[i] - 1) // N]) == N:
        print(i + 1)
        exit()
    
    # 縦の列
    column[(A[i] - 1) % N].add(A[i])
    if len(column[(A[i] - 1) % N]) == N:
        print(i + 1)
        exit()
        
    # 斜めの列
    if A[i] in slash:
        slash.remove(A[i])
        if len(slash) == 0:
            print(i + 1)
            exit()
    if A[i] in backslash:
        backslash.remove(A[i])
        if len(backslash) == 0:
            print(i + 1)
            exit()

print(-1)