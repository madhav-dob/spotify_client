# Import module
from tkinter import *

#### button Functions  : 
def next_button(event):
    exit()

def play_button(event):
    exit()

def prev_button(event):
    exit()


def bottom_window():
    # Create object
    root = Tk()
    h = root.winfo_screenheight()
    
    # getting screen's width in pixels
    w = root.winfo_screenwidth()
    H = h- 80
    W = w-570



    #######
    root.geometry(f"570x80+{W}+{H}")
    root.overrideredirect(1)

    root.bind("<Escape>", lambda e: root.destroy())

    # Add image file
    bg = PhotoImage(file = "3.png")
    play = PhotoImage(file = "play.png")
    prev = PhotoImage(file = "prev.png")
    next = PhotoImage(file = "next.png")



    #####
    label1 = Label( root, image = bg, borderwidth=0, highlightthickness=0)
    label1.place(x = 0, y = 0)






    ####### buttons

    next_label = Label( root, image = next, borderwidth=0, highlightthickness=0)
    next_label.place(x = 125, y= 27)
    next_label.bind("<Button-1>", next_button)

    play_label = Label( root, image = play, borderwidth=0, highlightthickness=0)
    play_label.place(x = 72, y= 17)
    play_label.bind("<Button-1>", play_button)

    prev_label = Label( root, image = prev, borderwidth=0, highlightthickness=0)
    prev_label.place(x = 28, y= 29)
    prev_label.bind("<Button-1>", prev_button)



    # Execute tkinter
    root.mainloop()

def top_window():
    # Create object
    root_top = Tk()
    h = root_top.winfo_screenheight()
    
    # getting screen's width in pixels
    w = root_top.winfo_screenwidth()
    H = 0
    W = w-820



    #######
    root_top.geometry(f"570x80+{W}+{H}")
    root_top.overrideredirect(1)

    root_top.bind("<Escape>", lambda e: root.destroy())

    # Add image file
    bg = PhotoImage(file = "3.png")
    play = PhotoImage(file = "play.png")
    prev = PhotoImage(file = "prev.png")
    next = PhotoImage(file = "next.png")



    #####
    label1 = Label( root_top, image = bg, borderwidth=0, highlightthickness=0)
    label1.place(x = 0, y = 0)






    ####### buttons

    next_label = Label( root_top, image = next, borderwidth=0, highlightthickness=0)
    next_label.place(x = 125, y= 27)
    next_label.bind("<Button-1>", next_button)

    play_label = Label( root_top, image = play, borderwidth=0, highlightthickness=0)
    play_label.place(x = 72, y= 17)
    play_label.bind("<Button-1>", play_button)

    prev_label = Label( root_top, image = prev, borderwidth=0, highlightthickness=0)
    prev_label.place(x = 28, y= 29)
    prev_label.bind("<Button-1>", prev_button)



    # Execute tkinter
    root_top.mainloop()

top_window()
# bottom_window()
