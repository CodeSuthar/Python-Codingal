class Student():
    species = 'Human'
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Student('Aditya Suthar', 16)

print(f'Hello, I am {obj.name} and I am {obj.age} years old and Yes! I am are {obj.species} - Printed via Object, Attribute and Function')