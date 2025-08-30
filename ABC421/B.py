X, Y = map(int, input().split())

def fibonacci_reversed(i):
    if i == 1:
        return X
    elif i == 2:
        return Y
    
    temp = str(fibonacci_reversed(i - 1) + fibonacci_reversed(i - 2))
    reversed_temp = temp[::-1]
    return int(reversed_temp)

print(int(fibonacci_reversed(10)))