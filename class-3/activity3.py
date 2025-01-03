print("Welcome to the registration form!")

email = input("Enter your email address: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))

# Check if the user is 18 or older
if age >= 18:
    # Validate email
    if "@" in email and "." in email:
        print("Email looks valid.")
    else:
        print("Invalid email address. Please try again.")
    
    # Check password length
    if len(password) >= 8:
        print("Password is valid.")
    else:
        print("Password should be at least 8 characters long.")
else:
    print("You must be older than 18 to register.")
    exit()

print("Thank you for registering!")
print(f"Email: {email}")
print(f"Password: {'*' * len(password)}")
print(f"Age: {age}")