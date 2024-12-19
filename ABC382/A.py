N, D = map(int, input().split())
S = list(input())

count = 0

for i in S:
    if i == "@":
        count += 1

print(N - (count - D))