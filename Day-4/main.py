import pandas as pd
data ={
    "patient_ID": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    "Age":[25,65,45,70,35,55,62,40,75,30,58,67,42,72,33,61,50,68,28,64],
    "Blood_Pressure":[120,150,130,160,110,145,155,125,170,115,140,165,118,175,135,158,122,168,112,152],
    "Sugar_Level":[90,180,110,200,95,160,175,105,210,100,150,190,98,220,130,185,108,195,92,170],
    "Heart_Rate":[75,85,80,90,72,88,82,78,95,70,84,92,76,96,81,89,74,94,73,86],
    "BMI":[22,28,24,30,21,27,29,23,31,22,26,32,20,33,25,29,21,31,22,28]
}

df= pd.DataFrame(data)

print("Hospital patient Dataset")

print(df)

# 1. Display First Patient
print("\nFirst Patient:")
print(df.iloc[0])

# 2. Display Last Patient
print("\nLast Patient:")
print(df.iloc[-1])

# 3. Display All Blood Pressure Values
print("\nAll Blood Pressure Values:")
print(df["Blood_Pressure"])

# 4. Display Age and BMI Columns
print("\nAge and BMI Columns:")
print(df[["Age", "BMI"]])

# 5. Retrieve Patients 5 to 15
print("\nPatients 5 to 15:")
print(df.iloc[4:15])

# 6. Patients with High Blood Pressure
print("\nPatients with High Blood Pressure:")
print(df[df["Blood_Pressure"] > 140])

# 7. Identify Senior Citizens
print("\nSenior Citizens (Age > 60):")
print(df[df["Age"] > 60])

# 8. Patients with High BP and High Sugar
print("\nPatients with High BP and High Sugar:")

print(df[
    (df["Blood_Pressure"] > 140) &
    (df["Sugar_Level"] > 150)
])

