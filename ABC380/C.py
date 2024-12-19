N, K = map(int, input().split())
S = input()

mass = []

flag = 2

first = 9999

start_column = 0

for column in range(N):
    # 初回ループだけ
    if flag == 2:
        flag = int(S[column])
        first = int(S[column])

    if flag != int(S[column]):
        mass.append(S[start_column:column])
        flag = int(S[column])
        start_column = column
else:
    mass.append(S[start_column:column + 1])

ans = ""

if first == 0:
    mass[K * 2 - 1], mass[K * 2 - 2] = mass[K * 2 - 2], mass[K * 2 - 1]
else:
    mass[K * 2 - 2], mass[K * 2 - 3] = mass[K * 2 - 3], mass[K * 2 - 2]

print("".join(mass))
