from tkinter import Tk, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from urllib.parse import urlparse

def display_image():
    url = url_entry.get()
    
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL")
    except:
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((256, 256))
        photo_img = ImageTk.PhotoImage(img)
        image_label.config(image=photo_img)
        image_label.image = photo_img
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Could not download the image from the URL")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

window = Tk()
window.title("Image from URL")
window.geometry("400x500")

url_label = Label(window, text="Enter Image URL:", font=("Garamond", 12))
url_label.pack(pady=(20, 5))

url_entry = Entry(window, width=50, font=("Garamond", 12))
url_entry.pack(pady=5)
url_entry.insert(0, "https://")

load_button = Button(window, text="Load Image", command=display_image, font=("Garamond", 12))
load_button.pack(pady=10)

image_label = Label(window)
image_label.pack(pady=20)

instruction_label = Label(window, text="Enter an image URL and click 'Load Image'", font=("Garamond", 12))
instruction_label.pack(pady=20)

window.mainloop()