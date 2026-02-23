#1.Write a Python program to sort a list of tuples using Lambda
# 2.Write a Python program to extract year, month, date and time using Lambda.
# 3.Write a Python script to concatenate the following dictionaries to create a new one.

data = [(1, 3), (4, 1), (2, 2)]
print(sorted(data, key=lambda x: x[1]))

from datetime import datetime
d = datetime.now()

print((lambda x: x.year)(d),
      (lambda x: x.month)(d),
      (lambda x: x.day)(d),
      (lambda x: x.strftime("%H:%M:%S"))(d))



