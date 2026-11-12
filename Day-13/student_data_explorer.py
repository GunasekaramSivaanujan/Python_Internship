import pandas as pd

# Student Names
names= pd.Series([
    "Arun",
    "Sivaa",
    "Susmi",
    "Ravi",
    "Abi",
    "Kavi",
    "Banu",
    "Sinthu",
    "Babi",
    "Thanu"
])

# Student Ages
ages = pd.Series([20,21,22,19,20,18,16,18,22,16])

# Student Python Marks
python_marks = pd.Series([85,65,90,45,75,65,82,93,55,71])

# Student AI Marks 
ai_marks = pd.Series([90,80,95,55,80,56,78,72,50,90])

# Display Student Names
print("student Names")
print(names)

# Display Student Ages
print("Student Ages")
print(ages)

# Display Python Marks
print("Python Marks")
print(python_marks)

# Display AI Marks
print("AI Marks")
print(ai_marks)

# Student with Highest Python Marks
highest_index = python_marks.idxmax()
print("Student with Highest Python Marks")
print(names[highest_index])
print(python_marks[highest_index])

# Student with Lowest Python Marks
lowest_index = python_marks.idxmin()
print("Student with Lowest Python Marks")
print(names[lowest_index])
print(python_marks[lowest_index])

# Student with Highest AI Marks
highest_ai_index = ai_marks.idxmax()
print("Student with Highest AI Marks")
print(names[highest_ai_index])
print(ai_marks[highest_ai_index])

# Student with Lowest AI Marks
lowest_ai_index = ai_marks.idxmin()
print("Student with Lowest AI Marks")
print(names[lowest_ai_index])
print(ai_marks[lowest_ai_index])

# Average Marks
print("Average Python Marks")
print(python_marks.mean())
print("Average AI Marks")
print(ai_marks.mean())

# Students Scoring Above 75
print("Students scoring above 75 in Python")
print(names[python_marks > 75])
print("Students scoring above 75 in AI")
print(names[ai_marks > 75])

# Number of Passing Students
print("Python Passing Students")
print((python_marks >= 50).sum())
print("AI Passing Students")
print((ai_marks >= 50).sum())

# Custom Index
student_ids = ["S001", "S002", "S003", "S004", "S005","S006","S007","S008","S009","S010"]
student_scores = pd.Series(
    python_marks.values,
    index=student_ids
)

print("Student Scores with IDs")
print(student_scores)