from tkinter import *

root = Tk()

label1 = Label(root, text="This Is The Label1", fg="Blue", bg="Yellow")
label1.pack()

label2 = Label(root, text="This Is The Label2", fg="Black", bg="Yellow")
label2.pack(fill=X)

label3 = Label(root, text="This Is The Label3", bg="red")
label3.pack(fill=Y, side=LEFT)

root.mainloop()