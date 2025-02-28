from collections import defaultdict
N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]

d = []

# 辞書に面の種類と個数を登録
for row in dice:
    tmp = defaultdict(int)
    for column in range(1, row[0] + 1):
        tmp[row[column]] += 1
    d.append((row[0], tmp))

ans = 0

# 全ての組み合わせで試す
for i in range(N - 1):
    for j in range(i + 1, N):
        
        i_len = d[i][0]
        j_len = d[j][0]
        
        i_dict = d[i][1]
        j_dict = d[j][1]
        
        probability = 0
        if len(i_dict) > len(j_dict):
            for current_key, j_value in j_dict.items():
                if current_key in i_dict:
                    i_value = i_dict[current_key]
                    probability += i_value / i_len * j_value / j_len
            ans = max(ans, probability)
        else:
            for current_key, i_value in i_dict.items():
                if current_key in j_dict:
                    j_value = j_dict[current_key]
                    probability += i_value / i_len * j_value / j_len
            ans = max(ans, probability)
            
print(ans)