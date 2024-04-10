import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

data = pd.read_csv('sales.csv')

sales_list = data['sales'].tolist()

expenditure_list = data['expenditure'].tolist()

month_list = data['month'].tolist()

data['Percentage Change'] = data['sales'].pct_change() * 100

data['Percentage Change Rounded'] = data['Percentage Change'].round(2)

data.drop(columns=['Percentage Change'], inplace=True)

x = np.array(month_list)
y = np.array(sales_list)

total_sales = sum(sales_list)

sales_list_df = pd.DataFrame({'Sales List': [sales_list]})
total_sales_df = pd.DataFrame({'Total Sales': [total_sales]})

data.to_csv('sales2.csv', index=False)

sales_list_df.to_csv('Sales_list.csv', index=False)
total_sales_df.to_csv('Total_Sales.csv', index=False)

print("Sales Listed:", sales_list)
print("Sales list saved to 'Sales_list.csv'")

print("Total sales across all months:", total_sales)
print("Total sales saved to 'Total_Sales.csv'")

choice = input("Would you like to see the minimum sale? (y/n) ")

if choice == 'y':
    minimum_sale = min(sales_list)
    print(minimum_sale)

choice2 = input("Would you like to see the maximum sale? (y/n) ")

if choice2 == 'y':
    maximum_sale = max(sales_list)
    print(maximum_sale)

choice3 = input("Do you want to see the average sale? (y/n) ")

if choice3 == 'y':
    average_sale = int(total_sales/len(sales_list))
    print(average_sale)

choice4 = input("Do you want to see the monthly percentage change? (y/n) ")

if choice4 == 'y':
    pct_diff = data['sales'].pct_change() *100
    print(pct_diff)

plt.bar(x, y, color = "red")
plt.title('Sales in 2018')
plt.xlabel('Month')
plt.ylabel('Sales in £')
plt.show()

bar_width = 0.35

x = np.arange(len(month_list))

fig, ax = plt.subplots()
bars1 = ax.bar(x - bar_width/2, sales_list, bar_width, label='Sales', color='blue')
bars2 = ax.bar(x + bar_width/2, expenditure_list, bar_width, label='Expenditure', color='orange')

ax.set_xlabel('Month')
ax.set_ylabel('Amount')
ax.set_title('Sales and Expenditure Comparison 2018')
ax.set_xticks(x)
ax.set_xticklabels(month_list)
ax.legend()

plt.show()

