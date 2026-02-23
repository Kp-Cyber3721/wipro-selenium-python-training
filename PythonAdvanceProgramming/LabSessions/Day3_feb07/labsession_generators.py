#Write a generator to generate numbers from 1 to N.
def gen_num(n):
    for i in range(1, n+1):
        yield i
for x in gen_num(5):
    print(x)

#Create a generator to generate even numbers only.
def gen_even(n):
    for i in range(2, n+1, 2):
        yield i

for x in gen_even(10):
    print(x)

#Write a generator to read a file line by line.
def read_file(fname):
    with open(fname) as f:
        for line in f:
            yield line
for line in read_file("C:/Users/priya/PycharmProjects/PythonAdvanceProgramming/Dataformats/writecsv.csv"):
    print(line)

#Create a generator for Fibonacci series.
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
for x in fib(6):
    print(x)

#Write a generator that simulates retry attempts (max 3 tries).
def retry():
    for i in range(1, 4):
        yield f"Attempt {i}"
for r in retry():
    print(r)

