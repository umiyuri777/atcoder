
N = int(input())
S = list(input())

posA = [i for i, ch in enumerate(S) if ch == 'A']


# A をインデックス 0,2,4,... に揃えるコスト
cost_start_A = sum(abs(posA[i] - (2 * i)) for i in range(N))
# A をインデックス 1,3,5,... に揃えるコスト
cost_start_B = sum(abs(posA[i] - (2 * i + 1)) for i in range(N))

print(min(cost_start_A, cost_start_B))

