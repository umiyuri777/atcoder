N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

include = True

count = 0

while include:
    setA = set(A)
    if len(setA) == M:
        include = False
    else:
        A.pop()
        count += 1
print(count)