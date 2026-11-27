import pandas as pd
import matplotlib.pyplot as plt

# Load Student Dataset
df = pd.read_csv("Day-23/student_data.csv")

# Display First 5 Student Records
print("\nStudent Performance Dataset:")
print(df.head())

# Display Dataset Information
print("\nDataset Information:")
print(df.info())

# Calculate Total Marks
df["Total Marks"] = (
    df["Math"]
    + df["Science"]
    + df["Python"]
    + df["AI"]
)
# Display Student Total Marks
print("\nStudent Total Marks:")
print(df[["Student Name", "Total Marks"]])

# Calculate Average Marks
df["Average Marks"] = df["Total Marks"] / 4

# Display Student Average Marks
print("\nStudent Average Marks:")
print(df[["Student Name", "Average Marks"]])

# Line Chart - Student vs Total Marks
plt.figure(figsize=(12, 6))
plt.plot(
    df["Student Name"],
    df["Total Marks"],
    marker="o",
    label="Total Marks"
)
# Add Chart Title and Labels
plt.title("Student vs Total Marks")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")

# Display Student Names Clearly
plt.xticks(rotation=45)

# Display Legend
plt.legend()

# Display Chart
plt.tight_layout()
plt.show()

# Bar Chart - Student vs Average Marks
plt.figure(figsize=(12, 6))
plt.bar(
    df["Student Name"],
    df["Average Marks"],
    label="Average Marks"
)
# Add Chart Title and Labels
plt.title("Student vs Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

# Rotate Student Names
plt.xticks(rotation=45)

# Display Legend
plt.legend()

# Display Chart
plt.tight_layout()
plt.show()

# Assign Grades Based on Average Marks
def assign_grade(average):

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"


df["Grade"] = df["Average Marks"].apply(assign_grade)

# Pie Chart - Grade Distribution
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

# Add Chart Title
plt.title("Student Grade Distribution")

# Display Legend
plt.legend(title="Grades")

# Display Chart
plt.show()

# Find Top 5 Students
top_5_students = df.nlargest(5, "Total Marks")

print("\nTop 5 Students:")
print(top_5_students[["Student Name", "Total Marks"]])

# Bar Chart - Top 5 Students
plt.figure(figsize=(10, 6))

plt.bar(
    top_5_students["Student Name"],
    top_5_students["Total Marks"],
    label="Total Marks"
)
# Add Chart Title and Labels
plt.title("Top 5 Students Performance")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")

# Display Legend
plt.legend()

# Display Chart
plt.tight_layout()
plt.show()


