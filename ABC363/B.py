N, T, P = map(int, input().split())

L = list(map(int, input().split()))


day_count = 0

while True:
    people_count = 0
    for idx in range(N):
        if L[idx] >= T:
            people_count += 1
        L[idx] += 1 
    if people_count >= P:
        print(day_count)
        exit()
    day_count += 1
