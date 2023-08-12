import tkinter as tk
from PIL import Image, ImageTk

def place_button(button, x, y):
    button.place(x=x, y=y)

# Create the main window
root = tk.Tk()
root.title("Image Background with Buttons")

# Load and display the image background
image = Image.open("background_image.jpg")  # Replace with your image file
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Place the buttons using x, y coordinates
place_button(button1, x=50, y=100)
place_button(button2, x=200, y=150)
place_button(button3, x=350, y=200)

# Start the tkinter main loop
root.mainloop()
