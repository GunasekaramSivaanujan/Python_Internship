import pandas as pd
import random
import csv

# Generate 2000 Sales Records
random.seed(42)
salespersons = ["Arun", "Kumar", "Ravi", "Suresh", "Nimal"]
regions = ["Colombo", "Jaffna", "Kandy", "Galle", "Negombo"]
products = ["Laptop", "Phone", "Shirt", "Shoes", "Table"]

categories = {
    "Laptop": "Electronics",
    "Phone": "Electronics",
    "Shirt": "Clothing",
    "Shoes": "Clothing",
    "Table": "Furniture"
}

with open("Day-21/sales_data.csv", "w", newline="") as file:

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

    # Generate 2000 Records
    for i in range(2000):

        order_id = f"O{i+1:04}"
        salesperson = random.choice(salespersons)
        region = random.choice(regions)
        product = random.choice(products)
        category = categories[product]
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
df = pd.read_csv("Day-21/sales_data.csv")

# Display First 5 Records
print("\nFirst 5 Sales Records:")
print(df.head())

# Display Dataset Information
print("\nDataset Information:")
print(df.info())

# Regional Report
regional_report = df.groupby("Region").agg({
    "Revenue": ["sum", "mean"],
    "Profit": "sum"
})
print("\nRegional Business Report:")
print(regional_report)

# Product Report
product_report = df.groupby("Product").agg({
    "Quantity": "sum",
    "Revenue": "sum",
    "Profit": "sum"
})
print("\nProduct Business Report:")
print(product_report)

# Salesperson Report
salesperson_report = df.groupby("Salesperson").agg({
    "Order ID": "count",
    "Revenue": ["sum", "mean"]
})
print("\nSalesperson Business Report:")
print(salesperson_report)

# Final Business Intelligence Summary
top_region = regional_report[("Revenue", "sum")].idxmax()
top_product = product_report["Revenue"].idxmax()
top_salesperson = salesperson_report[("Revenue", "sum")].idxmax()
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
average_order_value = df["Revenue"].mean()
print("\n========== BUSINESS INTELLIGENCE SUMMARY ==========")
print("Top Region:", top_region)
print("Top Product:", top_product)
print("Top Salesperson:", top_salesperson)
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Average Order Value:", round(average_order_value, 2))

# Export Reports as CSV Files
regional_report.to_csv("Day-21/regional_report.csv")
product_report.to_csv("Day-21/product_report.csv")
salesperson_report.to_csv("Day-21/salesperson_report.csv") 
print("\nAll Business Reports Exported Successfully!")

