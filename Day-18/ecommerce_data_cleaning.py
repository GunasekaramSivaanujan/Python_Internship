import csv
import random
import pandas as pd
from datetime import date,timedelta

# Generate 1000 E-Commerce Orders
random.seed(42)
products = ["Laptop", "Phone", "Mouse", "Keyboard", "Monitor"]
categories = ["Electronics", "Accessories"]
cities = ["Colombo", "colombo", "COLOMBO", "Jaffna", "JAFFNA", "Kandy"]
prices = [50000, 80000, 1500, 2500, 30000]

with open("Day-18/raw_orders.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # CSV Column Names 
    writer.writerow([
        "Order_ID",
        "Customer_ID",
        "Product",
        "Category",
        "Quantity",
        "Price",
        "City",
        "Order_Date"
    ])

    # Generate 1000 Records
    for i in range(1000):
        order_id = f"O{i+1:04}"
        customer_id = f"C{random.randint(1, 200):03}"
        product = random.choice(products)
        category = random.choice(categories)
        quantity = random.randint(1, 10)
        price = prices[products.index(product)]
        city = random.choice(cities)

        order_date = date(2026, 1, 1) + timedelta(days=i % 365)

        # Introduce Missing Prices
        if i % 20 == 0:
            price = ""
        # Introduce Duplicate Order IDs
        if i in [100, 200, 300, 400, 500]:
            order_id = f"O{i:04}"
        # Introduce Invalid Quantities
        if i % 50 == 0:
            quantity = -5
        # Introduce Different Date Formats
        if i % 3 == 0:
            order_date = order_date.strftime("%d-%m-%Y")
        else:
            order_date = order_date.strftime("%Y-%m-%d")

        writer.writerow([
            order_id,
            customer_id,
            product,
            category,
            quantity,
            price,
            city,
            order_date
        ])

print("1000 E-Commerce Orders Generated Successfully!")

# Load Raw E-Commerce Dataset
df = pd.read_csv("Day-18/raw_orders.csv")
print("Raw E-Commerce Dataset Loaded Successfully!")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

# Check Missing Prices
missing_prices = df["Price"].isnull().sum()
print("Missing Prices:", missing_prices)

# Check Duplicate Orders
duplicate_orders = df["Order_ID"].duplicated().sum()
print("Duplicate Orders:", duplicate_orders)

# Check Invalid Quantities
invalid_quantities = df[df["Quantity"] <= 0]
print("Invalid Quantity Records")
print(invalid_quantities)
print("Total Invalid Quantities:", len(invalid_quantities))

# Standardize City Names
df["City"] = df["City"].str.strip().str.title()
print("City Names Standardized Successfully!")
print(df["City"].unique())

# Convert Order Dates to Standard Format
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    dayfirst=True,
    format="mixed"
)
print("Order Dates Converted Successfully!")
print(df["Order_Date"].head())

# Fill Missing Prices Using Product Median
df["Price"] = df.groupby("Product")["Price"].transform(
    lambda x: x.fillna(x.median())
)
print("Missing Prices Filled Successfully!")
print("Remaining Missing Prices:", df["Price"].isnull().sum())

# Remove Duplicate Orders
df = df.drop_duplicates(subset="Order_ID", keep="first")
print("Duplicate Orders Removed Successfully!")
print("Remaining Duplicate Orders:", df["Order_ID"].duplicated().sum())

# Remove Invalid Quantities
df = df[df["Quantity"] > 0]
print("Invalid Quantities Removed Successfully!")
print("Remaining Invalid Quantities:", (df["Quantity"] <= 0).sum())

# Save Cleaned E-Commerce Dataset
df.to_csv("Day-18/clean_orders.csv", index=False)
print("Cleaned Dataset Saved Successfully!")
print("Total Cleaned Orders:", len(df))

# Generate Cleaning Log
with open("Day-18/cleaning_log.txt", "w") as file:

    file.write("E-COMMERCE DATA CLEANING REPORT\n")
    file.write("--------------------------------\n")
    file.write("Original Records: 1000\n")
    file.write(f"Cleaned Records: {len(df)}\n")
    file.write(f"Remaining Missing Prices: {df['Price'].isnull().sum()}\n")
    file.write(f"Remaining Duplicate Orders: {df['Order_ID'].duplicated().sum()}\n")
    file.write(f"Remaining Invalid Quantities: {(df['Quantity'] <= 0).sum()}\n")
    file.write("City Names: Standardized\n")
    file.write("Order Dates: Standardized\n")
    file.write("Cleaning Status: Completed\n")
    
print("Cleaning Log Generated Successfully!")