class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
    
    def __del__(self):
        print(f"Employee {self.name} is being deleted")

obj = Employee("John Doe", 50000)

print(obj)

del obj