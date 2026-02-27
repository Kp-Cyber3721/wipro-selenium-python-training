#NumPy indexing is used to access or modify elements in anarray
import numpy as np

a = np.arange(10)
print(a)
#at the 0th index what is the value
b = a[0]
print(b)

scores = ['86' , '98' ,'100', '65', '75']
arr = np.array(scores)
print(arr[2])

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[0,1])

arr = np.array([10,20,30,40,50])
print(arr[1:4])

#slicing - Slicing is the way to extract a subset of data from a NumPy array
#the syntax for slicing an array id [start:stop:step]
arr = np.array(['86' , '98' ,'100', '65', '75','62','75','80','12','45'])
print(arr[1:8:2])
arr =np.arange(10)
s = slice(1,8,2)
print(arr[s])

#slicing with starting parameter
a=np.arange(10)
print(a[2:])
#slicing with stop parameter
a=np.arange(10)
print(a[:7])

#using step parameter
a=np.arange(10)
print(a[::2])

#silicing 0f 2D arrays

employees = np.array([[1,25,50000],
                     [2,30,60000],
                     [3,28,55000],
                     [4,35,65000],
                     [5,40,70000]])
print("Information of employee 2:",employees[1])
print("Ages of employees from index 2 onwards",employees[2:,1])



array_3d = np.arange(24).reshape(2,3,4)
print("Original 3D array: \n",array_3d)
subarray = array_3d[0,:,:2]
print(subarray)

#Negative Slicing - Negative indexing allows accessing elements from the end of an array.

marks = np.array([93, 87, 98, 89, 67, 65, 54, 32, 21])
print("Lowest 5 marks is:", marks[-5:])

data=np.array(['H','A','R','R','Y'])
print(data[-1::-2])


