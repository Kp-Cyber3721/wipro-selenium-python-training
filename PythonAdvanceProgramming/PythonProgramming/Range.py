#all no should be integers
#step size cannot be zero
#start- default 0
#range does not create a list, it created a obj [memory efficiency]
#usage
#fast iteration


a= range(5)
print(a[1])
print(a[3])

a1= range(2,5)
print(a1[1])
#
a=range(2,5,3)
for i in a:
    print(i)

a=range(2,15,-3)
for i in a:
    print(i)

a=range(15,2,-1)
for i in a:
    print(i)

for attempt in range(3):
    pin=input("enter the pin:")
    if pin == "1234":
        print("Access granted")
    else:
        print("Try again")

#scenario apply discount based on the position of the item
prices = [100,200,300,400]
for i in range(len(prices)):
    if i % 2 == 0:
        print(f"discounted applied on item {i}")

#scenario : simulate polling every second for 10 second
import time
for seconds in range(10):
    print(f"checking the status at {seconds} sec")
    time.sleep(1)

#accessing of the enumerate values
a=['God','is','Great']
b=enumerate(a)
next_val =next(b)
print(next_val)