N, Q = map(int, input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_min = 9999999
idx_A_min = 0
B_min = 9999999
idx_B_min = 0

for idx in range(N):
    if A_min <= A[idx]:
        A_min = A[idx]
        idx_A_min = idx
        
    if B_min <= B[idx]:
        B_min = B[idx]
        idx_B_min = idx

for _ in range(Q):
    c, X, V = input().split()
    X, V = int(X), int(V)
    
    if c == "A":
        
    elif c == "B":
        