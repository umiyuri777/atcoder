X = input()

ZeroCount = 0
for i in range(1, 4):
    if X[-i] == "0":
        ZeroCount += 1
    else:
        if ZeroCount != 0:
            X = X[:-ZeroCount]
        break
else:
    if ZeroCount != 0:
        X = X[:-ZeroCount]

if X[-1] == ".":
    X = X[:-1]
print(X)

