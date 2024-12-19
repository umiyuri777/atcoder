points = list(map(int, input().split()))

N = len(points)
ploblem_name = ["A", "B", "C", "D", "E"]


get_points = []
solved_problems = []

ans_list = []


for bit in range(2**N):  # 1 << (N-1) は 2^(N-1) と同じ
    get_point = 0
    solved_problem = ""
    
    for i in range(N):  # どこにbitが立ってるかを確認していく
        if bit & (1 << i):  # 下からi番目にbitが立っているとき
            get_point += points[i]
            solved_problem += ploblem_name[i]

    ans_list.append([get_point, solved_problem])
    # get_points.append(get_point)
    # solved_problems.append(solved_problem)
    
sorted_ans = sorted(ans_list, key=lambda i: (-i[0], i[1]), reverse=True)


for i in range(31, -1, -1):
    print(sorted_ans[i][1])
# zip_list = zip(get_points, solved_problems)
# zip_sort = sorted(zip_list, reverse=True)
# sorted_get_points, sorted_solved_problems = zip(*zip_sort)

# for i in sorted_solved_problems:
#     print(i)