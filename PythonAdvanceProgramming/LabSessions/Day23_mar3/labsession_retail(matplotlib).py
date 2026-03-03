import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Load dataset
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Priyadarshee@2003",
    database="retailDB"
)

query = "SELECT * FROM retail_data"
retail_df = pd.read_sql(query, connection)

# Convert Date to datetime
retail_df['Date'] = pd.to_datetime(retail_df['Date'])

# Handle null values
retail_df = retail_df.dropna()

# Create Revenue column
retail_df['Revenue'] = retail_df['Quantity'] * retail_df['Price']

# Analysis Questions

# 1. Which region generates the highest total revenue
region_revenue = retail_df.groupby('Region')['Revenue'].sum()
top_region = region_revenue.idxmax()
print("Region generating highest revenue:", top_region)

# 2. What is the monthly sales trend?
retail_df['Month'] = retail_df['Date'].dt.to_period('M')
monthly_revenue = retail_df.groupby('Month')['Revenue'].sum()

# 3. Which category performs best?
category_revenue = retail_df.groupby('Category')['Revenue'].sum()
best_category = category_revenue.idxmax()
print("Best performing category:", best_category)

# 4.What are the top 5 products by revenue?
product_revenue = retail_df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
top_5_products = product_revenue.head(5)
print("\nTop 5 Products by Revenue:\n", top_5_products)

# Visualizations (Matplotlib only)

# 1. Bar chart
plt.figure()
region_revenue.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# 2. Line plot
plt.figure()
monthly_revenue.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# 3. Pie chart
plt.figure()
category_revenue.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Contribution")
plt.ylabel("")
plt.show()

# 4. Horizontal bar
plt.figure()
top_5_products.plot(kind='barh')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()