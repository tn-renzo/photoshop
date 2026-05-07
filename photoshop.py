from curses import A_HORIZONTAL
import tkinter as tk


def setup_gui(root):

    root.title("Photoshop")
    root.geometry("1000x600")

    # configure wheigts of rows and collumns
    """
    i = 0
    for i in range(8):
        root.rowconfigure(i, weight=1)
    h = 0
    for h in range(4):
        root.columnconfigure(h, weight=1)
    """

    """
    # creating frames
    conf_frame = tk.LabelFrame(master=root, text="configurations", bg="lightgrey")
    conf_frame.grid(column=0, row=0)
    """

    # creating buttons
    back = tk.Button(text="<--", width=4)
    back.grid(column=0, columnspan=1, row=0)

    forward = tk.Button(text="-->", width=4)
    forward.grid(column=3, columnspan=1, row=0)

    reset = tk.Button(text="reset", width=16)
    reset.grid(column=1, columnspan=2, row=0)

    bl_wh = tk.Button(text="black/white", width=12)
    bl_wh.grid(column=0, columnspan=2, row=1)

    invert = tk.Button(text="invert", width=12)
    invert.grid(column=2, columnspan=2, row=1)

    save = tk.Button(text="save", width=24)
    save.grid(column=0, columnspan=4, row=7)

    save = tk.Button(text="load", width=24)
    save.grid(column=0, columnspan=4, row=8)

    # creating sliders
    Blur = tk.Scale(from_=0, to=100, orient=tk.HORIZONTAL, length=180)
    Blur.grid(column=1, columnspan=3, row=2)

    red = tk.Scale(from_=0, to=255, orient=tk.HORIZONTAL, length=180)
    red.grid(column=1, columnspan=3, row=3)

    green = tk.Scale(from_=0, to=255, orient=tk.HORIZONTAL, length=180)
    green.grid(column=1, columnspan=3, row=4)

    blue = tk.Scale(from_=0, to=255, orient=tk.HORIZONTAL, length=180)
    blue.grid(column=1, columnspan=3, row=5)

    # creating text
    blur_label = tk.Label(text="Blur")
    blur_label.grid(column=0, row=2)

    red_label = tk.Label(text="R")
    red_label.grid(column=0, row=3)

    green_label = tk.Label(text="G")
    green_label.grid(column=0, row=4)

    blue_label = tk.Label(text="B")
    blue_label.grid(column=0, row=5)

    """


def main():

    # tkinter setup
    root = tk.Tk()
    setup_gui(root)

    # run mainloop
    root.mainloop()


main()
