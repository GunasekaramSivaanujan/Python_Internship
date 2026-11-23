# Import Required Libraries
import pandas as pd
import random 
import csv 

# Generate 2000 Sales Records
random.seed(42)
salespersons = ["Arun", "Kumar", "Ravi", "Suresh", "Nimal"]
regions = ["Colombo", "Jaffna", "Kandy", "Galle", "Negombo"]
products = ["Laptop", "Phone", "Shirt", "Shoes", "Table"]
categories = ["Electronics", "Clothing", "Furniture"]

with open("Day-20/sales_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # CSV Column Names
    writer.writerow([
        "Order ID",
        "Salesperson",
        "Region",
        "Product",
        "Category",
        "Quantity",
        "Revenue",
        "Profit"
    ])

    # Generate 2000 Sales Records
    for i in range(2000):

        order_id = f"O{i+1:04}"
        salesperson = random.choice(salespersons)
        region = random.choice(regions)
        product = random.choice(products)
        category = random.choice(categories)
        quantity = random.randint(1, 10)
        revenue = quantity * random.randint(5000, 20000)
        profit = int(revenue * random.uniform(0.05, 0.25))

        writer.writerow([
            order_id,
            salesperson,
            region,
            product,
            category,
            quantity,
            revenue,
            profit
        ])

print("2000 Sales Records Generated Successfully!")

# Load Sales Dataset
df = pd.read_csv("Day-20/sales_data.csv")

# Display First 5 Records 
print("\nFirst 5 sales Records:")
print(df.head())

# Display Dataset Information:
print("\nDataset Information:")
print(df.info())

# Calculate Total Revenue by Region 
region_revenue = df.groupby("Region")["Revenue"].sum()
print("\nTotal Revenue by Region:")
print(region_revenue)

# Calculate Total Revenue by Category
category_revenue = df.groupby("Category")["Revenue"].sum()
print("\nTotal Revenue by Category:")
print(category_revenue)

# Calculate Total Profit by Salesperson
salesperson_profit = df.groupby("Salesperson")["Profit"].sum()
print("\nTotal Profit by Salesperson:")
print(salesperson_profit)

# Identify Top Salesperson
salesperson_revenue = df.groupby("Salesperson")["Revenue"].sum()
top_salesperson = salesperson_revenue.idxmax()
top_revenue = salesperson_revenue.max()
print("\nTop Salesperson:")
print("Salesperson:", top_salesperson)
print("Total Revenue:", top_revenue)

# Identify Best-Performing Region
best_region = region_revenue.idxmax()
highest_region_revenue = region_revenue.max()
print("\nBest-Performing Region:")
print("Region:", best_region)
print("Total Revenue:", highest_region_revenue)

# Identify Best-Selling Category
category_quantity = df.groupby("Category")["Quantity"].sum()
best_category = category_quantity.idxmax()
highest_quantity = category_quantity.max()
print("\nBest-Selling Category:")
print("Category:", best_category)
print("Total Quantity Sold:", highest_quantity)

# Rank Regions Based on Total Profit
region_profit = df.groupby("Region")["Profit"].sum()
region_ranking = region_profit.sort_values(ascending=False)
print("\nRegion Ranking Based on Total Profit:")
print(region_ranking)

# Combine Analysis Results
analysis_results = pd.DataFrame({
    "Revenue by Region": region_revenue,
    "Revenue by Category": category_revenue,
    "Profit by Salesperson": salesperson_profit
})

# Save Analysis Results
analysis_results.to_csv("Day-20/sales_analysis.csv")
print("\nSales Analysis Results Saved Successfully!")