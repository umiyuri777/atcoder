from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# AとWをペアにしてソート
paired = sorted(zip(W, A))

# ソートされたペアを再度アンパック
W, A = zip(*paired)

countDict = defaultdict(int)
for a in A:
    countDict[a] += 1

ans = 0
sum_count = 0

for idx in range(N):
    if countDict[A[idx]] > 1:
        ans += W[idx]
        countDict[A[idx]] -= 1
        sum_count += 1

    if sum_count == N - len(countDict):
        print(ans)
        exit()