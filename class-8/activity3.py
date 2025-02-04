SetX = {"Aditya", "Vyom", "Param", "Shaurya", "Krisha"}
SetY = {"Krisha", "Jiya", "Vanshika", "Krishna", "Hetvi", "Aditya", "Vyom"}

print(f"---------------------------------")
print(f"Set X: {SetX}")
print(f"Set Y: {SetY}")
print(f"---------------------------------")
SetZ = SetX.intersection(SetY)
SetU = SetX.union(SetY)
print(f"Intersection: {SetZ}")
print(f"Union: {SetU}")
print(f"---------------------------------")