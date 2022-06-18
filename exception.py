a = 6
b = 2
#-------------------try is used for excecuting the program
try:
    #-----------------------to know the excecution
    print("resource open")
    print(a/b)
    k = int(input("enter the number"))
    print(k)
    #----it is for exception occurs when it is divides with 0
except ZeroDivisionError as e:
    print("hey, you cannot divide a number by zero", e)
    #--------------for value error
except ValueError as e:
    print("ivalid input")
    #-----------------for any type of error will handles
except Exception as e:
    print("something went wrong...")
    #--------------------to print any type of msgs we can use
finally:
    print("resource closed")