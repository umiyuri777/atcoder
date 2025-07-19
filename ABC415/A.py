N = int(input())
A = set(map(int, input().split()))
X = int(input())


if X in A:
    print("Yes")
else:
    print("No")