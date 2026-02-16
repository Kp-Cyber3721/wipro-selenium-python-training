#class is a blueprint or a template
#which describes the state /  behaviour of its object
#data is put in variables
#behaviour is put in function
class Student:
#data or the properties
    Studentname = "Ravi"
    StudentID = 677887
#self is used to access the attribute of the class we have defined
#it is automatically loaded
#self represents the instance of the class
#create a function to access the data
    def displaystudentdetails(self):
        print(self.Studentname)
        print(self.StudentID)

#create the object pf the class
a = Student()
a.displaystudentdetails()







