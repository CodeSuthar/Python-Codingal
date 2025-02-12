class someClass:
    def __init__(self, name):
        self.name = name

    def printActivitySinging(self, singingSongName):
        print(f'{self.name} is singing {singingSongName}')

    def printActivityDancing(self, dancingSongName):
        print(f'{self.name} is dancing on {dancingSongName}')

obj = someClass('Aditya Suthar')
obj.printActivitySinging('Tum Hi Ho')
obj.printActivityDancing('Saath Hum Rahein')