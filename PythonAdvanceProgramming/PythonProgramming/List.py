empty_list=[]
numbers = [1,2,3,4,0,8,3]
mixdata=[1,"hello",True,6.67,1]
nested=[[1,2],[3,4]]

#accessing the list eliment(indexing concept)
print(mixdata[1])
print(mixdata[2])

#modifying the data
mixdata[4]=6
print(mixdata)

#add element
mixdata.insert(0,10)
print(mixdata)
#append will add at the end
mixdata.append("John")
print(mixdata)

#remove data
mixdata.remove("hello")
print(mixdata)
mixdata.pop(1)
print(mixdata)

#list method
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(3))

print(numbers.index(3))

numbers.clear()

fruits =["apple","banana","cherry"]
for items in fruits:
    print(items)

for i, fruit in enumerate(fruits):
    print(i,fruit)


#slicing- access a portion of list
my_list=['p','r','o','g','r','a','m']
print("my_list =",my_list)
#get the list with items from index 2 to 5(n-1)
print(my_list[2: 5])

#ommit start and end indices
print(my_list[5:])

#from index 5 to last(n)
print(my_list[5: ])
#from first item to last item
print((my_list[:]))

#extends
numbers = [1,3,5]
even_numbers = [2,4,6]
#adding elements of one list to another
numbers.extend(even_numbers)
print(numbers)






