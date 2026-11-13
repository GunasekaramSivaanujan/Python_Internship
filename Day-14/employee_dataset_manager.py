import pandas as pd 

# Employee Dataset
data ={
    "Employee_ID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Arun", "Siva", "Ravi", "Kumar", "Abi", "Banu", "Sinthu", "Manoj", "Kavi", "Sara"],
    "Age": [25,28,30,26,24,32,29,27,31,23],
    "Department":["IT", "HR", "IT", "Finance", "HR", "IT", "Sales", "Finance", "Sales", "IT"],
    "Salary": [50000, 45000, 60000, 55000, 40000, 65000, 52000, 58000, 48000, 42000],
    "Experience": [2, 4, 6, 3, 1, 7, 5, 4, 6, 1],
    "Performance_Score": [85, 78, 90, 82, 75, 95, 88, 80, 86, 79]
}
df = pd.DataFrame(data)

# Display Complete Employee Dataset
print("Complete Employee Dataset")
print(df)

# Display Selected Columns
print("Employee Name and Salary")
print(df[["Name","Salary"]])

#  Display First 5 Employees
print("First 5 Employees")
print(df.head())

# Display Last 5 Employees
print("Last 5 Employees")
print(df.tail())

# Add Bonus Column
df["Bonus"] = [5000,4000,6000,4500,3000,7000,5000,5500,4000,3500]
print("Employee Dataset with Bonus")
print(df)

# Rename Salary Column 
df = df.rename(columns={"Salary":"Base_Salary"})
print("Updated Column Names")
print(df)

# Remove Unnecessary Column
df = df.drop("Performance_Score", axis=1)
print("Dataset After Removing Column")
print(df)

# Select Employee Using loc
print("Employee Details Using loc")
print(df.loc[0])

# Select Employee Using iloc
print("Employee Details Using iloc")
print(df.iloc[0])

# Calculate Total Salary
df["Total_Salary"] = df["Base_Salary"] + df["Bonus"]
print("Employee Total Salary")
print(df[["Name", "Base_Salary", "Bonus", "Total_Salary"]])

