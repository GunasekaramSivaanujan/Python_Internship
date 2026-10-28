
students = {}

def add_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter Student Marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Please enter valid marks!")
        return

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found!")
        return

    for student_id, details in students.items():
        print(f"ID: {student_id} | Name: {details['name']} | Marks: {details['marks']}")

def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        details = students[student_id]
        print(f"ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
        print(f"Grade: {calculate_grade(details['marks'])}")
    else:
        print("Student not found!")

def update_marks():
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found!")
        return

    try:
        marks = float(input("Enter new marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Please enter valid marks!")
        return

    students[student_id]["marks"] = marks
    print("Marks updated successfully!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def calculate_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 35:
        return "S"
    else:
        return "F"

def grade_report():
    if not students:
        print("No students available!")
        return

    total_marks = 0
    top_student_id = None
    highest_marks = -1

    print("\n--- Student Grade Report ---")

    for student_id, details in students.items():
        marks = details["marks"]
        grade = calculate_grade(marks)

        print(
            f"ID: {student_id} | "
            f"Name: {details['name']} | "
            f"Marks: {marks} | Grade: {grade}"
        )

        total_marks += marks

        if marks > highest_marks:
            highest_marks = marks
            top_student_id = student_id

    average = total_marks / len(students)

    print(f"\nAverage Marks: {average:.2f}")

    top_student = students[top_student_id]
    print(
        f"Top Performer: {top_student['name']} "
        f"({highest_marks} marks)"
    )

def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Display Grade Report")
        print("7. Exit Application")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            grade_report()
        elif choice == "7":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()