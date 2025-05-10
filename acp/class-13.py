class Robot:

    def __init__(self, name):
        self.name = name

    def introduce_self(self):
        print(f"Hello, I am {self.name}!")


if __name__ == "__main__":
    tom = Robot("Tom")
    jerry = Robot("Jerry")

    tom.introduce_self()
    jerry.introduce_self()