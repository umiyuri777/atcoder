"""
Aの方法をとる回数を決め打ちしてしまって全探索し、Bの方法をとらなければならない回数を数えていく
Sの配列を2連続にしてるのがミソ
"""

N, A, B = map(int, input().split())
S = input()

S += S

ans = 999999999999999

# iがAの方法の回数
# Nは最大5000なので、全探索しても間に合う
for i in range(N):
    temp = A * i
    
    # jはBの回数
    # 対象になる部分を比較して、違ったらansにBの値段だけ足す
    for j in range(N // 2):
        if S[i + j] != S[i + N - 1 - j]:
            temp += B
    ans = min(temp, ans)

print(ans)
