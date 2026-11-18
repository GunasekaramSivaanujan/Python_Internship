import csv 
import random 

# Generate 500 Patinent Records 
random.seed(42)
genders = ["Male","Female"]
with open("Day-17/patient_data.csv","w",newline="") as file:
    writer = csv.writer(file)

    #CSV Column Names
    writer.writerow([
        "Patient_ID",
        "Age",
        "Gender",
        "Blood_Pressure",
        "Glucose",
        "BMI",
        "Cholesterol"
    ])

    # Create 500 Records 
    for i in range(500):
        age = random.randint(18, 80)
        gender = random.choice(genders)
        blood_pressure = random.randint(90, 160)
        glucose = random.randint(70, 180)
        bmi = round(random.uniform(18, 40), 1)
        cholesterol = random.randint(120, 280)

        # Introduce Missing Values
        if random.random() < 0.1:
            age = ""
        if random.random() < 0.1:
            glucose = ""
        if random.random() < 0.1:
            bmi = ""
        if random.random() < 0.1:
            cholesterol = ""

        writer.writerow([
            f"P{i+1:03}",
            age,
            gender,
            blood_pressure,
            glucose,
            bmi,
            cholesterol
        ])

print("500 Patient Records Created Successfully!")

# Import Pandas Library
import pandas as pd

# Load Patient Dataset
df = pd.read_csv("Day-17/patient_data.csv")
print("Patient Dataset Loaded Successfully")

# Count Missing Values
print("Missing Values in Each Column")
print(df.isnull().sum())

# Calculate Missing Values Percentage
missing_percentage = (df.isnull().sum() / len(df)) * 100
print("Missing Values Percentage")
print(missing_percentage)

# Store Missing Values Before Cleaning
missing_before = df.isnull().sum().sum()

# Fill Missing Values Using Median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Glucose"] = df["Glucose"].fillna(df["Glucose"].median())
df["BMI"] = df["BMI"].fillna(df["BMI"].median())
df["Cholesterol"] = df["Cholesterol"].fillna(df["Cholesterol"].median())
print("Missing Values Filled Successfully!")

# Count Missing Values After Cleaning
missing_after = df.isnull().sum().sum()
print("Missing Values Before Cleaning:", missing_before)
print("Missing Values After Cleaning:", missing_after)

# Save Cleaned Patient Dataset
df.to_csv("Day-17/cleaned_patient_data.csv", index=False)
print("Cleaned Patient Dataset Saved Successfully!")

# Display Cleaning Results
print("\n===== PATIENT DATA CLEANING RESULTS =====")
print("Total Patient Records:", len(df))
print("Missing Values Before Cleaning:", missing_before)
print("Missing Values After Cleaning:", missing_after)
print("Cleaning Status: Successful")

# Generate Cleaning Report
with open("Day-17/cleaning_report.txt", "w") as file:
    file.write("PATIENT DATA CLEANING REPORT\n")
    file.write("-----------------------------\n")
    file.write(f"Total Patient Records: {len(df)}\n")
    file.write(f"Missing Values Before Cleaning: {missing_before}\n")
    file.write(f"Missing Values After Cleaning: {missing_after}\n")
    file.write("Cleaning Method: Median Imputation\n")
    file.write("Cleaning Status: Successful\n")
print("Cleaning Report Saved Successfully!")