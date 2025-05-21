N = int(input())

state = "logout"

ans = 0

for i in range(N):
    query = input()
    
    if query == "private" and state == "logout":
        ans += 1
    
    if query == "login" or query == "logout":
        state = query
print(ans)