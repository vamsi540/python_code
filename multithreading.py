from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()
#----------to print thread we will use this start
t1.start()
sleep(0.2)
t2.start()
#---------her join is used to ask the main thread to join
t1.join()
t2.join()
print("Bye")
