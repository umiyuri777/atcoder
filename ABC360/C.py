N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# AとWをペアにしてソート
paired = sorted(zip(A, W), key=lambda x: (x[0], x[1]))

# ソートされたペアを再度アンパック
A, W = zip(*paired)

