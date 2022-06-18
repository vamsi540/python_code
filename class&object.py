#class Computer:
#    def config(self):
#        print("i5, 16gb, 1tb")
#com1 = Computer()
#Computer.config(com1)
#com1.config()

# __init__ method

#class Computer:
#    def __init__(self, cpu, ram):
#        self.cpu = cpu
#        self.ram = ram
#    def config(self):
#        print("config is", self.cpu, self.ram)
#com1 = Computer('i5',16)
#com2 = Computer('ryzen',8)
#com1.config()
#com2.config()

# Constructor and Self

#class Computer:
#    def __init__(self):
#        self.name = 'ranganadh'
#        self.age = 23
#    def update(self):
#        self.age = 22
#    def compare(self,other):
#        if self.age == other.age:
#            return True
#        else:
#            return False
#c1 = Computer()
#c2 = Computer()
#c1.name = "priya"
#c1.age = 22
#if c1.compare(c2):
#    print("they are same")
#else:
#    print("they are not same")
#c1.update()
#print(c1.name)
#print(c2.name)

# variables in object

class Car:
    wheels = 3
    def __init__(self):
        self.mil = 10
        self.com = "BMW"
c1 = Car()
c2 = Car()
c1.mil = 12
Car.wheels =4
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)

# different types of methods

