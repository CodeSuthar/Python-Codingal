from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denomination Breakdown Tool")
window.geometry("700x400")
window.configure(bg="#f0f4f7")

head = Label(window, text="Denomination Breakdown Tool", font=("Arial", 24), bg="#f0f4f7", fg="#333")
head.pack(pady=10)


main_frame = Frame(window, bg="#f0f4f7")
main_frame.pack(pady=10, padx=20, fill=X)

input_frame = Frame(main_frame, bg="white", bd=2, relief=GROOVE)
input_frame.pack(side=LEFT, padx=10, fill=Y)

input_label = Label(input_frame, text="Enter Amount:", font=("Arial", 14), bg="white", anchor="w")
input_label.pack(pady=(20, 5), padx=10, anchor="w")

amount_entry = Entry(input_frame, font=("Arial", 14), width=20)
amount_entry.pack(pady=5, padx=10)

calc_btn_frame = Frame(input_frame, bg="white")
calc_btn_frame.pack(pady=10)

def reset_fields():
    amount_entry.delete(0, END)
    for e in [e_2000, e_500, e_100]:
        e.config(state=NORMAL)
        e.delete(0, END)
        e.config(state='readonly')

def calculate_breakdown():
    try:
        amt = int(amount_entry.get())
        n2000 = amt // 2000
        amt %= 2000
        n500 = amt // 500
        amt %= 500
        n100 = amt // 100
        amt %= 100

        for e in [e_2000, e_500, e_100]:
            e.config(state=NORMAL)
            e.delete(0, END)
        
        e_2000.insert(0, str(n2000))
        e_500.insert(0, str(n500))
        e_100.insert(0, str(n100))

        for e in [e_2000, e_500, e_100]:
            e.config(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

Button(calc_btn_frame, text="Calculate", command=calculate_breakdown, font=("Arial", 14), bg="#4CAF50", fg="white").pack(side=LEFT, padx=5)

Button(calc_btn_frame, text="Reset", command=reset_fields, font=("Arial", 14), bg="#f44336", fg="white").pack(side=LEFT, padx=5)

output_frame = Frame(main_frame, bg="white", bd=2, relief=GROOVE)
output_frame.pack(side=RIGHT, padx=10, fill=Y)

Label(output_frame, text="Denomination Breakdown:", font=("Arial", 12, 'bold'), bg="white").pack(pady=20)

def create_readonly_entry(label_text):
    row = Frame(output_frame, bg="white")
    row.pack(pady=5, padx=20)
    Label(row, text=label_text, font=("Arial", 11), bg="white").pack(side=LEFT)
    entry = Entry(row, width=10, font=("Arial", 11), justify='center')
    entry.pack(side=RIGHT)
    entry.config(state='readonly')
    return entry

e_2000 = create_readonly_entry("₹2000 Notes:")
e_500 = create_readonly_entry("₹500 Notes:")
e_100 = create_readonly_entry("₹100 Notes:")

try:
    Logo = ImageTk.PhotoImage(Image.open("app.png").resize((100, 100)))
    LastLabel = Label(window, image=Logo, bg="#f0f4f7")
    LastLabel.pack(side=BOTTOM, pady=10)
except FileNotFoundError:
    LastLabel = Label(window, text="Logo not found", bg="#f0f4f7", font=("Arial", 12), fg="red")
    LastLabel.pack(side=BOTTOM, pady=10)

window.mainloop()
