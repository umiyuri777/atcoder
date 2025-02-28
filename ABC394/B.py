N = int(input())
S = [input() for _ in range(N)]

li = []
for i in range(N):
    li.append((i, len(S[i])))
    
sorted_li = sorted(li, key=lambda x: x[1])

for i in sorted_li:
    print(S[i[0]], end="")
print()