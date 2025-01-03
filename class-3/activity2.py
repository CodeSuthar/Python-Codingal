height = float(input("Enter your height in centimeter: "))
weight = float(input("Enter your weight in kilogram: "))

bmi = weight / (height / 100) ** 2

if bmi <= 18.4:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif bmi <= 24.9:
    print(f"Your BMI is {bmi:.2f}. You are normal weight.")
elif bmi <= 29.9:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
elif bmi <= 34.9:
    print(f"Your BMI is {bmi:.2f}. You are severely overweight.")
elif bmi <= 39.9:
    print(f"Your BMI is {bmi:.2f}. You are obese.")
else: 
    print(f"Your BMI is {bmi:.2f}. You are severely obese.")