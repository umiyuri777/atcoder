N = int(input())
P = list(map(int, input().split()))

r = 1

max_num = 0

ans = [0] * N

set_p = set(P)
sorted_p = sorted(set_p, reverse=True)
for max_p in sorted_p:
    temp = 0
    for i in range(N):
        if P[i] == max_p:
            ans[i] = r
            temp += 1
    r += temp
for m in ans:
    print(m)
