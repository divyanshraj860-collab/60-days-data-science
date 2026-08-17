# Day 1 - Python Fundamentals Bootcamp

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))

# Calculating yearly salary
yearly_salary = salary * 12

# Storing data in a dictionary
employee = {
    "name": name,
    "age": age,
    "monthly_salary": salary,
    "yearly_salary": yearly_salary
}
# Displaying the result
print("\n--- Employee Details ---")
print("Name:", employee["name"])
print("Age:", employee["age"])
print("Monthly Salary:", employee["monthly_salary"])
print("Yearly Salary:", employee["yearly_salary"])