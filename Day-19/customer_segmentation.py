import csv
import random
import pandas as pd

# Generate 1000 Customer Records

random.seed(42)

genders = ["Male", "Female"]
cities = ["Colombo", "Jaffna", "Kandy", "Galle", "Negombo"]
products = ["Electronics", "Clothing", "Accessories", "Home Appliances"]

with open("Day-19/customer_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # CSV Column Names
    writer.writerow([
        "Customer ID",
        "Age",
        "Gender",
        "City",
        "Income",
        "Purchase Amount",
        "Product Category"
    ])

    # Generate 1000 Customers
    for i in range(1000):

        customer_id = f"C{i+1:04}"
        age = random.randint(18, 70)
        gender = random.choice(genders)
        city = random.choice(cities)
        income = random.randint(20000, 200000)
        purchase_amount = random.randint(1000, 100000)
        product = random.choice(products)

        # Create Customers Who Never Purchased
        if i % 20 == 0:
            purchase_amount = 0

        writer.writerow([
            customer_id,
            age,
            gender,
            city,
            income,
            purchase_amount,
            product
        ])

print("1000 Customer Records Created Successfully!")

# Load Customer Dataset
df = pd.read_csv("Day-19/customer_data.csv")
# Display First 5 Customer Records
print("\nFirst 5 Customer Records:")
print(df.head())

# Filter Customers Above Age 40
above_40 = df[df["Age"] > 40]
print("\nCustomers Above Age 40:")
print(above_40)

# Filter Customers With Income Above 100,000
high_income = df[df["Income"] > 100000]
print("\nCustomers With Income Above 100,000:")
print(high_income)

# Filter Customers Who Spend Above 50,000
high_spending = df[df["Purchase Amount"] > 50000]
print("\nCustomers Spending Above 50,000:")
print(high_spending)

# Filter Customers From Colombo
colombo_customers = df[df["City"] == "Colombo"]
print("\nCustomers From Colombo:")
print(colombo_customers)

# Filter High-Income and High-Spending Customers
premium_customers = df[
    (df["Income"] > 100000) &
    (df["Purchase Amount"] > 50000)
]
print("\nHigh-Income and High-Spending Customers:")
print(premium_customers)

# Filter Customers Who Never Purchased
never_purchased = df[df["Purchase Amount"] == 0]
print("\nCustomers Who Never Purchased:")
print(never_purchased)

# Categorize Customers Based on Spending

def spending_category(amount):
    if amount > 50000:
        return "Premium"
    elif amount >= 20000:
        return "Regular"
    else:
        return "Low Value"

df["Spending Category"] = df["Purchase Amount"].apply(spending_category)
print("\nCustomer Spending Categories:")
print(df[["Customer ID", "Purchase Amount", "Spending Category"]])

# Save Segmented Customer Data
df.to_csv("Day-19/segmented_customers.csv", index=False)
print("\nSegmented Customer Data Saved Successfully!")