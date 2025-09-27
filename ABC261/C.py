N = int(input())

S_dict = dict()

for _ in range(N):
    S = input()
    
    if S in S_dict:
        print(S + f"({S_dict[S]})")
        S_dict[S] += 1
    else:
        S_dict[S] = 1
        print(S)