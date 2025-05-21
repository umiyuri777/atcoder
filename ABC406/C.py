from collections import defaultdict

N = int(input())
P = list(map(int, input().split()))

count = 0

isNakama = defaultdict(int)
isHazure = defaultdict(int)

for left in range(N):
    if left > 0 and left + 1 < N:
        print(isNakama)
        if isNakama[(P[left - 1], P[left], P[left + 1])] > 0:
            isNakama[(P[left - 1], P[left], P[left + 1])] -= 1
            
            print((P[left - 1], P[left], P[left + 1]))
            if isNakama[(P[left - 1], P[left], P[left + 1])] == 0:
                del isNakama[(P[left - 1], P[left], P[left + 1])]

        if isHazure[(P[left - 1], P[left], P[left + 1])] > 0:
            isHazure[(P[left - 1], P[left], P[left + 1])] -= 1
            
            if isHazure[(P[left - 1], P[left], P[left + 1])] == 0:
                del isHazure[(P[left - 1], P[left], P[left + 1])]
            
    for right in range(left + 2, N):
        if P[left] >= P[left + 1]:
            continue

        if P[right - 2] < P[right - 1] > P[right]:
            isNakama[(P[right - 2], P[right - 1], P[right])] += 1

        if P[right - 2] > P[right - 1] < P[right]:
            isHazure[(P[right - 2], P[right - 1], P[right])] += 1

        if len(isNakama) == 1 and len(isHazure) == 1:
            count += 1
        #     print("left: ", left)
        #     print("right: ", right)
        #     print("isNakama: ", isNakama)
        #     print("isHazure: ", isHazure)
        # if left == 1 and right == 5:
        #     print("left: ", left)
        #     print("right: ", right)
        #     print("isNakama: ", isNakama)
        #     print("isHazure: ", isHazure)
            

print(count)