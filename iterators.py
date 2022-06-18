#nums = [2,5,6,9]
#----------------using for loop
#for i in nums:
#    print(i)
#--------nums is list converting it to iterator
#it = iter(nums)

#-------to print the values in iterator we will use __next__
#print(it.__next__())

#--------another way to print the values
#print(next(it))

#-----------------creating own iterator
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
value = TopTen()
print(next(value))

for i in value:
    print(i)