from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import requests
from io import BytesIO
import urllib.request

# Setup Tkinter Window
root = Tk()
root.title("Yes/No Oracle")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Frame to hold the GIF
gif_frame = Frame(root, bg="#f0f0f0")
gif_frame.pack(pady=20)

# Label to display the GIF
gif_label = Label(gif_frame, bg="#f0f0f0")
gif_label.pack()

# Function to fetch and display the GIF
def fetch_yesno():
    try:
        # Fetch data from the API
        response = requests.get("https://yesno.wtf/api")
        data = response.json()
        answer = data["answer"].upper()
        gif_url = data["image"]

        # Download the GIF
        with urllib.request.urlopen(gif_url) as url_response:
            gif_data = url_response.read()

        # Open the GIF with PIL
        gif_image = Image.open(BytesIO(gif_data))
        gif_image = gif_image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(gif_image)

        # Update the label with the new GIF
        gif_label.config(image=photo)
        gif_label.image = photo  # Keep a reference

        # Update the answer label
        answer_label.config(text=f"The Oracle says: {answer}!", fg="green")

    except Exception as e:
        answer_label.config(text="Failed to fetch answer!", fg="red")

# Answer display label
answer_label = Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
answer_label.pack(pady=10)

# Button to fetch a new answer
fetch_button = Button(
    root,
    text="Ask the Oracle",
    command=fetch_yesno,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=5,
    relief="raised",
    bd=3
)
fetch_button.pack(pady=20)

root.mainloop()