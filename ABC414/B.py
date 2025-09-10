N = int(input())

ans = ""

for _ in range(N):
    c, l = input().split()
    
    l = int(l)
    if l > 100:
        print("Too Long")
        exit()
    
    ans += c * int(l)
    
    print("len(ans): ", len(ans))
    if len(ans) > 100:
        print("Too Long")
        exit()
        
print(ans)