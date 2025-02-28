from collections import defaultdict, deque

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

dependence_num = dict()
dependenced_node = defaultdict(list)

for i in range(V):
    dependence_num[i] = 0

for e in edges:
    dependenced_node[e[0]].append(e[1])
    dependence_num[e[1]] += 1

task = deque()
ans = []
for key, value in dependence_num.items():
    if value == 0:
        task.append(key)
        ans.append(key)

while len(task) > 0:
    current_task = task.popleft()
    for d in dependenced_node[current_task]:
        dependence_num[d] -= 1
        if dependence_num[d] == 0:
            task.append(d)
            ans.append(d)

for i in ans:
    print(i)