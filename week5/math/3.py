import math
n = int(input("Number of sides: "))
a = int(input("length: "))
h = a/(2*math.tan(math.pi/n))
p = a*n
print(round(h * p / 2))