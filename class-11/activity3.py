from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk. What am I?")

class Fish(Animal):
    def move(self):
        print("I can swim. What am I?")

class Bird(Animal):
    def move(self):
        print("I can fly. What am I?")

class Dog(Animal):
    def move(self):
        print("I can run. What am I?")

class Cat(Animal):
    def move(self):
        print("I can fall on my feet from any height even if placed inversed. What am I?")

class Snake(Animal):
    def move(self):
        print("I can crawl. What am I?")

H = Human()
H.move()

F = Fish()
F.move()

B = Bird()
B.move()

D = Dog()
D.move()

C = Cat()
C.move()

S = Snake()
S.move()