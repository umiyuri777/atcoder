N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

ans = 0

for idx, enemy_hand in enumerate(T):
    if idx - K >= 0:
        if T[idx - K] == enemy_hand:
            T[idx] = "Z"
            continue
    
    if enemy_hand == "r":
        ans += P
    elif enemy_hand == "s":
        ans += R
    elif enemy_hand == "p":
        ans += S
    
print(ans)