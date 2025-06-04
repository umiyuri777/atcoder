N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if len(set(A)) < M:
        print(i)
        exit()
    A.pop()
print(N)