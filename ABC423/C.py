N, R = map(int, input().split())
L = list(map(int, input().split()))

left = 0
right = 0

openCount = 0
closeCount = 0

isCount = False

for l in range(R):
    if L[l] == 0:
        isCount = True
        
    if isCount == True:
        if L[l] == 0:
            openCount += 1
        else:
            closeCount += 1

isCount = False

for r in range(N - 1, R - 1 , -1):
    if L[r] == 0:
        isCount = True
        
    if isCount == True:
        if L[r] == 0:
            openCount += 1
        else:
            closeCount += 1
print(openCount + closeCount * 2)