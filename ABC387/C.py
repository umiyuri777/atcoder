def count_hebi_num(num):
    str_num = str(num)
    
    ans = 0
    
    # 9回
    # 最上位桁でならす
    tmp = []
    for i in range(1, len(str_num)):
        if str_num[0] > str_num[i]:
            tmp.append(int(str_num[i]) + 1)
        else:
            tmp.append(int(str_num[0]))

    omake = 1
    for t in tmp:
        omake *= t
    ans += omake
    print("omake: ", omake)

    # 8回
    # 桁を一つ下げる
    for i in range(1, int(str_num[0])):
        ans += i ** (len(str_num) - 1)
    print("kapooo: ", ans)
    # 10までの蛇数数える
    for keta in range(len(str_num) - 2, 0, -1):
        for i in range(1, 10):
            ans += i ** keta
    print("ans: ", ans)
    return ans



L, R = map(int, input().split())

max_num = count_hebi_num(R)
min_num = count_hebi_num(L - 1)

print(max_num - min_num)