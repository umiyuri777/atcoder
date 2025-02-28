N, M = map(int, input().split())

A = list(map(int, input().split()))

A.sort()
index = 1
ans = []
pointer = 0


for i in range(1, N + 1):
    if pointer >= len(A):
        ans.append(i)
        continue
    if i == A[pointer]:
        pointer += 1
    else:
        ans.append(i) 

print(len(ans))
print(*ans)