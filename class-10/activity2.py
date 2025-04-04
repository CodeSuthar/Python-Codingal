import json

class Library:
    def __init__(self, booklist, name):
        self.booksList = booklist
        self.name = name
        self.lendedBooks = {}

    def displayBooks(self):
        print(f"\nBooks available in {self.name}:")
        for book in self.booksList:
            print(f" - {book}")

    def lendBook(self, book, user):
        if book not in self.booksList:
            print(f"Sorry, '{book}' is not available in the library.")
        elif book in self.lendedBooks:
            print(f"Sorry, '{book}' is already lent to {self.lendedBooks[book]}.")
        else:
            self.lendedBooks[book] = user
            print(f"{user} has borrowed '{book}'.")

    def addBook(self, book):
        self.booksList.append(book)
        print(f"'{book}' has been added to the library.")

    def returnBook(self, book):
        if book not in self.lendedBooks:
            print(f"'{book}' was not lent out.")
        else:
            del self.lendedBooks[book]
            print(f"'{book}' has been returned to the library.")

# Load users from JSON
def load_users():
    try:
        with open("user.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"data": []}

# Save users to JSON
def save_users(users):
    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)

# Find user by username
def get_user_by_username(users, username):
    for user in users["data"]:
        if user["username"] == username:
            return user
    return None

if __name__ == '__main__':
    library = Library(["Python", "Java", "C++"], "Central Library")
    users = load_users()

    username = input("Enter your username (Case Sensitive): ").strip()
    user = get_user_by_username(users, username)

    if not user:
        print("User not found!")
        exit()

    is_admin = user.get("admin", False)

    while True:
        print(f"\nWelcome to the Library! - User: {username} {'(Admin)' if is_admin else ''}")

        if is_admin:
            print("\n========= Admin Menu =========")
            print("1. Display Books")
            print("2. Lend Book")
            print("3. Add Book")
            print("4. Return Book")
            print("5. Create User")
            print("6. Delete User")
            print("7. Exit")
            print("==============================")
        else:
            print("\n========= User Menu =========")
            print("1. Display Books")
            print("2. Lend Book")
            print("3. Add Book")
            print("4. Return Book")
            print("5. Exit")
            print("=============================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            library.displayBooks()

        elif choice == 2:
            book_name = input("Enter the name of the book you want to lend: ").strip()
            library.lendBook(book_name, username)

        elif choice == 3:
            book_name = input("Enter the name of the book you want to add: ").strip()
            library.addBook(book_name)

        elif choice == 4:
            book_name = input("Enter the name of the book you want to return: ").strip()
            library.returnBook(book_name)

        elif is_admin and choice == 5:
            new_username = input("Enter the new username (Case Sensitive): ").strip()
            new_name = input("Enter the full name: ").strip()
            admin_input = input("Is the user an admin? (yes/no): ").strip().lower()
            is_new_admin = True if admin_input == "yes" else False

            if get_user_by_username(users, new_username):
                print("Username already exists!")
            else:
                new_id = max([u["id"] for u in users["data"]], default=0) + 1
                new_user = {
                    "id": new_id,
                    "name": new_name,
                    "username": new_username,
                    "admin": is_new_admin
                }
                users["data"].append(new_user)
                save_users(users)
                print(f"User '{new_username}' created successfully.")

        elif is_admin and choice == 6:
            del_username = input("Enter the username to delete: ").strip()
            if del_username == username:
                print("You cannot delete yourself.")
            else:
                user_to_delete = get_user_by_username(users, del_username)
                if user_to_delete:
                    users["data"] = [u for u in users["data"] if u["username"] != del_username]
                    save_users(users)
                    print(f"User '{del_username}' has been deleted.")
                else:
                    print("User not found.")

        elif (not is_admin and choice == 5) or (is_admin and choice == 7):
            print("Thank you for using the library system!")
            break

        else:
            print("Invalid choice. Please try again.")