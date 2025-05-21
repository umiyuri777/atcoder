N, K = map(int, input().split())

a = [1] * K + [K] + [0] * (N - K)

a_i = K

for i in range(K + 1, N + 1):
    a_i -= a[i - K - 1]
    a_i += a[i - 1]
    a_i %= 10 ** 9
    a[i] = a_i

print(a[N])