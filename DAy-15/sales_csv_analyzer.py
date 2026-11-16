import pandas as pd

# Load CSV File
df = pd.read_csv("Day-15/sales_data.csv")
print("Sales Dataset Loaded Successfully")

# Display Dataset Information
print("Dataset Information")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("Column Names:", df.columns.tolist())
print("Data Types:")
print(df.dtypes)

# Display First 5 Records
print("First 5 Sales Records")
print(df.head())

# Display Last 5 Records
print("Last 5 Sales Records")
print(df.tail())

# Calculate Total Revenue
total_revenue = df["Revenue"].sum()
print("Total Sales Revenue:", total_revenue)

# Find Highest-Value Order
highest_order = df.loc[df["Revenue"].idxmax()]
print("Highest-Value Order")
print(highest_order)

# Save Analyzed Data to New CSV File
df.to_csv("Day-15/analyzed_sales_data.csv", index=False)
print("Analyzed data saved successfully!")