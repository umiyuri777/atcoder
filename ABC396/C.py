N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

row_B = 0
row_W = 0

ans = 0

while row_B < len(B) and B[row_B] >= 0:
    ans += B[row_B]
    row_B += 1

while row_W < len(W) and W[row_W] >= 0 and row_W < row_B:
    ans += W[row_W]
    row_W += 1
    
while row_B < len(B) and row_W < len(W):
    if B[row_B] + W[row_W] > 0:
        ans += B[row_B] + W[row_W]
        row_B += 1
        row_W += 1
    else:
        break
print(ans)
