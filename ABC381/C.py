N = int(input())

S = input()

ans = 1

for i in range(N):
    if S[i] != "/":
        continue

    count = 1

    for j in range(1, N // 2 + 1):
        if i - j < 0 or i + j >= N:
            ans = max(ans, count)
            break
        if S[i - j] == "1" and S[i + j] == "2":
            count += 2
            ans = max(ans, count)
        else:
            ans = max(ans, count)
            break

print(ans)
