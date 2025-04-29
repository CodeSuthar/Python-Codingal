class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_sum(self):
        total = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {total}")


if __name__ == "__main__":
    expression = Expression(10, 20, 30)

    expression.calculate_sum()