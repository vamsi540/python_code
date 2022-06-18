#--------------------------------------duck typing
#class PyCharam():
#    def execute(self):
#        print("compiling")
#        print("running")
#class MyEditor:
#    def execute(self):
#        print("spell check")
#        print("convention check")
#        print("compiling")
#        print("running")
#class Laptop:
#    def code(self, ide):
#        ide.execute()
#ide = MyEditor()
#lap1  =Laptop()
#lap1.code(ide)

#-----------------------------------------operator overloading
#a = '5'
#b = '6'
#print(a + b)
#print(add.__add__(a,b))
#print(str.__add__(a,b))

#class Student:
#    def __init__(self,m1,m2):
#        self.m1 = m1
#        self.m2 = m2
#    def __add__(self,other):
#        m1 = self.m1 + other.m1
#        m2 = self.m2 + other.m2
#        s3 = Student(m1,m2)
#        return s3
#    def __gt__(self, other):
#        r1 = self.m1 + other.m1
#        r2 = self.m2 + other.m2
#       if r1 > r2:
#            return True
#       else:
#            return False
#--------------------------------to print the values in string
#    def __str__(self):
#        return '{} {}'.format(self.m1, self.m2)
#s1 = Student(88,69)
#s2 = Student(69,65)
#s3 = s1 + s2
#if s1 > s2:
#    print("s1 wins")
#else:
#    print("s2 wins")
#a = 9
#print(a.__str__())
#print(s1)

#-------------------------------------------method overloading
#class Student:
#    def __init__(self,m1,m2):
#        self.m1 = m1
#        self.m2 = m2
#    def sum(self,a=None,b=None,c=None):
#        s = 0
#        if a!=None and b!=None and c!=None:
#            s = a + b + c
#        elif a!=None and b!=None:
#            s = a + b
#        else:
#            s = a
#        return s
#s1 = Student(58,69)
#print(s1.sum(5))

#--------------------------------------------method overriding
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")
a1 = B()
a1.show()