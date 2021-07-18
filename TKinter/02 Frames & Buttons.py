from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()              # side By Default value is TOP
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

b1 = Button(topFrame, text="Button 1")  # fg By Default value is black
b1.pack(padx=2, pady=2)
b2 = Button(topFrame, text="Button 2", fg="red")
b2.pack()
b3 = Button(bottomFrame, text="Button 3", fg="blue")
b3.pack(side=RIGHT, padx=10)
b4 = Button(bottomFrame, text="Button 4", fg="green")
b4.pack()

root.mainloop()
