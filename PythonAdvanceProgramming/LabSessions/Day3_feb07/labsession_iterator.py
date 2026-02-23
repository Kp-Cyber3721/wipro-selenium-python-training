#Create a custom iterator that prints numbers from 1 to 5.
class OneToFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

for i in OneToFive():
    print(i)

#Write an iterator class that returns next even number.
class EvenNumbers:
    def __init__(self, limit):
        self.num = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            val = self.num
            self.num += 2
            return val
        else:
            raise StopIteration
for i in EvenNumbers(10):
    print(i)

#__iter__(): Returns the iterator object
#__next__(): Returns next element or raises StopIteration




