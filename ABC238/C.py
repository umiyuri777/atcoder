N = int(input())

tochuu_sum = sum(range(1, 11))

ans = 0

if N  < 10:
    ans = sum(range(1, N + 1))
else:
    ans = sum(range(1, 10))
    
    print("ans_1~9:", ans)
    
    # 端数を切り出し
    str_n = str(N)
    hasuu = int(str_n[-1])
    
    # 中間の和の計算
    tochuu_end = N - (hasuu + 1)
    digitnum = int(str(tochuu_end)[0])
    print("digitnum: ", digitnum)
    ans += tochuu_sum * digitnum
    print("ans_tochuu:", ans)
    
    # 端数の和の計算
    ans += sum(range(1, hasuu + 2))
    print("ans_hasuu:", ans)
print(ans)