N = int(input())
A =  map(int, input().split())

before_a = 0

for a in A:
    if a <= before_a:
        print("No")
        exit()
    before_a = a
print("Yes")