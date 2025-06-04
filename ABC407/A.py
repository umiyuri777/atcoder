A, B = map(int, input().split())

increment = A // B + 1
decrement = A // B

if abs(increment - A/B) < abs(decrement - A/B):
    print(increment)
else:
    print(decrement)