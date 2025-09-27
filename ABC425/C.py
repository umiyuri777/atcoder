import itertools



N, Q = map(int, input().split())

A = list(map(int, input().split()))

pop_count = 0

prefix_sum = list(itertools.accumulate(A))

# print(prefix_sum)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        pop_count += c
    
    if query[0] == 2:
        l, r = query[1] - 1, query[2] - 1 
        fixed_l = (l + pop_count) % N
        fixed_r = (r + pop_count) % N
        
        # print("pop_count: ", pop_count)
        # print("fixed_l, fixed_r: ", fixed_l, fixed_r)
        
        # 一周まわっちゃった時
        if fixed_r < fixed_l:
            result = (prefix_sum[N - 1] - prefix_sum[fixed_l - 1]) + prefix_sum[fixed_r]
        else:
            if fixed_l == 0:
                result = prefix_sum[fixed_r]
            else:
                result = prefix_sum[fixed_r] - prefix_sum[fixed_l - 1]
        print(result)