#polymorphism means taking many forms

#same methods / function name will behave differently depending on the type of the object, input arguments, class implementation

#object type
print(len("python"))#string
print(len([1,2,3,4]))# list
print(len({1,2,3,4})) #tuple

#input arguments no of arguments / data types

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c

c= calculator()
print(c.add(5))
print(c.add(5,10.5))
print(c.add(5 ,10,15))

#runtime polymorphism is supported
#achieved method overriding - child class method will override the parent class method

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
a=Dog()
a.sound()




