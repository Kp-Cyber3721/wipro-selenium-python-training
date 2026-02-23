#variables - used to store the data
#instance cariable - global variables at class level
#local variable - inside the method only

#instance variable example
class Student:
    school ="St Joseph Convent"
    def __init__(self,name ,marks):
        self.name = name #instance variable or global variable
        self.marks = marks # instance variable or global variable

    def show(self):
        schoolcity = "Banglore" #Local variable - scope is inside method
        print(self.name,self.marks)
        print(schoolcity)
        print(self.school)
s1 = Student("Harsha", 85)
s2 = Student("Amit", 90)
s1.show()
s2.show()

