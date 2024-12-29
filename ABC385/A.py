A, B, C = map(int, input().split())

if A + B == C or A + C == B or A == B + C or A == B == C:
    print("Yes")
else:
    print("No")