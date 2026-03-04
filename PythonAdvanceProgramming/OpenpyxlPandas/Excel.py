import pandas as pd

#read excel Sheet

df=pd.read_excel("students.xlsx")
print(df.head())


#writing to excel
data ={
    "Name" :["Ram","Ravi","Sita"],
    "Age":[20,21,19],
    "Marks":[85,90,78]
}
df.to_excel("Output.xlsx",index=False,engine="openpyxl")

#read a specific column
df = pd.read_excel("Output.xlsx",usecols=["Name"],engine="openpyxl")
print(df)

#read a particular sheet
df = pd.read_excel("students.xlsx",
                   sheet_name="Sheet1",
                   engine="openpyxl")
print(df)

#read all sheets
df = pd.read_excel("students.xlsx",
                   sheet_name=None)
print(df)

#writing Multiple Sheets
data1 ={
    "Products":["Laptop","Phone"],
    "Sales":[10,20]
}
data2 ={
    "City":["Delhi","Mumbai"],
    "Customers":[200,150]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

with pd.ExcelWriter("report.xlsx",engine="openpyxl") as writer:
    df1.to_excel(writer,sheet_name="Sales")
    df2.to_excel(writer,sheet_name="Customers")





