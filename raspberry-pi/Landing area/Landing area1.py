import math


def getArea(p1,p2,p3):
    side1 = (1/2) * \
            abs(
                p1[0]*(p2[1]-(p3[1]))  + 
                p2[0]*(p3[1]-(p1[1]))  + 
                p3[0]*(p1[1]-(p2[1]))
                )
                # In acordance to the area of a triangle formula relative to cordinate geometry
                # https://www.cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/
    return side1
      
p1 = input("First point: ")
p2 = input("second point: ")
p3 = input("third point: ")

l = [p1,p2,p3]
nl = []

for i,point in enumerate(l):
    point = tuple(int(x) for x in point.split(","))
    nl.append(point)





print(f"Area of the triangle is {getArea(nl[0],nl[1],nl[2])}")