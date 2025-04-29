x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))

values = [x, y, z]
values.sort()

x, y, z = values[0], values[1], values[2]

print("After sorting:")
print("x =", x)
print("y =", y)
print("z =", z)
