import pandas as pd
import numpy as np
#1. Create a DataFrame containing missing (Non e /NaN) values.
data = {
    "Name": ["Ram", "Sam", "John", "Priya", "Amit"],
    "Age": [25, np.nan, 30, 28, None],
    "Salary": [40000, 50000, np.nan, 60000, 45000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "City": ["Bangalore", "Mumbai", "Bangalore", "Delhi", "Bangalore"]
}
df = pd.DataFrame(data)
print("Original DataFrame")
print(df)

#2. Detect missing values using appropriate function.
print("\nMissing Values:")
print(df.isnull())

#3. Replace missing values with 0.
df_filled = df.fillna(0)
print("\nAfter Replacing Missing Values with 0:")
print(df_filled)

#4. Drop rows containing missing values.
df_dropped = df.dropna()
print("\nAfter Dropping Missing Values:")
print(df_dropped)

#5. Sort the DataFrame by Age in ascending order.
print("\nSorted by Age (Ascending):")
print(df.sort_values(by="Age"))

#6. Sort the DataFrame by Salary in descending order.
print("\nSorted by Salary in Descending order:")
print(df.sort_values(by="Salary", ascending=False))

#7. Perform groupby on Department and find average Salary per department.
print("\nAverage Salary as per Department:")
print(df.groupby("Department")["Salary"].mean())

#8. Find total Salary per department using groupby.
print("\nTotal Salary per Department:")
print(df.groupby("Department")["Salary"].sum())

#9. Filter employees where Age > 25 AND City = 'Bangalore'.
filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print("\nFiltered Employees (Age > 25 AND City = Bangalore):")
print(filtered)

#10. Create a new column 'Tax' which is 1 0% of Salary using apply().
df["Tax"] = df["Salary"].apply(lambda x: x * 0.10)
print("\nAfter Adding Tax Column:")
print(df)