my_tuple = () # Empty tuple
my_tuple2 = (1, 2, 3) # Tuple with integers
my_tuple3 = (1, 2, "Hello") # Tuple with mixed data types
my_tuple4 = ("Hello", [1, 2, 3], (4, 5, 6)) # Nested tuple
my_tuple5 = ("A", "D", "I", "T", "Y", "A") # Accessing using index

print(f"---------------------------")
print(f"Tuple 1: {my_tuple}")
print(f"Tuple 2: {my_tuple2}")
print(f"Tuple 3: {my_tuple3}")
print(f"Tuple 4: {my_tuple4}")
print(f"Tuple 5: {my_tuple5}")
print(f"---------------------------")
print(f"Accessing using index: {my_tuple5[0]}")
print(f"Nested indexing: {my_tuple4[1][2]}")
print(f"Slicing: {my_tuple5[1:4]}")
print(f"---------------------------")
for letter in (my_tuple4):
    print("Hello", letter)
print(f"---------------------------")