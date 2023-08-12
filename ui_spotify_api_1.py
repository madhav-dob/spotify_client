# Import module
from tkinter import *
import spotify_curr_track

#### button Functions  : 
def next_button(win):
    curr_song  = spotify_curr_track.next_song()
    label1 = Label( win, text = curr_song)
    label1.place(x = 0, y = 0)

def play_button(event):
    spotify_curr_track.play()

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
    bg = PhotoImage(file = "2.png")
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
    H = h-80
    W = w-570



    #######
    root_top.geometry(f"570x80+{W}+{H}")
    root_top.overrideredirect(1)

    root_top.bind("<Escape>", lambda e: root_top.destroy())

    # song_variable = StringVar()
    # song_variable.set("Initial text")
    


    # Add image file
    bg = PhotoImage(file = "2.png")
    play = PhotoImage(file = "play.png")
    prev = PhotoImage(file = "prev.png")
    next = PhotoImage(file = "next.png")

    def song_name_modifier (song):
        res = song
        if len(song) > 21:
            res = song[0:20]
            res = res + "..."

        else : 
            for i in range(23-len(song)):
                res = res + " "
        return res
    def artist_name_modifier (name):
        res = name
        if len(name) > 37:
            res = name[0:37]
            res = res + "..."
        return res


    def next_button():
        print("next button")
        curr_song  = spotify_curr_track.next_song()
        print(curr_song)
        # song_variable.set(curr_song)
        song = song_name_modifier(curr_song[0])
        name = artist_name_modifier(curr_song[1])
        canvas.itemconfig(song_label, text=song)
        canvas.itemconfig(artist_label, text=name)
    
    def play_button():
        print("play button")
        # spotify_curr_track.play()
        exit()


    def prev_button():
        print("prev button")
        curr_song  = spotify_curr_track.prev_song()
        print(curr_song)
        # song_variable.set(curr_song)
        song = song_name_modifier(curr_song[0])
        canvas.itemconfig(song_label, text=song)
        canvas.itemconfig(artist_label, text=curr_song[1])
        

    #####

    
    font_style = ("Helvetica", 20)
    font_style_artist = ("Helvetica", 12)

    canvas = Canvas(root_top, width=570, height=80, highlightthickness=0)
    canvas.pack(expand=True, fill=BOTH)
    background = canvas.create_image(285,40, image= bg)
    # label1 = canvas.create_text( 50, 50 ,text ="hello", fill = "white")

 


    song_label = canvas.create_text(370, 32, text="Standby mode", font=font_style, fill='white', anchor="center")
    artist_label = canvas.create_text(370, 59, text=" ", font=font_style_artist, fill='white', anchor="center")
    # song_label = Label(root_top, textvariable= song_variable, font=font_style, fg= "white")
    # song_label.config(bg=root_top.cget('bg'))
    # song_label.place( x = 200, y = 20)





    ####### buttons

    next_label = Label( root_top, image = next, borderwidth=0, highlightthickness=0)
    next_label.place(x = 125, y= 27)
    next_label.bind("<Button-1>", lambda event : next_button())

    play_label = Label( root_top, image = play, borderwidth=0, highlightthickness=0)
    play_label.place(x = 72, y= 17)
    play_label.bind("<Button-1>", lambda event : play_button())

    prev_label = Label( root_top, image = prev, borderwidth=0, highlightthickness=0)
    prev_label.place(x = 28, y= 29)
    prev_label.bind("<Button-1>", lambda event : prev_button())



    # Execute tkinter
    root_top.mainloop()

top_window()
