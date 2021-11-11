import math

p1 = input().split(" ")
p2 = input().split(" ")

x1, y1 = p1
x2, y2 = p2

cal = ((round(float(x2),1) - round(float(x1),1)) ** 2) + ((round(float(y2),1) - round(float(y1),1)) ** 2)

print(cal)
distance = round(math.sqrt(cal), 4)

print(str(distance))
