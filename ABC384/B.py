N, rating = map(int, input().split())

div = [list(map(int, input().split())) for _  in range(N)]



for idx in range(N):
    if div[idx][0] == 1:
        if 1600 <= rating <= 2799:
            rating += div[idx][1]
    else:
        if 1200 <= rating <= 2399:
            rating += div[idx][1]
            
print(rating)