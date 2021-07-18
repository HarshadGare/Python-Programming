from tkinter import *


class Custom:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()
            self.b1 = Button(frame, text="Print Name", command=self.printname)
            self.b1.pack(side=LEFT)
            self.b2 = Button(frame, text="Quit", command=frame.quit)
            self.b2.pack(side=LEFT)

        def printname(self):
                print("Python")


root = Tk()
a = Custom(root)
root.mainloop()
