N = int(input())

a = N // 100
b = N % 100 // 10
c = N % 10

print(b, end="")
print(c, end="")
print(a, end="")

print(" ", end="")

print(c, end="")
print(a, end="")
print(b)