import collections

A = list(map(int, input().split()))

A.sort()

a = collections.Counter(A)

count = 0
for i in a.values():
    count += i // 2

print(count)

