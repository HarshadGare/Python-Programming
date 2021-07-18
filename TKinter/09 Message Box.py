from tkinter import *
import tkinter.messagebox

main = Tk()

tkinter.messagebox.showinfo("Window Title", "This is Message Box")

ans = tkinter.messagebox.askquestion("Window Title", "Do you want to Continue....")

if ans == "yes":
    print("Yes")
else:
    exit()

main.mainloop()
