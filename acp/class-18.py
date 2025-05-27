def read_entire_file(filename):
    with open(filename, 'r') as file:
        print("\n=== Entire File ===\n" + file.read())

def read_line_by_line(filename):
    with open(filename, 'r') as file:
        print("\n=== Line by Line ===")
        for i, line in enumerate(file, 1):
            print(f"Line {i}: {line.strip()}")

def read_with_readlines(filename):
    with open(filename, 'r') as file:
        print("\n=== readlines() ===")
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def read_in_chunks(filename):
    with open(filename, 'r') as file:
        print("\n=== In Chunks ===")
        while True:
            chunk = file.read(50)
            if not chunk:
                break
            print(chunk, end='')

def main():
    filename = input("Enter filename to read: ")
    
    while True:
        print("\n--- File Reader Menu ---")
        print("1. Read entire file")
        print("2. Read line by line")
        print("3. Read with readlines()")
        print("4. Read in chunks")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            read_entire_file(filename)
        elif choice == '2':
            read_line_by_line(filename)
        elif choice == '3':
            read_with_readlines(filename)
        elif choice == '4':
            read_in_chunks(filename)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()