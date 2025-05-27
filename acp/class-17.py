def read_file(filename):
    """Read and display the entire file content"""
    try:
        with open(filename, 'r') as file:
            print("\nFile content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_line_by_line(filename):
    """Read and display file content line by line"""
    try:
        with open(filename, 'r') as file:
            print("\nFile content (line by line):")
            for i, line in enumerate(file, 1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file(filename):
    """Append content to the file"""
    try:
        content = input("\nEnter content to append: ")
        with open(filename, 'a') as file:
            file.write(content + "\n")
        print("Content appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def overwrite_file(filename):
    """Overwrite the file with new content"""
    try:
        content = input("\nEnter new content (will overwrite existing): ")
        with open(filename, 'w') as file:
            file.write(content + "\n")
        print("File overwritten successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_binary_file(filename):
    """Read file in binary mode"""
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            print("\nBinary content (first 100 bytes):")
            print(content[:100])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("File Operations Menu")
    print("--------------------")
    
    filename = input("Enter the filename: ")
    
    while True:
        print("\nChoose an operation:")
        print("1. Read entire file")
        print("2. Read file line by line")
        print("3. Append to file")
        print("4. Overwrite file")
        print("5. Read file in binary mode")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            read_file(filename)
        elif choice == '2':
            read_line_by_line(filename)
        elif choice == '3':
            append_to_file(filename)
        elif choice == '4':
            overwrite_file(filename)
        elif choice == '5':
            read_binary_file(filename)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()