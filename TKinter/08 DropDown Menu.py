from tkinter import *


def done():
    print("Ok....")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=done)
subMenu.add_command(label="New", command=done)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=done)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=done)

# *****STATUS BAR*********

status = Label(root, text="Processing....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
