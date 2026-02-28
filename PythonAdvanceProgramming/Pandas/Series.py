#Pandas - it is high performance and data manipulation and data analysis tool
#developed in 2008 Mckinnley
#data frames object
#list , csv, josn, pdf

#series -  A one-dimensional labeled homogeneous array, size immutable
#DataFrames is a 2dimensional labeled ,size-mutable tabular structure with potentially heterogeneously typed columns.

import pandas as pd
#creation of series Out of lists
data = ['Steve', '35', 'Male', '3.5']
series =pd.Series(data, index=['Name','Age','Gender','Rating'])
print(series)

#create Series using custom indexing
data =[100,200,300]
s = pd.Series(data, index =['a','b','c'])
print(s)

#create series from dictionary
data={'a':1 , 'b':2, 'c':3}
s=pd.Series(data)
print(s)

#create series Numpy array
import numpy as np
data = np.array([5,10,15])
s=pd.Series(data)
print(s)

#create a empty series
s = pd.Series(dtype=float)
print(s)

#cerate series with specific data type
data = [1,2,3]
s = pd.Series(data,dtype=float)
print(s)







