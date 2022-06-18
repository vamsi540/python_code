from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("its running")
class Programmer:
    def work(self,com):
        print("solving bugs")
        com.process()
#com = Computer()
com1 = Laptop()
#com.process()
prog1 = Programmer()
prog1.work(com1)
