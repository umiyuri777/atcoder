N, c1, c2 = map(str, input().split())
S = list(input())


for idx in range(int(N)):
    if S[idx] != c1:
        S[idx] = c2

print("".join(S))