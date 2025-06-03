import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8 or length > 32:
            messagebox.showerror("Error", "Password length must be between 8 and 32")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

root = tk.Tk()
root.title("Simple Password Generator")

password_var = tk.StringVar()

tk.Label(root, text="Password Length (8-32):").pack(pady=5)

length_entry = tk.Entry(root, width=5)
length_entry.pack()
length_entry.insert(0, "12") 

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, textvariable=password_var, width=30, justify='center')
password_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

root.mainloop()