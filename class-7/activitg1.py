list = ["Aditya K.Suthar", "Vyom Varia", "Param Mistry", "Shaurya Patel", "Jiya Darji"]

print("-----------------")
print(f"| - 1. Length of List: {len(list)}")
print(f"| - 2. First Element: {list[0]}")
print(f"| - 3. Last Element: {list[-1]}")
print("-----------------")

list.append("Krisha Patel")
print(f"| - 4. Append: {list}")
list.remove("Vyom Varia")
print(f"| - 5. Remove: {list}")

list.sort()
print(f"| - 6. Sort: {list}")

list.pop(1)
print(f"| - 7. Pop: {list}")

list.reverse()
print(f"| - 8. Reverse: {list}")

print("Multiplication of List: ", list * 2)

list.clear()
print(f"| - 9. Clear: {list}")
print("-----------------")