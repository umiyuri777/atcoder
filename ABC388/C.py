N = int(input())
A = list(map(int, input().split()))

def isOK(index, key, data):
    return data[index] // 2 >= key

def meguru_bisect(key, data):
    ng = -1
    ok = len(data)
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isOK(mid, key, data):
            ok = mid
        else:
            ng = mid
    return ok

ans = 0

for a in A:
    ans += len(A) - meguru_bisect(a, A)

print(ans)