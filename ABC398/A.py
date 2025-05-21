N = int(input())

if N % 2 == 0:
    ans = "-" * (N // 2 - 1) + "==" + "-" * (N // 2 - 1)
else:
    ans = "-" * (N // 2) + "=" + "-" * (N // 2)
print(ans)