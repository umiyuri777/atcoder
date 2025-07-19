from collections import deque

Q = int(input())

A = deque()  # (value, count)のペアを格納

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        c = query[1]
        x = query[2]
        A.append([c, x])
        
    elif query[0] == 2:
        k = query[1]
        total = 0
        
        
        while k > A[0][0] and len(A) > 0:
            c, x = A[0]
            total += c * x
            
            k -= c
            A.popleft()
        
        total += k * A[0][1]
        A[0][0] -= k
        print(total)