#iter() method - built in command
#create a iterator from a iterable
import get_input

#iteration - looping in the collection of items

a=[10,20,30,40,50]

#conver the list into a iterator
iterator=iter(a)

#next() allows the user to acces  the elements
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the string to a iterator
s="Hello"
iterator=iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))

#convert the dict to a iterator
d={'a':1,'b':2,'c':3}
iterator=iter(d)
print(next(iterator))
print(next(iterator))

#for loop to iterate
for key in iterator:
    print(key)

for key, value in d.items():
    print(key,"->",value)

#iter(callable,sentinel)
it=iter(input,"quit")
for value in it:
    print("you entered",value)

for value in iter(get_input, "quit"):
    print("you entered:",value)

print("loop ended")



