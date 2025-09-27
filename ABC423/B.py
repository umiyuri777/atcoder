N = int(input())
L = list(map(int, input().split()))

front = 0
back = 0

for idx in range(N):
    if L[idx] == 1:
        front = idx
        break

for idx in range(N - 1, -1, -1):
    print(idx)
    if L[idx] == 1:
        back = idx
        break
        
        
print(back - front)
