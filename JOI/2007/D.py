from collections import deque
n = int(input())
m = int(input())

wins_num = [0] * (n + 1)
losing_teams = [[] for _ in range(n + 1)]

for r in range(m):
    winner, loser = map(int, input().split())
    wins_num[winner] += 1
    losing_teams[loser].append(winner)

task = deque()

for i in range(1, n + 1):
    if wins_num[i] == 0:
        task.append(i)

ans = []
enable_dual_ans = 0

if len(task) > 1:
    enable_dual_ans = 1

while len(task) > 0:
    if len(task) > 1:
        enable_dual_ans = 1
    current_task = task.popleft()
    ans.append(current_task)
    for i in losing_teams[current_task]:
        wins_num[i] -= 1
        if wins_num[i] == 0:
            task.append(i)

for i in range(n - 1, -1 , -1):
    print(ans[i])
print(enable_dual_ans)