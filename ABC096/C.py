h, w = map(int,input().split())
s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            check = 0
            for x, y in ([1,0],[0,1],[0,-1],[-1,0]):
                new_h, new_w = i + x, j + y
                #print(new_h,new_w)
                if new_h < 0 or new_h >= h or new_w < 0 or new_w >= w:
                    continue
                if s[new_h][new_w] == '.':
                    check += 1
            if check == 4: #4方向に黒がない
                print('No')
                quit()
print('Yes')