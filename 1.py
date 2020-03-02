from tkinter import *


def add_label():
    Label(root, text="New Label", padx="30", pady="20", fg="#eeeeee", bg="#333333").pack(side=BOTTOM, fill=X)


root = Tk()
root.geometry("300x500")

Label(root, text="Just a test", padx="30", pady="20").pack(side=BOTTOM)
Button(root, text="Click me!", command=add_label).pack()

root.mainloop()