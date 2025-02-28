S = list(input())

stack = []

for st in S:
    if st == "(" or st == "[" or st == "<":
        stack.append(st)
    else:
        if len(stack) > 0:
            if stack[-1] == "(" and st == ")" or stack[-1] == "[" and st == "]" or stack[-1] == "<" and st == ">":
                stack.pop()
            else:
                print("No")
                exit()
        else:
            print("No")
            exit()

if len(stack) == 0:
    print("Yes")
else:
    print("No")