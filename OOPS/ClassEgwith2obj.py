#write a program to create a class for an employee - with data - emp id , emp name , emp  dept and create function to display the data with 2 objects

class Employee:
    empId = 201
    empName = "Ravi"
    empDept = "IT"
    def displayemployeedetails(self):
        print(self.empId)
        print(self.empName)
        print(self.empDept)
e1 = Employee()
e1.displayemployeedetails()
e2 = Employee()
e2.empId = 202
e2.empName = "Tina"
e2.empDept = "Finance"
e2.displayemployeedetails()