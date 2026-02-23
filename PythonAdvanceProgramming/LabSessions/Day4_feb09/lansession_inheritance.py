#cerate a python program with class name savings account and functions deposit in parent class  and  add interest in the child class
class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(amount)
        print(self.balance)
class InterestAccount(SavingsAccount):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(interest)
        print(self.balance)
a = InterestAccount(1000)
a.deposit(500)
a.add_interest(5)


#for multi level
class FinalAccount(InterestAccount):
    def show_balance(self):
        print(self.balance)
acc = FinalAccount(1000)
acc.deposit(500)
acc.add_interest(5)
acc.show_balance()

#1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print(c.area())
print(c.perimeter())

#2.Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    def age(self):
        today = date.today()
        return today.year - self.dob.year
p = Person("Ravi", "India", date(2000, 5, 10))
print(p.age())

#3.Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r
class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a
    def perimeter(self):
        return 4 * self.a
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
s = Square(4)
print(s.area(), s.perimeter())

#4.Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def start(self):
        print("Vehicle started")
    def stop(self):
        print("Vehicle stopped")
class Bus(Vehicle):
    pass
b = Bus()
b.start()
b.stop()

#5.Write a python program to create  a Vehicle class without any variables and methods
class Vehicle:
    pass





