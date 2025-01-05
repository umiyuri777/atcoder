X = int(input())

sum = 0

for i in range(1, 10):
    for j in range(1, 10):
        if i * j != X:
            sum += i * j
print(sum)
    