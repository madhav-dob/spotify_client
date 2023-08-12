import tkinter as tk

class MovableWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Movable Window")
        self.overrideredirect(1)

        # Create a label to act as a title bar for dragging
        self.title_bar = tk.Label(self, text="Drag here to move", bg="blue", fg="white", cursor="fleur")
        self.title_bar.pack(fill=tk.X)

        # Bind events for dragging the window
        self.title_bar.bind("<ButtonPress-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.drag)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_drag)

    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        deltax = event.x - self.start_x
        deltay = event.y - self.start_y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def stop_drag(self, event):
        self.start_x = None
        self.start_y = None

app = MovableWindow()
app.mainloop()
