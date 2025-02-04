myset = {1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5}
set1 = myset
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"---------------------------")
print(f"Diffrence: \"{set2.difference(set1)}\"")
print(f"Symmetric Difference: \"{set1.symmetric_difference(set2)}\" ")
print(f"---------------------------")
