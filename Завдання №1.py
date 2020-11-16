import math

print("Enter point A: ")
x1 = float(input())
y1 = float(input())

print("Enter point B: ")
x2 = float(input())
y2 = float(input())

print("Enter point C: ")
x3 = float(input())
y3 = float(input())

AB = float(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
BC = float(math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2))
CA = float(math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2))
print("Side lenghts: {0} {1} {2}\n".format(AB, BC, CA))

p = (AB + BC + CA) / 2
print("0.5 perimetr: {0}\n".format(p))

S = float(math.sqrt(p * (p - AB) * (p - BC) * (p - CA)))
print("Square: {0}".format(S))

