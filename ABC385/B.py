H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = list(input())

ans = 0

visited_home = set()

for t in T:
    if t == "U":
        if S[X - 1 - 1][Y - 1] == ".":
            X -= 1
        elif S[X - 1 - 1][Y - 1] == "@":
            if (X - 1, Y) not in visited_home:
                ans += 1
                visited_home.add((X - 1, Y))
            X -= 1
        
    if t == "D":
        if S[X - 1 + 1][Y - 1] == ".":
            X += 1
        elif S[X - 1 + 1][Y - 1] == "@":
            if (X + 1, Y) not in visited_home:
                ans += 1
                visited_home.add((X + 1, Y))
            X += 1
        
    if t == "L":
        if S[X - 1][Y - 1 - 1] == ".":
            Y -= 1
        elif S[X - 1][Y - 1 - 1] == "@":
            if (X, Y - 1) not in visited_home:
                ans += 1
                visited_home.add((X, Y - 1))
            Y -= 1
        
    if t == "R":
        if S[X  - 1][Y - 1 + 1] == ".":
            Y += 1
        elif S[X - 1][Y - 1 + 1] == "@":
            if (X, Y + 1) not in visited_home:
                ans += 1
                visited_home.add((X, Y + 1))
            Y += 1
print(X, Y, ans)