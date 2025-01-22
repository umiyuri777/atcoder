import math

R = int(input())
r2 = R*R

def max_j_for_i(i):
    # (i+0.5)^2 + (j+0.5)^2 <= R^2
    # j+0.5 <= sqrt(R^2 - (i+0.5)^2)
    limit = math.sqrt(r2 - (i+0.5)**2) - 0.5
    return max(0, int(math.floor(limit)))

# 第1象限 (i>0,j>0)
cnt_q = 0
for i in range(1, R+1):
    if (i+0.5)**2 > r2: 
        break
    cnt_q += max_j_for_i(i)

# 軸 (i=0, j>0)
limit_j = int(math.floor(math.sqrt(r2 - 0.25) - 0.5))
cnt_axis_j = max(0, limit_j)

# 軸 (i>0, j=0)
limit_i = int(math.floor(math.sqrt(r2 - 0.25) - 0.5))
cnt_axis_i = max(0, limit_i)

# 原点 (0,0)
cnt_origin = 1 if (0.5**2 + 0.5**2) <= r2 else 0

ans = 4*cnt_q + 2*cnt_axis_j + 2*cnt_axis_i + cnt_origin
print(ans)