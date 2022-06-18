#                                           Outer class
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
#                                           Inner class
    class Laptop:
        def __init__(self):
            self.brand = "DELL"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('ranganadh', 31)
s2 = Student('aditya', 37)
s1.show()

#lap1 = s1.lap
#lap2 = s2.lap
#print(id(lap1))
#print(id(lap2))
