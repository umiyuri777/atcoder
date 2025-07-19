S = input()

ans = []

for idx, s in enumerate(S):
    if s == "#":
        ans.append(idx + 1)
        if len(ans) == 2:
            print(",".join(map(str, ans)))
            ans = []
