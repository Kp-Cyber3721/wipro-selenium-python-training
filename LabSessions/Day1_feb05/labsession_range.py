#Write a Python function to check whether a number falls within a given range
def inrange(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False
print(inrange(5,1,10))

#Write a Python function to Print even numbers from 1 to 50
def printevennumbers():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)
printevennumbers()



#Write a Python function to Sum of numbers from 1 to 100
def sumof100():
    t = 0
    for i in range(1, 101):
        t += i
    return t
print(sumof100())

#Print all numbers sum for by 5 between 1 and 100
for i in range(1, 101):
    if i % 5 == 0:
        print(i)

#Create a list of numbers from 50 to 100 with a step of 5
n = list(range(50, 101, 5))
print(n)

#Print the square of each number from 1 to 10
for i in range(1, 11):
    print(i * i)



#Print numbers between -10 and 10
for i in range(-10, 11):
    print(i)

