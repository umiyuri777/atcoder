H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
S = [list(input()) for _ in range(W)]

rs -= 1
cs -= 1
rt -= 1
ct -= 1

x = rs
y = cs

while True:
    