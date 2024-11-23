import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Display first rows of data
print(df.head())

# Get a summary of the dataset
print(df.info())

# Get a statistical summary of numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Calculate total sales and profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
print(f"Total Sales: ${total_sales:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate sales and profit by date
daily_sales_profit = df.groupby('Date').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
print(daily_sales_profit.head())

# DATA VISUALIZATION

# Sales over time
plt.figure(figsize=(18, 8))
sns.lineplot(data=daily_sales_profit, x='Date', y='Sales')
plt.title('Daily Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Profit'], bins=20, kde=True)
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.show()

# Save cleaned data to CSV
df.to_csv('cleaned_sales_data.csv', index=False)

# Save plot to a file
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_sales_profit, x='Date', y='Sales')
plt.title('Daily Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_sales_plot.png')
