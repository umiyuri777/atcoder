N, M = map(int, input().split())

ans = 0

guusuu = 0
# N_C_2
if N >= 2:
    guusuu += (N * (N - 1))/2 

kisuu = 0
if M >= 2:
    kisuu += (M * (M - 1))/2 

print(int(guusuu + kisuu))

