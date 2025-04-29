class Robot:
    """
    Represents a robot with a name.
    """

    def __init__(self, name):
        """
        Initializes the robot with a name.

        Args:
            name (str): The name of the robot.
        """
        self.name = name

    def introduce_self(self):
        """
        Introduces the robot by printing its name.
        """
        print(f"Hello, I am {self.name}!")


if __name__ == "__main__":
    tom = Robot("Tom")
    jerry = Robot("Jerry")

    tom.introduce_self()
    jerry.introduce_self()