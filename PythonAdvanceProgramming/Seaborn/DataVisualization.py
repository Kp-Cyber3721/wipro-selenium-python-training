import seaborn as sns
import matplotlib.pyplot as plt

#basic plot(line plot)

#load the sample data set
data = sns.load_dataset('flights')

#line plot
sns.lineplot(x="year", y="passengers", data=data)
plt.title("yearly passengers growth")
plt.show()

#bar plot
data = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=data)

plt.title("Total Bill vs Tips")
plt.show()

#Scatterplot
data = sns.load_dataset("tips")
sns.scatterplot(x="day", y="total_bill", data=data)

plt.title("Total Bill vs Tips")
plt.show()

#histogram
data = sns.load_dataset("tips")
sns.histplot(data["total_bill"],bins=20)

plt.title("Total Bill vs Tips")
plt.show()
#box plot
data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Bill Distribution by Day")
plt.show()


#heat map
data = sns.load_dataset("tips")
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

#pair plot
data = sns.load_dataset("iris")
sns.palplot(data)
plt.show()

#violin plot
data = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=data)
plt.title("Bill Distribution by day")
plt.show()

#count plot
data = sns.load_dataset("tips")
sns.countplot(x="day", data=data)
plt.title("Numbers of Customers per day")
plt.show()

#Regression plot
data = sns.load_dataset("tips")
sns.regplot(x="day", y="total_bill", data=data)
plt.title("Regression between  Bill and Tips")
plt.show()


