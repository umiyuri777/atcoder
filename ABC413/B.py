N = int(input())
S = [input() for _ in range(N)]

combination = set()

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        combination.add(S[i] + S[j])

print(len(combination))
