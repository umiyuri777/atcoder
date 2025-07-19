S = input()
T = set(input())

for idx in range(1, len(S)):
    if S[idx].isupper():
        if S[idx - 1] not in T:
            print("No")
            exit()
            
print("Yes")