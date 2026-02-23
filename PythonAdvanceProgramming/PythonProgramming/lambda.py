#lambda function - anonymous(nameless) functions, one line , simple operations

#syntax lambda arguments: expressions


#it can have any number of arguments
#must have only one expression
# the expressions is automatically returned

#functions - function name, arguments , return type, code,

#normal function add 2 numbers
def add(a,b):
    return a+b
print(add(5, 3))
#lambda function
add=lambda a,b: a+b
print(add(5,3))

#square of a number
square = lambda x :x*x
print(square(5))

#check even or odd
even_odd = lambda x: "Even" \
    if x % 2 == 0 else "Odd"
print(even_odd(10))
print(even_odd(7))

max=lambda a,b:a if a>b else b
print(max(10,30))

#filter, map and reduce in built function in lamda
#filter-select data-filtering the data
#map-transform the data
#reduce-aggregate the data
#filter

numbers=[1,2,3,4,5,6]
evens=list(filter(lambda x: x%2 ==0, numbers))
print((evens))

#filter the failed testcase

status = ['Pass', 'Fail', 'Pass', 'Fail']
failed = list(filter(lambda s:s =='Fail', status))
print((failed))

nums = [-5, 10, -3, 7, 0, 2]

p= list(filter(lambda x: x > 0, nums))
print(p)

data = ["hello", "", "world", "", "python"]

empty_string = list(filter(lambda x: x != "", data))
print(empty_string)

#reduce - aggegarte - combining many values  to a one single result
from functools import reduce
nums = [10,20,30,40]
print(reduce(lambda x,y:x+y,nums))
# multiply
print(reduce(lambda x, y: x * y, nums))
# max value
print(reduce(lambda x, y: x if x > y else y, nums))
# min value
print(reduce(lambda x, y: x if x < y else y, nums))

#map - transform the data - the function is applied to every elements
num=[10,20,30,40]
squares = list(map(lambda x:x*x,nums))
print(squares)

#sorting in lambda
data=[(1,3),(4,1),(2,2)]
sorteddata= sorted(data, key=lambda x:x[0])
print(sorteddata)

marks={"a":75,"b":90,"c":60}
sorted_marks=dict(sorted(marks.items(),key=lambda x:x[1]))
print(sorted_marks)

nums = [1, 2, 3, 4, 5, 6]

# filter even numbers
evenno = list(filter(lambda x: x % 2 == 0, nums))
print(evenno)
# square the even numbers
square = list(map(lambda x: x * x, evenno))
print(square)
# find the sum
r = reduce(lambda x, y: x + y, square)
print(r)

salaries = [25000, 40000, 32000, 18000]

# filter salaries > 30000
high_sal = list(filter(lambda x: x > 30000, salaries))
print(high_sal)
# add 10% hike
hiked_sal = list(map(lambda x: x + (x * 0.10), high_sal))
print(hiked_sal)
# total payout
total_pay = reduce(lambda x, y: x + y, hiked_sal)
print(total_pay)

print(list(map(lambda x: x.upper(), filter(lambda x: x.islower(), "PyThOn"))))


