import numpy as np
import csv

# AI Data Preprocessing Pipeline 
student_id = np.arange(101,201)

# Student Age
age = np.random.randint(18,28, 100)


# Student Marks
marks = np.random.randint(0,101, 100)

# Student Attendance
attendance = np.random.randint(50,101, 100)

# Add Missing Values
marks = marks.astype(float)
marks[5] = np.nan

# Check Missing Values
missing_values = np.isnan(marks)
print("Missing Values:", missing_values)
print("Total Missing values:", np.sum(missing_values))

# Replace Missing Values
average_marks = np.nanmean(marks)
cleaned_marks = np.where(np.isnan(marks), average_marks, marks)
print("average Marks:", average_marks)
print("Cleaned Marks:", cleaned_marks)

# Filiter Student With Marks Above 50
passed_students = cleaned_marks[cleaned_marks >= 50]
print("Passed Students Marks:", passed_students)

# Find Highest Marks
highest_marks = np.max(cleaned_marks)
print("Highest Marks:", highest_marks)

# Find lowest Marks
lowest_marks = np.min(cleaned_marks)
print("Lowest Marks:", lowest_marks)

# Calculate Average Marks
average = np.mean(cleaned_marks)
print("Averge Marks:", average_marks)

# Calculate Median Marks
median_marks = np.median(cleaned_marks)
print("Median Marks:", median_marks)

# Calculate Standard Deviation
std_deviation = np.std(cleaned_marks)
print("Standard Deviation:", std_deviation)

# Filter Students By Attendance
high_attendance = attendance[attendance >= 75]
print("High Attendance:", high_attendance)

# Calculate Pass Percentage
pass_count = np.sum(cleaned_marks >= 50)
pass_percentage = (pass_count / len(cleaned_marks)) * 100
print("Total Passed Students:", pass_count)
print("Pass Percentage:", pass_percentage)

# Reshape Student Marks
reshaped_marks = cleaned_marks.reshape(10,10)
print("Reshaped Marks;")
print(reshaped_marks)

# Check Dataset Information
print("Total Student:", len(student_id))
print("Dataset Shape:", cleaned_marks.shape)
print("Dataset Size:", cleaned_marks.size)

# Create Final Dataset
final_dataset = np.column_stack((
    student_id,
    age,
    cleaned_marks,
    attendance
))
print("Final Student Dataset:")
print(final_dataset)

# Save Dataset as csv
np.savetxt(
    "student_performance.csv",
    final_dataset,
    fmt="%.2f",
    header="Student_ID,Age,Marks,Attendance",
    comments=""
)
print("Dataset Saved Successfully!")

# Final Project Summary
print("\n===== STUDENT PERFORMANCE SUMMARY =====")
print("Total Students:", len(student_id))
print("Average Marks:", average)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Median Marks:", median_marks)
print("Pass Percentage:", pass_percentage)
print("Average Attendance:", np.mean(attendance))

