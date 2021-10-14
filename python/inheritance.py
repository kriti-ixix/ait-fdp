""" single level
class A:
    def Msg1(self):
        print("class a")
class B(A):
    def Msg2(self):
        print("b class")
b1=B()
b1.Msg1()
b1.Msg2()
"""
""" multiple 
class A:
    def Msg1(self):
        print("class a")
class B:
    def Msg2(self):
        print("b class")
class C(A,B):
    def Msg3(self):
        print("c class")
c1=C()
c1.Msg1()
c1.Msg2()
c1.Msg3()
"""
""" multilevel
class A:
    def Msg1(self):
        print("class a")
class B(A):
    def Msg2(self):
        print("b class")
class C(B):
    def Msg3(self):
        print("class c")
c1=C()
c1.Msg1()
c1.Msg2()
c1.Msg3()
"""
class A:
    def msg1(self):
        print("a class")
class B(A):
    def msg2(self):
        print("b class")
class C(A):
    def msg3(self):
        print("c class")
o1=B()
o1.msg1()
o1.msg2()
o2=C()
o2.msg1()
o2.msg3()