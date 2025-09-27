
N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

counted_num = set()
not_counted_num = list(range(1, N + 1))

for i in range(N):
    if A[i] != -1 and A[i] in counted_num:
        print("No")
        exit()
    counted_num.add(A[i])

    ans[i] = A[i]
    if A[i] != -1:
        not_counted_num.remove(A[i])

# print("not_counted_num: ", not_counted_num)
# print("ans: ", ans)
for i in range(len(ans)):
    if ans[i] == -1:
        ans[i] = not_counted_num.pop()

print("Yes")
print(*ans)