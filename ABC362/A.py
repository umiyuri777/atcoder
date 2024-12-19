RGB = list(map(int, input().split()))

kirai = input()

if kirai == "Red":
    RGB.pop(0)
elif kirai == "Green":
    RGB.pop(1)
else:
    RGB.pop(2)

print(min(RGB))