T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    
    left_s = S[0]
    right_s = S[-1]
    
    count = 2
    
    if left_s * 2 >= right_s:
        print(2)
        continue
    
    remain_s = S[1:-1]
    remain_s.sort()
    
    for idx in range(len(remain_s)):
        
        if (idx == len(remain_s) - 1) or (remain_s[idx] <= left_s * 2 and remain_s[idx + 1] > left_s * 2):
            current_s = remain_s[idx]
            count += 1
        
            if left_s * 2 >= current_s and current_s * 2 >= right_s:
                print(count)
                break
            elif left_s * 2 < current_s:
                print(-1)
                break
            left_s = current_s
    else:
        print(-1)
