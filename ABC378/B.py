
"""
<方針>
- `d` を `q` で割ってみる．
  - 余りが `r` であった時， `d` が答え．
  - 余りが `r` より小さい時，余りを省いた分と `r` の和が答え．
  - 余りが `r` より大きい時，余りを省いた分と `q` と `r` の和が答え．
"""

N = int(input())
rules = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
gomi = [list(map(int, input().split())) for _ in range(Q)]

for g in gomi:
    t, d = g
    t -= 1

    q, r = rules[t]

    di, mo = divmod(d, q)

    ans = 0

    if mo == r:
        ans = d
    elif mo < r:
        ans = di * q + r
    elif mo > r:
        ans = di*q + q + r
    
    print(ans)
