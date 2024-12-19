N, D = map(int, input().split())
S = list(input())

eat_count = 0

# while eat_count == D:
for i in range(N - 1, -1, -1):
    if S[i] == "@":
        S[i] = "."
        eat_count += 1
    
    if eat_count == D:
        print("".join(S))
        exit()