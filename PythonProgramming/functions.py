#functions is a block of code that performs a specific tasks
#created using  def functionname()
#default function with no parameters
def printdata():
    print("Hello world")
#call the function
printdata()

#function with parameters
def printdata(name):
    print("Hello ",name)
#pass the argument
printdata("Tina")
printdata("Rita")
#return Statement
#in order to return the function value we would use return statement will be used
def sq(num):
    result = num * num
    return result

#function call
square = sq(3)
print('square :',square)

#function pass
def func_pass():
    pass

#call the function
func_pass()

#multiple return values
def cal(a, b):
    return a-b, a+b,a*b
sub,add,mul=cal(10,5)
print(sub)
print(add)
print(mul)

#function calling a another function

def areaofrect(length, width):
    return length * width

def areaofsq(side):
    return side * side

value = areaofrect(4, 6)
sq= areaofsq(value)
print(sq)

#function with a loop
def even(limit):
    for i in range(2, limit+1,2):
        print(i)
even(10)

#function with if else condition
def even(limit):
    if limit %2 ==0:
        return "even"
    else:
        return "odd"
print(even(10))
print(even(11))






