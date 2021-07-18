from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()

Dline = canvas.create_line(0, 0, 300, 200)
Cline = canvas.create_line(0, 400, 300, 200, fill="blue")

rect = canvas.create_rectangle(200, 0, 100, 200, fill="green")

text = canvas.create_text(100, 100, text="This Is Text", fill="Red")

#canvas.delete(Dline)
# canvas.delete(ALL)

root.mainloop()
