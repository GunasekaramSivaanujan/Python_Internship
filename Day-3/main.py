import numpy as np

student_id = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
])

age = np.array([
    18, 19, 18, 20, 19, 18, 21, 20, 19, 18,
    20, 19, 21, 18, 20, 19, 18, 21, 20, 19
])

math_marks = np.array([
    85, 72, 91, 68, 77, 88, 65, 79, 90, 74,
    81, 69, 95, 73, 84, 76, 89, 62, 93, 80
])

science_marks = np.array([
    80, 75, 89, 70, 82, 91, 68, 77, 85, 73,
    84, 71, 94, 76, 88, 79, 90, 65, 92, 81
])

english_marks = np.array([
    78, 80, 85, 65, 75, 90, 70, 82, 88, 76,
    83, 72, 96, 79, 86, 74, 91, 67, 89, 81
])

print("Student IDs:", student_id)
print("Student Ages:", age)
print("Math Marks:", math_marks)
print("Science Marks:", science_marks)
print("English Marks:", english_marks)
print("Student ID Shape:", student_id.shape)
print("Student ID Dimensions:", student_id.ndim)
print("Student ID Size:", student_id.size)
print("Student ID Data Type:", student_id.dtype)
print("Math Marks Shape:", math_marks.shape)
print("Math Marks Dimensions:", math_marks.ndim)
print("Math Marks Size:", math_marks.size)
print("Math Marks Data Type:", math_marks.dtype)

import time

# Python List
marks_list = [
    85, 72, 91, 68, 77, 88, 65, 79, 90, 74,
    81, 69, 95, 73, 84, 76, 89, 62, 93, 80
]

start_time = time.time()

for i in range(100000):
    total = sum(marks_list)

list_time = time.time() - start_time

# NumPy Array
start_time = time.time()

for i in range(100000):
    total = np.sum(math_marks)

numpy_time = time.time() - start_time

print("Python List Time:", list_time)
print("NumPy Array Time:", numpy_time)

# 3D Array
marks_3d = np.array([
    [
        [85, 80, 78],
        [72, 75, 80]
    ],
    [
        [91, 89, 85],
        [68, 70, 65]
    ]
])

print("3D Array:")
print(marks_3d)

print("3D Array Shape:", marks_3d.shape)
print("3D Array Dimensions:", marks_3d.ndim)
print("3D Array Size:", marks_3d.size)

# Student Marks Summary

total_marks = math_marks + science_marks + english_marks

average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# 2D Array - Student Marks

all_marks = np.array([
    math_marks,
    science_marks,
    english_marks
])

print("All Students Marks:")
print(all_marks)

print("Array Shape:", all_marks.shape)
print("Array Dimensions:", all_marks.ndim)
print("Array Size:", all_marks.size)

# Highest and Lowest Marks

print("Highest Math Mark:", np.max(math_marks))
print("Lowest Math Mark:", np.min(math_marks))

print("Highest Science Mark:", np.max(science_marks))
print("Lowest Science Mark:", np.min(science_marks))

print("Highest English Mark:", np.max(english_marks))
print("Lowest English Mark:", np.min(english_marks))

# Find the Best Student

best_student = np.argmax(average_marks)

print("Best Student ID:", student_id[best_student])
print("Highest Average Mark:", average_marks[best_student])

# Student Result Summary

print("\nSTUDENT RESULT SUMMARY")
print("-" * 75)

for i in range(20):
    if average_marks[i] >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    print(
        "ID:", student_id[i],
        "| Age:", age[i],
        "| Math:", math_marks[i],
        "| Science:", science_marks[i],
        "| English:", english_marks[i],
        "| Total:", total_marks[i],
        "| Average:", round(average_marks[i], 2),
        "| Result:", result
    )
    