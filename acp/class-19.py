import os
from collections import OrderedDict

def display_file(filename):
    try:
        with open(filename, 'r') as file:
            print("\nCurrent file content:")
            print(file.read())
    except FileNotFoundError:
        print("File doesn't exist yet. Create it first.")

def write_to_file(filename):
    content = input("\nEnter content to write (will overwrite existing):\n")
    with open(filename, 'w') as file:
        file.write(content)
    print("Content written successfully.")

def append_to_file(filename):
    content = input("\nEnter content to append:\n")
    with open(filename, 'a') as file:
        file.write(content + "\n")
    print("Content appended successfully.")

def delete_duplicate_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        unique_lines = list(OrderedDict.fromkeys(lines))
        
        with open(filename, 'w') as file:
            file.writelines(unique_lines)
        
        print(f"Removed {len(lines) - len(unique_lines)} duplicate lines.")
    except FileNotFoundError:
        print("File not found.")

def count_lines_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            
            print(f"\nFile statistics:")
            print(f"Lines: {len(lines)}")
            print(f"Words: {len(words)}")
            print(f"Characters: {len(content)}")
    except FileNotFoundError:
        print("File not found.")

def search_in_file(filename):
    try:
        search_term = input("\nEnter search term: ")
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if search_term in line:
                    print(f"Found at line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print("File not found.")

def main():
    print("File Manipulation Tool")
    print("----------------------")
    
    filename = input("Enter filename to work with: ")
    
    while True:
        print("\nMenu Options:")
        print("1. Display file content")
        print("2. Write to file (overwrite)")
        print("3. Append to file")
        print("4. Delete duplicate lines")
        print("5. Count lines, words, characters")
        print("6. Search in file")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            display_file(filename)
        elif choice == '2':
            write_to_file(filename)
        elif choice == '3':
            append_to_file(filename)
        elif choice == '4':
            delete_duplicate_lines(filename)
        elif choice == '5':
            count_lines_words(filename)
        elif choice == '6':
            search_in_file(filename)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()