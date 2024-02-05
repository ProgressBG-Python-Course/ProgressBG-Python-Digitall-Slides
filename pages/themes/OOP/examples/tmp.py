class Employee:
    """Represents an employee with a name, ID, salary, and department."""

    def __init__(self, name, emp_id, salary, department):
        """Initializes an Employee object with the given attributes."""
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

# Create 5 employee objects with different salaries
employees = [
    Employee("Ivan Petrov", 1234567890, 50000, "Engineering"),
    Employee("Maria Ivanova", 9876543210, 65000, "Marketing"),
    Employee("Mihail Georgiev", 2345678901, 48000, "Sales"),
    Employee("Alisa Stoyanova", 3456789012, 52000, "Human Resources"),
    Employee("Bogomil Nikolov", 5678901234, 70000, "Finance"),
]

# Find the employee with the highest salary
highest_earner = None
highest_salary = 0

for employee in employees:
    if employee.salary > highest_salary:
        highest_earner = employee
        highest_salary = employee.salary

# Print the details of the employee with the highest salary
print(f"Employee with the highest salary:")
print(f"Name: {highest_earner.name}")
print(f"ID: {highest_earner.emp_id}")
print(f"Salary: ${highest_salary}")
print(f"Department: {highest_earner.department}")
