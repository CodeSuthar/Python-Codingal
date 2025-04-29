class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Cat. My name is {self.name}. I am {self.age} year old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Dog. My name is {self.name}. I am {self.age} year old.")

    def make_sound(self):
        print("Bark")

CatCallable = Cat("Doraemon", -100)
DogCallable = Dog("Neymar", 4)

for animal in (CatCallable, DogCallable):
    animal.info()
    animal.make_sound()