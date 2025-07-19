N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]

count = 0

for a, b in task:
    if a < b:
        count += 1
        
print(count)