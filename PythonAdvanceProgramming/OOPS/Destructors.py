#destructors - when we want to destroy the object
#pos conditions - closing of the browser
#clen up operation
#for proper memory usage destructor should be used
#when db connection has to be closed
#free the memory (garbage collection) which is automatically called
#Destructor runs when program ends or object is garbage-collected.


class Desct:
    def __init__(self):
        print("Object created ")
    def __del__(self):
        print("Closing the db connection")

a=Desct()
print("End of the program")
del a
#desct in file handaling
class FileHandler:
    def __init__(self,filename):
        self.file = open(filename , 'w')
        print("File is opened")
    def readFile(self, filename):
        print("Reading the file")
    def __del__(self):
        self.file.close()
        print("File closed")
f=FileHandler("test.txt")
f.readFile("test.txt")
del f









