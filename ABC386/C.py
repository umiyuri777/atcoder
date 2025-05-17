K = int(input())
S = input()
T = input()

if len(S) == len(T):
    count = 0
    for idx in range(len(S)):
        if S[idx] != T[idx]:
            count += 1
    if count <= 1:
        print("Yes")
    else:
        print("No")
    exit()

if len(S) > len(T):
    longer = S[:]
    shorter = T[:]
else:
    longer = T[:]
    shorter = S[:]

if len(longer) != len(shorter) + 1:
    print("No")
    exit()
    
Misaligned = False
for idx in range(len(shorter)):
    if Misaligned == False:
        if longer[idx] != shorter[idx]:
            Misaligned = True
    else:
        if longer[idx + 1] != shorter[idx]:
            print("No")
            exit()
print("Yes")