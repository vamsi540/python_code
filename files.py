#------------------------for opening the file
#f = open('MyData', 'r')
#------------------used to read all the data in file
#print(f.read())
#------------------used to read a single line from file
#print(f.readline(), end="")
#------------------it is used to print only 4 characters
#print(f.readline(4))

#f1 = open('abc','w')
#---------------------it is used to write into the file
#--in write we can only write what we want the data will not be saved
#f1.write("something")

#--when we want to add anything with previous one then we will use append
#f1 = open('abc','a')
#f1.write('mobile')

#--------------to write the data from f to f1
#for data in f:
#    f1.write(data)

#-------------image copying
#------------------------rb is used read the image in binary format
f = open('image.JPG','rb')

f1 = open('other.JPG', 'wb')

for i in f:
    f1.write(i)
