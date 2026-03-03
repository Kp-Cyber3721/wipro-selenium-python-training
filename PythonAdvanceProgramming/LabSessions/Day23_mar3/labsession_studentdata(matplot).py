import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# dataset
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # or your wiprotraining URI
db = client["schoolDB"]
collection = db["students"]

data = list(collection.find({}, {"_id": 0}))
print(data)

student_df = pd.DataFrame(data)

# Create Average_Marks
student_df['Average_Marks'] = student_df[['Math', 'Science', 'English']].mean(axis=1)

# Create Result column
student_df['Result'] = np.where(
    student_df['Average_Marks'] >= 40,
    'Pass',
    'Fail'
)

# ANALYSIS

# 1 What is the average score per subject?
subject_avg = student_df[['Math', 'Science', 'English']].mean()
print("\nAverage Score per Subject:\n", subject_avg)

# 2 Does attendance correlate with performance?
correlation = student_df['Attendance'].corr(student_df['Average_Marks'])
print("\nCorrelation between Attendance and Performance:", correlation)

# 3 Compare performance by gender.
gender_performance = student_df.groupby('Gender')['Average_Marks'].mean()
print("\nPerformance by Gender:\n", gender_performance)

# 4 How many students passed vs failed?
result_counts = student_df['Result'].value_counts()
print("\nPass vs Fail:\n", result_counts)

# VISUALIZATIONS

# 1. Bar chart
plt.figure()
subject_avg.plot(kind='bar')
plt.title("Average Subject Scores")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()

# 2. Scatter plot
plt.figure()
plt.scatter(student_df['Attendance'], student_df['Average_Marks'])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

# 3. Boxplot
plt.figure()
student_df.boxplot(column='Average_Marks', by='Gender')
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.show()

# 4. Pie chart
plt.figure()
result_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Pass vs Fail Distribution")
plt.ylabel("")
plt.show()