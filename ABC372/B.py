# N進法への変換を行えばいい

# 入力
M = int(input())

# Aのリスト
A = []

for i in range(11):
    M, mo = divmod(M, 3)

    for _ in range(mo):
        A.append(i)

print(len(A))
print(*A)
