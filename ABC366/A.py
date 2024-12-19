N, T, A = map(int, input().split())

if N - (T + A) > abs(T - A):
    print("No")
else:
    print("Yes")