# BFSで解ける
from collections import deque

T = int(input())

for nnn in range(T):
    N = int(input())
    S = "0" + input()
    
    queue = deque()
    queue.append(0)
    
    visited = set()
    visited.add(0)
    
    found = False
    
    while queue:
        current_state = queue.popleft()
        for i in range(N):
            new_state = current_state | 1 << i
            if new_state >= len(S):
                continue
            
            if S[new_state] == "0" and new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
                if new_state == 2 ** N - 1:
                    found = True
    if found:
        print("Yes")
    else:
        print("No")
