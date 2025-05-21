S = input()

while len(S) > 4:
    if S[-7:] == "dreamer":
        S = S[:len(S) - 7]
    elif S[-6:] == "eraser":
        S = S[:len(S) - 6]
    elif S[-5:] == "dream" or S[-5:] == "erase":
        S = S[:len(S) - 5]
    else:
        print("NO")
        exit()

if len(S) == 0:
    print("YES")
else:
    print("NO")