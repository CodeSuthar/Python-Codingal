import tkinter as TKINTER

window = TKINTER.Tk("My Second GUI")

window.configure(bg="#6200B3")

for i in range(3):
    for j in range(3):
        frame = TKINTER.Frame(window, bg="#3B0086", borderwidth=6, relief="raised")
        label = TKINTER.Label(frame, text=f"Frame {i+1}, {j+1}", bg="#3B0086", fg="white")
        frame.grid(row=i, column=j, padx=10, pady=10)
        label.pack(padx=10, pady=10)

window.mainloop()