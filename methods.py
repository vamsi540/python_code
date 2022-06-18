class Student:
    school = "IIT"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
#                                                 class method
    @classmethod
    def getSchool(cls):
        return cls.school
#                                                 static method
    @staticmethod
    def info():
        print("this is student class....")
#                                                 instance method
#    def get_m1(self):
#        return self.m1
#    def set_m1(self, value):
#        self.m1 = value
s1 = Student(34,67,32)
s2 = Student(89,32,52)
print(s1.avg())
print(Student.getSchool())
Student.info()