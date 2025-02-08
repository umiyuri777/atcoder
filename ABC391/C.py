N, Q = map(int, input().split())

query = [list(map(int, input().split())) for _ in range(Q)]

su_num = [1] * (N + 1)

poppo_loc_dict = {x: x for x in range(N + 1)}

multi_count = 0

for q in query:
    if q[0] == 1:
        before_poppo_loc = poppo_loc_dict[q[1]]
        if su_num[before_poppo_loc] == 2:
            multi_count -= 1
        poppo_loc_dict[q[1]] = q[2]
        su_num[before_poppo_loc] -= 1
        
        if su_num[q[2]] == 1:
            multi_count += 1
        su_num[q[2]] += 1
    else:
        print(multi_count)