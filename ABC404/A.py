S = list(input())

S.sort()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in S:
    if i in alphabet:
        alphabet = alphabet.replace(i, "", 1)
if len(alphabet) != 0:
    print(alphabet[0])
else:
    print("None")