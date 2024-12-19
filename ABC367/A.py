A, B, C = map(int, input().split())

if B < C:
    if B < A < C:
        print("No")
        exit()
    print("Yes")

elif C < B:
    if C < A < B:
        print("Yes")
        exit()
    print("No")


