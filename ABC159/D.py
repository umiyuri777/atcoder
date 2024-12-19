
N = int(input())
A = list(map(int, input().split()))

count_a = [0] * 100000000

for i in A:
    count_a[i] += 1

sum = 0
for i in count_a:
    sum += (i * (i - 1)) // 2

for i in A:
    print(sum - (count_a[i] - 1))
