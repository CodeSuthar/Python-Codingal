def conversion(data):
    result = {}
    for item in data:
        result[item[0]] = item[1:]
    return result

students = [
    [1, "Aditya K. Suthar", 15],
    [2, "Krisha Patel", 15],
    [3,"Vyom Varia", 15],
    [4,"Param Mistry", 15],
    [5,"Shaurya Patel", 15],
    [6,"Jiya Darji", 15]
]

print("-----------------")
print(f"| - 1. Students: {students}")
print(f"| - 2. Conversion: {conversion(students)}")
print("-----------------")