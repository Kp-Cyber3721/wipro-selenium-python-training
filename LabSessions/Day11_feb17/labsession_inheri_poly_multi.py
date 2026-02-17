#Create a Car class with attributes brand, model, price
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print(self.brand, self.model, self.price)
c1 = Car("Tata", "BYE", 30000)
c1.display()

#Create a Student class with method get_grade() based on marks.
class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


s1 = Student(82)
print(s1.get_grade())

#Create a BankAccount class with deposit() and withdraw() methods
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


b1 = BankAccount(1000)
b1.deposit(500)
b1.withdraw(300)
print(b1.balance)

#Write a class Employee that initializes name, id, salary using __init__.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

#Create a class that counts how many objects are created.
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


a = Counter()
b = Counter()
c = Counter()

print("Objects created:", Counter.count)

#Create a class that counts how many objects are created.
class Company:
    company_name = "TechCorp"

    def __init__(self, emp_name):
        self.emp_name = emp_name

#Implement a static method to validate email format.
class Validator:
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


print(Validator.validate_email("test@gmail.com"))


#Inheritance
#Create a base class Vehicle and derived class Bike.
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    def ride(self):
        print("Bike Riding")


b = Bike()
b.start()
b.ride()

#Create Person → Employee → Manager (multilevel inheritance).
class Person:
    def show(self):
        print("I am a Person")

class Employee(Person):
    def work(self):
        print("I am an Employee")

class Manager(Employee):
    def manage(self):
        print("I am a Manager")


m = Manager()
m.show()
m.work()
m.manage()

#Override a method in child class and call parent method using super().
class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child Method")


c = Child()
c.show()


#Encapsulation
#Create a class BankAccount with private balance.
class BankAccount:
    def __init__(self):
        self.__balance = 0


#Use getter and setter methods to update balance safely.
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

    def get_balance(self):
        return self.__balance

#Prevent negative salary using property decorators.
class Employee:
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative")


#Polymorphism
#Create a Shape class with method area(). Implement Circle and Rectangle.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

#Demonstrate method overloading using default arguments.
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c
m = Math()
print(m.add(5))
print(m.add(5, 10))
print(m.add(5, 10, 15))

#Demonstrate operator overloading (__add__).
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

#Create Engine class and use it inside Car class.
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def drive(self):
        self.engine.start()
        print("Car Driving")

#Create Team class that contains multiple Player objects.
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            print(p.name)


t = Team()
t.add_player(Player("Rahul"))
t.add_player(Player("Aman"))
t.show_players()

#

#













