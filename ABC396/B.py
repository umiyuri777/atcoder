Q = int(input())

stack = [0] * 100
for _ in range(Q):
    query = list(map(int, input().split()))

    query_type = query[0]

    if query_type == 1:
        stack.append(query[1])
    else:
        print(stack.pop())