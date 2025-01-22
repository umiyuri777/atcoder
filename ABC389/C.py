"""
蛇の長さと頭の位置をタプルの配列で保持して、出力する時何m先頭から抜けたか毎回計算する
"""

from collections import deque
Q = int(input())

query = [list(map(int, input().split())) for _ in range(Q)]

hebi_position = deque()

different = 0

for q in query:
    if q[0] == 1:
        if len(hebi_position) == 0:
            hebi_position.append((0, q[1]))
        else:
            hebi_position.append((hebi_position[-1][0] + hebi_position[-1][1], q[1]))
    if q[0] == 2:
        pop_hebi_info = hebi_position.popleft()
        different += pop_hebi_info[1]
    if q[0] == 3:
        print(hebi_position[q[1] - 1][0] - different)
    # print(hebi_position)
