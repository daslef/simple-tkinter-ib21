import tkinter as tk
import tkinter.messagebox as messagebox # to tell why

def open_results():
    result = state_of_radio.get()
    messagebox.showinfo("Results", f"{result} was choosen")

root = tk.Tk()
root.geometry("400x400")

state_of_radio = tk.IntVar()

rb_1 = tk.Radiobutton(root, text="Orange", value=1, variable=state_of_radio)
rb_2 = tk.Radiobutton(root, text="Mango", value=2, variable=state_of_radio)
rb_3 = tk.Radiobutton(root, text="Avocado", value=3, variable=state_of_radio)

tk.Button(root, text='I have choosen', command=open_results).pack()

rb_1.pack()
rb_2.pack()
rb_3.pack()


root.mainloop()