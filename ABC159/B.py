S = input()
N = len(S)

if S == S[::-1]:
    temp = S[:(N - 1)//2]

    if temp == temp[::-1]:

        omake = S[(N+3)//2 - 1:]
        if omake == omake[::-1]:
            print("Yes")
            exit()
print("No")