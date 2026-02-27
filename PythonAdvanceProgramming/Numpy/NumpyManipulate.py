import numpy as np
#changing shape
#reshape
a= np.arange(1,7)
print("Original Array:", a)

#reshape the array
reshape = a.reshape(2,3)
print("Reshaped Array:", reshape)

#flat = return a 1D iterator over the array
arr = np.array([[1,2],[3,4]])
for x in arr.flat:
    print(x)

#flatten - returns a copy of the array collapsed into one dimension
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr=arr.flatten()
print(at_arr)

#ravel() -returns a flattened array (faster than flatten)
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr=arr.ravel()
print(at_arr)

#pad() - returns a padded array with shape increased according to pad_width
arr = np.array([1,2,3])
padded = np.pad(arr,2,'constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1 transpose
#reorder the dimensions of an array.

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)


#ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards
arr = np.zeros((2,3,4))
print(arr)
#2 is the blocks -axis 0
# 3 is rows -axis 1
# 4 is no of columns -axis 2
#(0,1,2) - (2,3,4)
#(2,0,1) - (4,2,3)
#arr[block][rows][columns]


new_arr = np.rollaxis(arr,2)
print(new_arr)
#swapzxes() - Interchanges two axes of an array
#$Axis 0 and Axis 2 Swapped
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr,0,2)
print(new_arr)

#moveaxis() - Moves Specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr,0,-1)
print(new_arr)




