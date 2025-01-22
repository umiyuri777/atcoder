"""

式変形していったら答え出る
L <= A + kM <= R

(L-A)//M <= k <= (R-A)//M

確かに〜〜〜〜〜
"""


A, M, L, R = map(int, input().split())

L -= A
R -= A

print(R//M - (L - 1)//M)