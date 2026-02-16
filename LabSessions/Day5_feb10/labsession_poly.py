#1: Method Overriding with Inheritance Create a base class Employee with a method calculate_salary(). Create a subclass Manager that overrides calculate_salary() and adds a bonus. Demonstrate runtime polymorphism using parent class reference.
class Employee:
    def calculate_salary(self):
        return 30000

class Manager(Employee):
    def calculate_salary(self):
        return 30000 + 10000

emp = Employee()
mgr = Manager()

ref = emp
print(ref.calculate_salary())

ref = mgr
print(ref.calculate_salary())

#2: Polymorphism Using Function Arguments Create classes Dog, Cat, and Cow each with a method speak(). Write a function animal_sound(obj) that calls speak(). Pass different objects to the same function.
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

class Cow:
    def speak(self):
        print("Cow moos")

def animal_sound(obj):
    obj.speak()

animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())

#3: Multilevel Inheritance with Polymorphism Create Vehicle → Car → ElectricCar.Each class overrides the method fuel_type().Call the method using different object references.
class Vehicle:
    def fuel_type(self):
        print("Generic fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol or Diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric")

v = Vehicle()
c = Car()
e = ElectricCar()

v.fuel_type()
c.fuel_type()
e.fuel_type()


#4: Operator Overloading Create a class BankAccount with attribute balance.Overload + to add balances and > to compare balances.Demonstrate polymorphic behavior of operators.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance


acc1 = BankAccount(5000)
acc2 = BankAccount(3000)

print("Total Balance:", acc1 + acc2)
print("acc1 > acc2:", acc1 > acc2)


#6: Multiple Inheritance and MRO Create classes A, B, C, and D(diamond structure).Override the same method in B and C.Call method using D object and observe MRO.
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())


#7:Polymorphism with Exception Handling Create Calculator class with divide(). Create SafeCalculator that overrides divide() and handles ZeroDivisionError. Demonstrate method overriding.
class Calculator:
    def divide(self, a, b):
        return a / b

class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

calc = Calculator()
safe = SafeCalculator()

print(safe.divide(10, 2))
print(safe.divide(10, 0))

#8: Real - Time Payment System Create base class Payment with method pay().Create CreditCard, UPI, and NetBanking subclasses.Use a single function to process all payments.
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")

def process_payment(payment, amount):
    payment.pay(amount)

process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
process_payment(NetBanking(), 2000)





