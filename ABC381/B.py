S = input()

omake = [0] * 130

if len(S) % 2 != 0:
    print("No")
    exit()

for k in range(len(S)//2):
    if S[k * 2] != S[k * 2 + 1]:
        print("No")
        exit()
    omake[ord(S[k * 2])] += 2

for j in omake:
    if not(j == 0 or j == 2):
        print("No")
        exit()
print("Yes")
