name = "Aditya Suthar"
age = 15
is_student = True
weight = "45.5"

print(f"Name: {name} ({type(name)})")
print(f"Age: {age} ({type(age)})")
print(f"Is Student: {is_student} ({type(is_student)})")
print(f"Weight: {weight} ({type(weight)})")

print("----------After Type Casting----------")

age = str(age)
is_student = str(is_student)
weight = float(weight)

print(f"Name: {name} ({type(name)})")
print(f"Age: {age} ({type(age)})")
print(f"Is Student: {is_student} ({type(is_student)})")
print(f"Weight: {weight} ({type(weight)})")