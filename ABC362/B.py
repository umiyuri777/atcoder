xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

AB2 = (xA - xB)**2 + (yA - yB)**2
BC2 = (xC - xB)**2 + (yC - yB)**2
CA2 = (xA - xC)**2 + (yA - yC)**2

if AB2 + BC2 == CA2 or AB2 + CA2 == BC2 or CA2 + BC2 == AB2:
    print("Yes")
else:
    print("No")

