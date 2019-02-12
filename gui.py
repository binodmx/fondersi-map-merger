import tkinter as tk
from tkinter import filedialog
import fondersi

filelist = []
def add_files():
    global filelist
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("JPEG files","*.jpg"),("All files","*.*")))
    filelist.append(filename)

window = tk.Tk()
window.title("Fondersi")
window.geometry("400x400")

text1 = tk.Text(master=window, height=10, width=30)
text1.grid()

button1 = tk.Button(text="Upload", command=add_files)
button1.grid(column=1, row=1)

button2 = tk.Button(text="Remove")
button2.grid(column=1, row=2)

button3 = tk.Button(text="Merge")
button3.grid(column=1, row=3)

fondersi.function1("calling function1...")
window.mainloop()
