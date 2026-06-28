class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


try:
    name = input("Enter Name: ")
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    manager = Manager(name, emp_id, salary, department)
    manager.display()

except ValueError:
    print("Invalid salary entered.")