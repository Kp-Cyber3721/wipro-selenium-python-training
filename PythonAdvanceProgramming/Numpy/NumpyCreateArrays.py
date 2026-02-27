
'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
    Using numpy.eye() Function
    Using numpy.diag() Function
'''

import numpy as np

#1D array
#This function creates a Numpy array filled with zeroes
#By default , the data type is float64
a = np.zeros(5)
print(a)
#2D array of zeros
a_2D =np.zeros((4,3))
print(a_2D)

# using nompy.ones() Function
a = np.ones(5)
print(a)

#2D array of ones
a_2D =np.ones((4,3))
print(a_2D)

# Using numpy.arange() Function
#The numpy.arrange() function created an array by generating a sequence of numbers based on
#It is similar to Pythons built-in range() function
#with only the stop
a = np.arange(10)
print(a)

#providing the start , stop and step values
a = np.arange(1,10,2)
print(a)


# Using numpy.linspace() function
#linspace() is used to generate evenly spaced numbers over a specified interval
#endpoint is true last no is included
a=np.linspace(0,10,5, True)
print(a)

a=np.linspace(0,10,5, False)
print(a)

# Using numpy.random.rand() Function
#generates an array of the specified shape with random values between 0 and 1
#if no argument is provided , it returns a single random float value

a = np.random.rand(5)
print(a)

#2D
a = np.random.rand(2,3)
print(a)

#3D
a = np.random.rand(2,3,4)
print(a)

#Using numpy.empty() Function
#2D
#this function initializes an array without initializing its elements:
#the content of the array is arbitrary and may vary

a = np.empty((2,3))
print(a)

#using numpy.full() Function
#In the following example, we are using the numpy.full() function to create a 2-dimensional array
#filled entirely with the value 5

a= np.full((2,3),5)
print(a)

#numpy.eye()
#the numpy eye() function is used to create a 2d array with ones on the diagonal and zeros in all other positions

identity_matrix = np.eye((4))
print(identity_matrix)

#numpy.identity -function is used to generate a square identity matrix
identity_matrix = np.identity((5))
print(identity_matrix)

#numpy.diag()
#in case of 2d array, the function extracts the diagonal elements of array
#in case of 1d array, the function created a square diagonal matrix with the element of the array
#the diagonal values and zeros in remaining positions
matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("original matrix", matrix)
Diagonal_matrix = np.diag(matrix)
print("diagonal elements",Diagonal_matrix)



