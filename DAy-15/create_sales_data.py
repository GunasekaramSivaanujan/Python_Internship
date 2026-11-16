import csv
from datetime import date, timedelta

# Generate 90 Sales Records

products = ["Laptop", "Mouse", "Keyboard", "Phone", "Monitor"]
categories = ["Electronics", "Accessories"]
cities = ["Colombo", "Jaffna", "Kandy", "Galle"]

with open("Day-15/sales_data.csv", "a", newline="") as file:

    writer = csv.writer(file)

    for i in range(90):

        order_id = 111 + i
        product = products[i % 5]
        category = categories[i % 2]
        quantity = (i % 5) + 1
        price = (i % 5 + 1) * 1000
        revenue = quantity * price
        city = cities[i % 4]
        order_date = date(2026, 2, 1) + timedelta(days=i)

        writer.writerow([
            order_id,
            product,
            category,
            quantity,
            price,
            revenue,
            city,
            order_date
        ])

print("90 records added successfully!")