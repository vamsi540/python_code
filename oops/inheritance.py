#-------single inheritance
#class Parent:
#    def fun1(self):
#        print("this is a parent class")
#class Child(Parent):
#    def fun2(self):
#        print("this is a child class")
#obj = Child()
#obj.fun1()
#obj.fun2()

#------------multilevel
#class Parent:
#    def fun1(self):
#        print("this is a parent class")
#class Child(Parent):
#    def fun2(self):
#       print("this is a child class")
#class GrandChild(Child):
#    def fun3(self):
#        print("this is a grand child class")
#obj = GrandChild()
#obj.fun1()
#obj.fun2()
#obj.fun3()

#------------hierarchical
#class Parent:
#    def fun1(self):
#        print("this is a parent class")
#class Child1(Parent):
#    def fun2(self):
#        print("this is a child1 class")
#class Child2(Parent):
#    def fun3(self):
#        print("this is a child2 class")
#obj = Child2()
#obj.fun1()
#obj.fun2()
#obj.fun3()

#--------------multiple
#class Father:
#    def fun1(self):
#        print("this is a father class")
#class Mother:
#    def fun2(self):
#        print("this is a mother class")
#class Child(Father, Mother):
#    def fun3(self):
#        print("this is a child class")
#obj = Child()
#obj.fun1()
#obj.fun2()
#obj.fun3()

#--------------------super
class A:
    def __init__(self):
        print("this is class A")
    def fun1(self):
        print("this is father class")
class B(A):
    def __init__(self):
        print("this is class B")
        super().__init__()
    def fun2(self):
        print("this is a mother class")
obj = B()