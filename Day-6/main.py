import numpy as np

# Empolyee Salary Data cleaning System
employee_id = np.array([101,102,103,104,105,106])

# Empoloyee Age
age = np.array([25,30,28,35,40,32])

# Empoloyee Department
department = np.array(["IT,HR,Finance,IT,HR,Finance"])

# Empolotee Salary
salary = np.array([30000,45000,-5000,60000,35000,50000])

# Empoloyee Experience 
experience = np.array([2,5,3,8,4,6])

# Empoloyee Performance Score
performance = np.array([85,95,75,92,88,98])

# Increase Salary by 10%
increased_salary = salary * 1.10
print("Salary After 10% Increase:" , increased_salary)

# Replace Negative Salary
cleaned_salary = np.where(salary < 0, 0, salary)
print("Cleaned Salary:" , cleaned_salary)

# Fliter Performance Above 90
high_performance = performance[performance > 90]
print("High Performance Scores:" , high_performance)

# Fliter Above Average Salary
average_salary = np.mean(cleaned_salary)
above_average = cleaned_salary[cleaned_salary > average_salary]
print("Averageb Salary:" , average_salary)
print("Above Average Salary:", above_average)

# Reshape Employee Salary
reshaped_salary = cleaned_salary.reshape(2,3)
print("Reshaped Salary:" )
print(reshaped_salary)

# Transpose Employee Salary 
transposed_salary = reshaped_salary.transpose()
print("Transposed Salary:")
print(transposed_salary)\

# Final Cleaned Dataset Summary

print("\n----- Final Employee Salary Summary -----")

print("Total Employees:", len(employee_id))
print("Cleaned Salaries:", cleaned_salary)
print("Average Salary:", average_salary)
print("High Performance Scores:", high_performance)
print("Above Average Salaries:", above_average)

# Display Employee Dataset
print("Employee Salary Data Cleaning System")

print("Employee ID:",employee_id)
print("Age:", age)
print("Department:", department)
print("Salary:", salary)
print("Experience:", experience)
print("Performance:", performance)


