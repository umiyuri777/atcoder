Q = int(input())

from collections import deque

wait = deque()

for _ in range(Q):
    query = input()
    
    if query[0] == "1":
        _, X = map(int, query.split())
        wait.append(X)
    else:
        print(wait.popleft())