print(f"1. name function as string \n 2. age as string \n 3. age as integer")
command = input("Enter the command: ")

if command == "1":
    name = input("Enter your name: ")
    print(f"Hello {name}")
elif command == "2":
    age = input("Enter your age: ")
    print(f"Your age is {age}")
elif command == "3":
    age = input("Enter your age: ")
    if age.isdigit():
        print(int(age))
    else:
        print("Invalid input")