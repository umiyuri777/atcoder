N, M = map(int, input().split())

conditions = [list(map(int, input().split())) for _ in range(M)]

ans = range(1, N + 1)

ans_index = dict()
