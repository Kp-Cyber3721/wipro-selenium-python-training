#default Methods - built in methods,  user define methods - method name , method body
#parametarized methods
#it allows the same methods to behave differently for diif input

#parametarized methods (multiple parameter)
class Calculator:
    def add(self,a,b):
        print(a+b)

c = Calculator()
c.add(10,20)
c.add(5,7)

#default parameter
class Test:
    def run(self,browser = "Chrome"):
        print("Running on ",browser)
t = Test()
t.run()
t.run("Firefox") #if we dont write firefox it will take default chrome ad parameter

#*args parameterized method
class Numbers:
    def total(self, *args):
        print(sum(args))
n= Numbers()
n.total(10,20,30)
n.total(10)
n.total(10,60)


