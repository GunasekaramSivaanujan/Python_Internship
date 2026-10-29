def collect_marks():
    marks=[]

    for i in range(10):
        mark =float(input("Enter student mark:"))
        marks.append(mark)

    return marks

def calculate_mean(marks):
    total = sum(marks)
    mean = total/ len(marks)
    return mean

def calculate_median(marks):
    sorted_marks = sorted(marks)
    n = len(sorted_marks)

    if n % 2 == 1:
        median = sorted_marks[n // 2]

    else:
        middle1 = sorted_marks[n // 2-1]
        middle2 = sorted_marks[n //2]
        median = (middle1 + middle2) / 2

    return median

def calculate_maximum(marks):
    return max(marks)

def calculate_minimum(marks):
    return min (marks)

def calculate_variance(marks):
    mean = calculate_mean(marks)
    squared_differences = []
    
    for mark in marks:
        difference = mark - mean
        squared_difference = difference ** 2
        squared_differences.append(squared_difference)

    variance = sum(squared_differences) / len(marks)
    return variance

def calculate_pass_fail(marks):
    pass_marks = []
    fail_marks = []
    
    for mark in marks:
        if mark >= 50:
            pass_marks.append(mark)
        else:
            fail_marks.append(mark)

    return pass_marks, fail_marks

def calculate_percentage(pass_marks, fail_marks):
    total_students = len(pass_marks) + len(fail_marks)

    pass_percentage = (len(pass_marks) / total_students) * 100
    fail_percentage = (len(fail_marks) / total_students) * 100

    return pass_percentage, fail_percentage

def calculate_probability(marks):
    total_students = len(marks)

    passed = sum(1 for mark in marks if mark >= 50)
    failed = sum(1 for mark in marks if mark < 50)
    above_80 = sum(1 for mark in marks if mark > 80)

    pass_probability = passed / total_students
    fail_probability = failed / total_students
    above_80_probability = above_80 / total_students

    return pass_probability, fail_probability, above_80_probability

import matplotlib.pyplot as plt


def display_bar_chart(marks):
    students = list(range(1, len(marks) + 1))

    plt.bar(students, marks)

    plt.title("Student Exam Marks")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.ylim(0, 100)
    plt.show()

def display_line_chart(marks):
    students = list(range(1, len(marks) + 1))

    plt.plot(students, marks, marker="o")

    plt.title("Student Marks Line Graph")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()

def display_histogram(marks):
    plt.hist(marks, bins=5, edgecolor="black")

    plt.title("Student Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

    plt.show()

def display_scatter_plot(marks):
    students = list(range(1, len(marks) + 1))

    plt.scatter(students, marks)

    plt.title("Student Marks Scatter Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()

def display_student_results(marks):
    print("\n--- Student Results Summary ---")

    for i, mark in enumerate(marks, start=1):
        if mark >= 50:
            result = "Pass"
        else:
            result = "Fail"

        print(f"Student {i}: Marks = {mark}, Result = {result}")

def main():
    marks = collect_marks()
    print("Student Marks:",marks)

    mean = calculate_mean(marks)
    print("Mean:",mean)

    median = calculate_median(marks)
    print("Median:", median)

    maximum = calculate_maximum(marks)
    print("Maximum Score:",maximum)
    
    minimum = calculate_minimum(marks)
    print("Minimum Score:",minimum)

    variance = calculate_variance(marks)
    print("Variance:", variance)

    pass_marks, fail_marks = calculate_pass_fail(marks)
    print("Passed Students:", len(pass_marks))
    print("Failed Students:", len(fail_marks))
    print("pass Marks:", pass_marks)
    print("Fail Marks:", fail_marks)
    
    pass_percentage, fail_percentage = calculate_percentage(pass_marks, fail_marks)
    print("Pass Percentage:", pass_percentage, "%")
    print("Fail Percentage:", fail_percentage, "%")

    pass_prob, fail_prob, above_80_prob = calculate_probability(marks)
    print("Pass Probability:", pass_prob)
    print("Fail Probability:", fail_prob)
    print("Probability of scoring above 80:", above_80_prob)

    display_bar_chart(marks)
    display_line_chart(marks)
    display_histogram(marks)
    display_scatter_plot(marks)
    display_student_results(marks)
    
if   __name__ == "__main__":
      main()    