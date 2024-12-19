N = int(input())

binary_N = list(map(str, bin(N)))
binary_N = binary_N[2:len(binary_N)]

ans = []

for b in binary_N:
    ans.append("B")
    if b == "1":
        ans.append("A")
ans.pop(0)
print("".join(ans))
