class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"I am a person. My name is {self.name}.")

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def display_employee(self):
        print(f"I am an employee. My employee ID is {self.emp_id}.")

class Manager(Employee,Person):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, emp_id)
        Person.__init__(self, name)
        
        self.department = department

    def display_manager(self):
        print(f"I am a manager. I manage the {self.department} department.")

# Taking input from the user
name = input("Enter the name of the manager: ")
emp_id = input("Enter the employee ID of the manager: ")
department = input("Enter the department the manager handles: ")

# Creating an object of the Manager class
manager = Manager(name, emp_id, department)
manager.display_person()
manager.display_employee()
manager.display_manager()
