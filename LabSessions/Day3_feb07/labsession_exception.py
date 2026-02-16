#1.Handle FileNotFoundError Exception When Opening a File
try:
    file = open("C:\\Users\\priya\\PycharmProjects\\PythonAdvanceProgramming\\FileHandiling\\JsonFilehandiling.py","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found at the given location")


#write a program to handle invalid user input
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Please enter a valid number.")

#3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
import string

# for alphabet
print(random.choice(string.ascii_letters))

# for alphabet string
print(''.join(random.choice(string.ascii_letters) for _ in range(5)))

# for alphabet string of fixed length (3)
print(''.join(random.choice(string.ascii_letters) for _ in range(3)))






