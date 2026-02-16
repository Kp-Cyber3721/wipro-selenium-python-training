#exception -  handles runtime error which will disrupt the normal program flow
#benefits
#helps in debugging
#prevents program crashing
#handling errors and exception in the code more effeciently

#try except
#try - code to be executed
#except- exception details catching
#else: if the exception does not occur then else part will be executed
#finally-mandated code
#custom exceptions
try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print(" Please enter valid numbers")

#generic exception
try:
    a = 5/0
except Exception as e:
    print(e)
#runs only if no exception occurs
else:
    print("Division successfull")
finally:
    print("Close the browser")

#custom exception- creating a own exception
age= int(input("Enter the age :"))
if age < 18:
    raise ValueError("Age must be 18 or above")



