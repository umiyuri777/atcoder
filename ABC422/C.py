T = int(input())

for _ in range(T):
    nA, nB, nC = map(int, input().split())
    minAC = min(nA, nC)
    average = (nA + nB + nC) // 3
    
    ans = min(minAC, average)
    print(ans)