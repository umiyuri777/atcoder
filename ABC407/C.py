S = list(input())
S.reverse()

count = 0


for s in S:
    prev = count % 10
    
    if int(s) == 0 and prev != 0:
        s = 10
    
    if int(s) < prev:
        # 前のボタンより小さい場合は、9を足す
        current_buttonB = int(s) + 10 - prev
    else:
        # 前のボタンより大きい場合は、単純に引き算
        current_buttonB = int(s) - prev
        
    count += current_buttonB

# 桁数足す
count += len(S)

print(count)
