import pandas as pd
import matplotlib.pyplot as plt

#load the csv
data = pd.read_csv('sales.csv')

#calculate total sales per product
data['Total'] = data['Quantity']*data['Price']
total_sales = data.groupby('Product')['Total'].sum()
print("Total sales per product:\n", total_sales)

#find the best selling product
best_product = total_sales.idxmax()
print("\nBest selling product:", best_product)

#create a bar chart
total_sales.plot(kind='bar' , color='skyblue')
plt.title('Total Sale per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()