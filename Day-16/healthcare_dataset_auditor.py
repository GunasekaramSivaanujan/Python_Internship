import pandas as pd

# Load Healthcare Dataset
df = pd.read_csv("Day-16/healthcare_data.csv")
print("Healthcare Dataset Loaded Successfully")

# Display Dataset Shape
print("Dataset Shape")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Display Column  Names
print("Dataset Column Names")
print(df.columns.tolist())

# Display Data Types
print("Dataset Data Types")
print(df.dtypes)

# Check Missing Values
print("Missing Values in Each Column")
print(df.isnull().sum())

# Check Duplicate Records 
duplicate_count = df.duplicated().sum()
print("Number of Duplicate Records:", duplicate_count)

# Check Invalid Age Values
invalid_age = df[
    (pd.to_numeric(df["Age"], errors="coerce")<0)|
    (pd.to_numeric(df["Age"],errors="coerce")>120)
]

print("Invaild Age Records")
print(invalid_age)
print("Total Invalid Age Records:", len(invalid_age))

# Check Incorrect Age Data Types
incorrect_age = df[
    pd.to_numeric(df["Age"], errors="coerce").isnull()
    & df["Age"].notnull()
]

print("Incorrect Age Data Types")
print(incorrect_age)
print("Total Incorrect Age Records:",len(incorrect_age))

# Display Statistical Summary 
print("Healthcare Dataset Statistical Summary")
print(df.describe())

# Generate Data Quality Report
print("\n========== DATA QUALITY REPORT ==========")
print("Total Records:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Records:", duplicate_count)
print("Invalid Age Records:", len(invalid_age))
print("Incorrect Age Types:", len(incorrect_age))
print("=========================================")

# Save Data Quality Report
with open("Day-16/data_quality_report.txt", "w") as file:

    file.write("HEALTHCARE DATA QUALITY REPORT\n")
    file.write("--------------------------------\n")
    file.write(f"Total Records: {df.shape[0]}\n")
    file.write(f"Total Columns: {df.shape[1]}\n")
    file.write(f"Missing Values: {df.isnull().sum().sum()}\n")
    file.write(f"Duplicate Records: {duplicate_count}\n")
    file.write(f"Invalid Age Records: {len(invalid_age)}\n")
    file.write(f"Incorrect Age Types: {len(incorrect_age)}\n")

print("Data Quality Report Saved Successfully!")