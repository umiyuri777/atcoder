N = int(input())
S = input()

one  = 0
two = 0

for i in range(len(S) // 2):

    if S[i] == "1":
        one += 1
    else:
        print("No")
        exit()

if S[len(S) // 2] != "/":
    print("No")
    exit()

for j in range((len(S) // 2 + 1), len(S)):
    if S[j] == "2":
        two += 1
    else:
        print("No")

        exit()

if one == two:
    print("Yes")
else:
    print("No")