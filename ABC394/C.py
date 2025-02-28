S = list(input())

for pointer in range(len(S) - 1, -1, -1):
    if pointer > 0:
        if S[pointer - 1] == "W" and S[pointer] == "A":
            S[pointer - 1] = "A"
            S[pointer] = "C"
print("".join(S))