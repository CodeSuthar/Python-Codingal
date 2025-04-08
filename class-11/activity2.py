class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def printName(self):
        print("Name: ", self.fname + " " + self.lname)

class Student(Person):
    def __init__(self, fname, lname, age, student_id, graduation_year):
        super().__init__(fname, lname, age)
        self.student_id = student_id
        self.graduation_year = graduation_year

stud = Student("John", "Doe", 20, "S12345", 2023)
stud.printName()
print("Age: ", stud.age)
print("Student ID: ", stud.student_id)
print("Graduation Year: ", stud.graduation_year)

