# 一回しか配列は全部見れない
# みてる配列の中にある石がいいっこになるように右にずらしていく
# 右にずらせる石がなくなったら終わり

N, M = map(int, input().split())

X = list(map(int, input().split()))
A = list(map(int, input().split()))

X, A = zip(*sorted(zip(X, A)))


if X[0] != 1:
    print(-1)
    exit()

count = 0

stock = 0

current_stones = 0
visited_stoneBox = 0

for i in range(M):
    temp = stock
    stock += A[i]

    if i > 0:
        if temp < X[i] - X[i - 1]:
            print(-1)
            exit()

        t = range(temp - 1, -1, -1)

        for j in range(X[i] - X[i - 1]):
            count += t[j]
        stock -= X[i] - X[i - 1]

if (N - X[-1]) > stock:
    print(-1)
    exit()

t = range(stock - 1, -1 , -1)
for i in range(N - X[-1]):
    count += t[i]

print(count)
