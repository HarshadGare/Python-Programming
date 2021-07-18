from tkinter import *

root = Tk()

l1 = Label(root, text="User Name: ")
l1.grid(row=0)
l2 = Label(root, text="Password: ")
l2.grid(row=1)

e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=1, column=1)

c1 = Checkbutton(root, text="Accept T&C")
c1.grid(columnspan=2)

root.mainloop()
