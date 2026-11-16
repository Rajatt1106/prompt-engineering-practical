class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


name = input("Enter student name: ")
marks = float(input("Enter marks: "))

student = Student(name, marks)
student.display()
