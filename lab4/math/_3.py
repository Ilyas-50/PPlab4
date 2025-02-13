import math
ns = int(input("Input number of sides: "))
ls = int(input("Input the length of a side: "))
area = (ns * ls**2) / (4 * math.tan(math.pi / ns))
print("The area of the polygon is: ", int(area))