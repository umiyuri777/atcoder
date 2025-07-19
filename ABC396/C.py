# 自前回答
# N, M = map(int, input().split())
# B = list(map(int, input().split()))
# W = list(map(int, input().split()))

# B.sort(reverse=True)
# W.sort(reverse=True)

# row_B = 0
# row_W = 0

# ans = 0

# while row_B < len(B) and B[row_B] >= 0:
#     ans += B[row_B]
#     row_B += 1

# while row_W < len(W) and W[row_W] >= 0 and row_W < row_B:
#     ans += W[row_W]
#     row_W += 1
    
# while row_B < len(B) and row_W < len(W):
#     if B[row_B] + W[row_W] > 0:
#         ans += B[row_B] + W[row_W]
#         row_B += 1
#         row_W += 1
#     else:
#         break
# print(ans)

# 公式回答

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

S, T, maxT = [0] * (N + 1), [0] * (M + 1), [0] * (M + 1)

# S, Tはそこまでとったときの和を格納してる
# maxTは
for i in range(N):
    S[i + 1] = S[i] + A[i]
for i in range(M):
    T[i + 1] = T[i] + B[i]
    maxT[i + 1] = max(maxT[i], T[i + 1])

ans = 0
for i in range(N + 1):
    ans = max(ans, S[i] + maxT[min(i, M)])
print(ans)
