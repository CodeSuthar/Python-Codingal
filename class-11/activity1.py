class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("-------Person Information-------")
        print("Name: ", self.name)
        print("ID Number: ", self.idnumber)
        print("---------------------------------")

class Student(Person):
    def __init__(self, name, idnumber, course):
        super().__init__(name, idnumber)
        self.course = course

        Person.__init__(self, name, idnumber)


a = Student("John Doe", "12345", "Computer Science")
a.display()