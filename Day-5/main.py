import numpy as np

# Sales Analytics Dashbord
product_id = np.array([101,102,103,104,105,106,107,108,109,110])

# Monthly Sales
monthly_sales = np.array([100,150,80,200,120,170,90,250,130,180])

# Revenue
revenue = np.array([50000,75000,40000,100000,60000,85000,45000,125000,65000,90000])

# Profit

profit = np.array([10000,15000,8000,20000,12000,17000,9000,25000,13000,18000])

# Display Dataset 

print("Sales Analytices Dashbord")
print("--------------------------")

print("Product IDs:", product_id)
print("Monthly Sales:", monthly_sales)
print("Revenue:", revenue)
print("Profit:",profit)

# Total Revenue 
total_revenue = np.sum(revenue)
print("Total Revenu:", total_revenue)

# Average Revenue
average_revenue = np.mean(revenue)
print("Average Revenu:", average_revenue)

#Highest Sales
highest_sales = np.max(monthly_sales)
print("Highest Sales:", highest_sales)

#Lowest Sales
lowest_sales = np.min(monthly_sales)
print("Lowest Sales:" , lowest_sales)

# Profit Percentage
profit_percentage = (np.sum(profit)/ np.sum(revenue))*100
print("Profit Percentage:", profit_percentage)

# Best Selling Product
best_index = np.argmax(monthly_sales)
best_product = product_id[best_index]
print("Best Selling Product:", best_product)

# Worst Selling product
worst_index = np.argmin(monthly_sales)
worst_product = product_id[worst_index]
print("Worst Selling Product:", worst_product)

# Top 5 Products Based on Revenue
top_5_index = np.argsort(revenue)[-5:][::-1]
top_5_products = product_id[top_5_index]
print("Top 5 Products:", top_5_products)

# Final Sales Summary

print("\n----- Final Sales Summary -----")
print("Total Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Profit Percentage:", profit_percentage)
print("Best Selling Product:", best_product)
print("Worst Selling Product:", worst_product)


