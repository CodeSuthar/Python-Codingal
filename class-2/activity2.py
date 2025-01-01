num1 = 5
num2 = 10

resultArithmetic = {
    "addition": num1 + num2,
    "subtraction": num1 - num2,
    "multiplication": num1 * num2,
    "division": num1 / num2,
    "floordivision": num1 // num2,
    "modulus": num1 % num2,
    "exponent": num1 ** num2,
    "squareRoot": num1 ** 0.5
}

conditionalResult = {
    "isNum1EqualToNum2": num1 == num2,
    "isNum1NotEqualToNum2": num1 != num2,
    "isNum1GreaterThanNum2": num1 > num2,
    "isNum1LessThanNum2": num1 < num2,
}

resultEq = num1 / 2 + num2 ** 2 + 10

print("Variables:")
print(f"  num1: {num1}")
print(f"  num2: {num2}")

print("Result of Arithmetic Operations:")
for key, value in resultArithmetic.items():
    print(f"  {key}: {value}")

print("\nResult of Conditional Operations:")
for key, value in conditionalResult.items():
    print(f"  {key}: {value}")

print(f"\nResult of Equation: {resultEq}")