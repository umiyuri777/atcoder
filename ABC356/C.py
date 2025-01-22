N, M, K = map(int, input().split())

tests = [list(map(str, input().split())) for _ in range(M)]

ans = 0


for i in range(2 ** N):
    wrong_case = False
    check_keys = []
    for j in range(N):
        if (i >> j) & 1:
            check_keys.append(str(j + 1))
    if len(check_keys) < K:
        continue

    for test in tests:
        test_keys = test[1:int(test[0]) + 1]
        test_result = test[-1]

        if test_result == "x":
            if all(key in test_keys for key in check_keys) or all(test_key in check_keys for test_key in test_keys):
                wrong_case = True
                break

    if wrong_case == False:
        ans += 1


print(ans)

