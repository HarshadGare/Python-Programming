from tkinter import *

root = Tk()

def printfun():
    print("My Name is Harshad")


b = Button(root, text="Print Name", command=printfun)
b.pack()

# ************ Second Way **************
def printfun1(event):
    print("My Name is Harshad Gare")


b1 = Button(root, text="Print Name")
b1.bind("<Button-1>", printfun1)
b1.pack()

root.mainloop()
