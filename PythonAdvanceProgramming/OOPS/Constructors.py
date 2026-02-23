#constructors - first function of the class when an object of the class is created
#syNACT __init__()
#we can parametarized the constructors
#self is mandatory here
#constructor are used for pre conditions
class Student:
    def __init__(self):
        print("Constructor is called")

    def addsum(self):
        print("Adding 2 numbers ")

s1= Student()
s1.addsum()

#parametrized constructor
#self.name is a instance or a global variable(belong to object)
#name is a local parameter(exists inside the method)
#if we dont assign it to the self.name the object will not remember the value


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name,self.salary)

e1= Employee("Harsha",50000)
e2=Employee("Ravi",656776)
e1.display()
e2.display()


#using * args in constructor
class Numbers:
    def __init__(self, * args):
        self.values = args
n= Numbers(10, 20, 30)
print(n.values)

m=Numbers(3,4,5)
print(m.values)

p = Numbers(3)
print(p.values)

#Parent and child constructors
#super keyword for accesing parent constructor

class Parent:
    def __init__(self):
        print("I am the parent constructor")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child1 constructor")

c = Child1()

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child2 constructor")
c= Child2()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print(self.title)
        print(self.author)
b1 = Book("Clean Code", "Robert C. Martin")
b2 = Book("Atomic Habits", "James Clear")
b3 = Book("Think Like a Monk", "Jay Shetty")
b1.display()
b2.display()
b3.display()




class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.area = l * w
        self.perimeter = 2 * (l + w)
    def display(self):
        print(self.area)
        print(self.perimeter)

r1 = Rectangle(40, 20)
r1.display()




