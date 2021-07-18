from tkinter import *

root = Tk()

photo = PhotoImage(file="minian.gif")

label = Label(root, image=photo)
label.pack()

root.mainloop()
