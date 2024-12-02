class Student:
    def __init__(self, name, age, marks):
        """Constructor to initialize student details."""
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        """Method to display student details."""
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        """Method to calculate grade based on marks."""
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "F"
        return grade

# Create a Student object
student1 = Student(name="Alice", age=20, marks=85)

# Display student details
student1.display_details()

# Calculate and display grade
grade = student1.calculate_grade()
print(f"Grade: {grade}")
