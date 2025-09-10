from collections import deque
N, Q = map(int, input().split())

A = deque()
for i in range(1, N + 1):
    A.append(i)

ptr = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        p = query[1]
        x = query[2]
        
        A[ - 1] = x
        
    elif query[0] == 2:
        p = query[1]
        print(A[p - 1])
        
    else:
        k = query[1]
        ptr = (ptr + k) % N
    print("A: ", A)
    print("ptr: ", ptr)