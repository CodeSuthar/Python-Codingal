from tkinter import *

def create_window():
    window = Tk()
    window.title("My First GUI")
    window.geometry('400x400')

    greeting_label = Label(window, text="Hello, Anonymous User", bg="#3B0086")
    interactive_button = Button(window, text="Click Me", command=lambda: greeting_label.config(text="You changed me user!"), bg="#6200B3", fg="white")
    text_area = Entry(window, width=60, bg="#6200B3", fg="white")

    frame = Frame(window, bg="#3B0086", borderwidth=6, relief="raised")
    label = Label(frame, text="This is a frame", bg="#3B0086", fg="white")

    textbox = Text(window, height=10, width=30, bg="#6200B3", fg="white")

    greeting_label.pack()
    interactive_button.pack()
    text_area.pack()
    frame.pack()
    label.pack()
    textbox.pack()
    
if __name__ == "__main__":
    create_window()
    mainloop()