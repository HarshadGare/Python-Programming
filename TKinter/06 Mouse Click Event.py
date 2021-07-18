from tkinter import *
root = Tk()


def leftclick(event):
    print("Left Click")


def rightclick(event):
        print("Right Click")


def middleclick(event):
    print("Middle Click")


f = Frame(root, width=500, height=500)
f.bind("<Button-1>", leftclick)
f.bind("<Button-2>", rightclick)
f.bind("<Button-3>", middleclick)
f.pack()

root.mainloop()
