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
#(3,4,2)

#Joining Arrays
#concatenate() -joining 2 array
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

#Stack - joins the array along the new axis

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

#hstack - Stacks arrays horizontally (column-wise
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))

#vstack - stacks arrays vertically (row-wise) (row-stack() will not work so in its place use vstack)
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))

#column_stack() - stack 1D arrays as columns into 2D array
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))


#Splitting Arrays
#split arrays into multiple sub-array based on axis
arr= np.array([1,2,3,4,5,6])
result = np.split(arr,3)
print(result)

#hsplit() - split array horizontally (column-size)
arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])
print(np.hsplit(arr2,2))

#vsplit - splits array vertically (row-wise)
arr2 = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])
print(np.vsplit(arr2,2))
#array_split() -similar to split() ,but does NOT require equal division
arr2 = np.array([1,2,3,4,5])
print(np.array_split(arr2,3))


#Adding/removing Elements
#resize() - Returns a new array with a specified shape
arr = np.array([1,2,3,4])
new_arr = np.resize(arr,(2,3))
print(new_arr)

#the elements will repeat in the new array
#returns a new array
#append() - Appends values at the end of an array
arr = np.array([1,2,3])
new_arr = np.append(arr,[4,5])
print(new_arr)

#2D array
a = np.array([[1,2],[3,4]])
b= np.array([[5,6]])
np.append(a,b,axis=0)

#insert values before given index
arr = np.array([10,20,30])
new_arr = np.insert(arr,2,15)
print(new_arr)

#Delete elements along a specified axis
arr = np.array([10,20,30])
new_arr = np.delete(arr,2)
print(new_arr)

#unique()
arr = np.array([1,2,2,3,4,4,5])
print(np.unique(arr))

#Repeating
#repeat() is used to repeat each element  of an array a specified number of times
arr = np.array([1,2,3])
print(np.repeat(arr,3))

#Different repeats for each element
arr = np.array([10,20,30])
print(np.repeat(arr,[1,2,3]))

#repeat in 2D Array
arr2 = np.array([[1,2],
                [3,4]])
print(np.repeat(arr2,3,axis=0))

#tile() the input array that will be repeated
my_array =np.array([1,2,3])
tiled_array= np.tile(my_array,2)
print("Original Array:", my_array)
print("Tiled Array:", tiled_array)


#Rearranging Elements
#flip() - Reverse the order of elements along a given axis
#If axis =None -> reverse entire flattened array
#if axis = 0 -> reverse rows
#if axis = 1 -> reverse columns

arr = np.array([1,2,3,4])
print(np.flip(arr))

#2D
arr2 = np.array([[1,2],
                 [3,4]])
print(np.flip(arr2,axis=0)) #flip rows
print(np.flip(arr2,axis=1)) #flip columns

#fliplr() -Flip Left-Right (axis=1) -works only on 2D+ arrays
arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(np.fliplr(arr2))

#flipud - Flip up-Down (axis=0)
print(np.flipud(arr2))

#roll() - Rolls (rotates) elements along a given axis.
arr2 = np.array([[1,2,3],
                 [4,5,6]])
np.roll(arr2,2,axis=None)

#Sorting and Searching
#sort() Returns a sorted copy of an array(or sorts in-place if using ndarray method)
arr = np.array([5,2,9,2])
sorted_arr = np.sort(arr)
print(sorted_arr)

#argsort() - Returns the indices that would sort the array return the iindex position
arr = np.array([5,2,9,1])
sorted_arr = np.sort(arr)
print(sorted_arr)
indices = np.argsort(arr)
print(indices)

#lexsort() - used for sorting with multiple columns ( like sorting by last name , then first name)
#sort by a first
#then by b(secondary key)
#sorting happens from right -> left
a= np.array([1,1,0,0])
b=np.array([1,0,1,0])
result = np.lexsort((b,a))
print(result)





#Changing Dimensions








