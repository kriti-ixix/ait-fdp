import math
class Student:
    print("hello")
c=Student()
print(c)
class Rect:
    l=0
    b=0
r1=Rect()
print("length=",r1.l)
print("breadth=",r1.b)
print("area=",r1.l*r1.b)
r1.l=10
r1.b=20
print("length=",r1.l)
print("breadth=",r1.b)
print("area=",r1.l*r1.b)
class Circle:
    def area(self,radius):
        print("radius of circle is ",radius)
        return math.pi*radius**2
class B(Circle):
    def abc(self):
        print("b class")
c1=B()
c1.abc()
print("area= ",c1.area(4))  

