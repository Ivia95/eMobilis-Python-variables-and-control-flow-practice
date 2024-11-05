# Base class
class Employee:
    def calculate_salary(self):
        print("Calculating salary for employee...")

# Subclass
class Manager(Employee):
    def calculate_salary(self):
        base_salary = 50000
        bonus = 10000
        total_salary = base_salary + bonus
        print(f"Calculating salary for manager: {total_salary}")

# Demonstrate the overridden behavior
# Creating an instance of Employee
employee = Employee()
employee.calculate_salary()

# Creating an instance of Manager
manager = Manager()
manager.calculate_salary()
