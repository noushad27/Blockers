import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('sales_data.csv')
#first rows of data sheet
print(df.head())
#get a summary
print(df.info())
#get a stats summary
print(df.describe())
#check for missing value
print(df.isnull().sum())
#drop the missing clm
df = df.dropna()

total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
print(f"total_sales: ${total_sales:.2f}")
print(f"total_profit: ${total_profit: .2f}")

#date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

daily_sales_profit = df.groupby('Date').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
print(daily_sales_profit.head())


#DATA VISUALIZATION

#sales over time
plt.figure(figsize=(18,8))
sns.lineplot(data=daily_sales_profit, x='Date', y='Sales')
plt.title('Daily Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout
plt.show()

#profit distribution
plt.figure(figsize=(12,6))
sns.histplot(df['Profit'], bins=20, kde=True)
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.show()

#Results
df.to_csv('cleaned_sales_data.csv', index=False)

plt.figure(figsize=(12,6))
sns.lineplot(data= daily_sales_profit, x='date', y='sales')
plt.title('Daily sales over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(roatation=45)
plt.tight_layout()
plt.savefig('daily_sales_plot.png')