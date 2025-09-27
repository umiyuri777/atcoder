N = int(input())
S = input()
Q = int(input())

alpha = {x: x for x in "abcdefghijklmnopqrstuvwxyz"}

for _ in range(Q):
    c, d = input().split()
    
    for k, v in alpha.items():
        if v == c:
            alpha[k] = d

print("".join(alpha[s] for s in S))