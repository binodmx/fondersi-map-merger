#=================importing modules=================

import os, PIL
from PIL import ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from TkinterDnD2 import *
import fondersi

#=================custom functions==================

def upload_files():    
    file_names = filedialog.askopenfilenames(filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")))
    for file_name in file_names:
        add_file(file_name)

def remove_files():
    for file_id in selected_file_ids.keys():
        del canvas.filenames[file_id]
        canvas.delete(file_id)
        canvas.delete(selected_file_ids[file_id])
    selected_file_ids.clear()
    
def merge():
    if len(canvas.filenames.values()) < 2:
        messagebox.showinfo("Warning", "Select at least 2 items to merge.")
    else:
        merged_map = fondersi.merge(canvas.filenames.values())
        
        res1 = messagebox.askyesno("Fondersi","Merging successful! \nWould you like to display the merged map?")
        if res1:
            fondersi.display()
            
        res2 = messagebox.askyesno("Fondersi","Would you like to save the merged map?")
        if res2:
            res3 = filedialog.asksaveasfilename(title = "Save")
            fondersi.save(res3)
            messagebox.showinfo("Fondersi", "Merged map is saved successfully!")


#=================main GUI=========================

window = TkinterDnD.Tk()
window.withdraw()
window.title('Fondersi')
window.resizable(False, False)
window_width = 350
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

lbl1 = ttk.Label(window, text='Drag and drop map segments here: (maximum 9)')
lbl1.pack(side='top')

button3 = ttk.Button(text="Merge", command=merge)
button3.pack(side='bottom', fill='x', padx='10', pady='10')

button2 = ttk.Button(text="Remove", command=remove_files)
button2.pack(side='bottom', fill='x', padx='10')

button1 = ttk.Button(text="Upload", command=upload_files)
button1.pack(side='bottom', fill='x', padx='10', pady='10')

canvas = Canvas(window, name='dnd_demo_canvas', bg='white', relief='sunken', bd=1, highlightthickness=1, takefocus=True, width=300)
canvas.pack(side='top')

#=================drag and drop functionality======

icons = {}
selected_file_ids = {}
canvas.filenames = {}
canvas.nextcoords = [50, 20]
canvas.dragging = False

def add_file(filename):
    if len(canvas.filenames) < 9:
        if filename[-3:] == "jpg" or filename[-3:] == "png":
            if filename not in canvas.filenames.values():
                icon = PIL.Image.open(filename)
                icon.thumbnail((30, 30), PIL.Image.ANTIALIAS)
                icons[filename] = ImageTk.PhotoImage(icon)
                id1 = canvas.create_image(canvas.nextcoords[0], canvas.nextcoords[1], image=icons[filename], anchor='n', tags=('file',))
                id2 = canvas.create_text(canvas.nextcoords[0], canvas.nextcoords[1] + 30, text=os.path.basename(filename), anchor='n', justify='center', width=90)
                def select_item(event):
                    selected_file_ids.clear()
                    canvas.select_from(id2, 0)
                    canvas.select_to(id2, 'end')
                    selected_file_ids[id1] = id2
                canvas.tag_bind(id1, '<ButtonPress-1>', select_item)
                canvas.tag_bind(id2, '<ButtonPress-1>', select_item)
                canvas.filenames[id1] = filename
                if canvas.nextcoords[0] > 150:
                    canvas.nextcoords = [50, canvas.nextcoords[1] + 80]
                else:
                    canvas.nextcoords = [canvas.nextcoords[0] + 100, canvas.nextcoords[1]]
            else:
                messagebox.showinfo("Warning", "File is already uploaded." )
        else:
            messagebox.showinfo("Warning", "Wrong file format." )
    else:
        messagebox.showinfo("Warning", "Maximum attachment size reached." )
        
#================mouse click methods============

def deselect_item(event):
    canvas.selection_clear()
    selected_file_ids.clear()

canvas.bind("<ButtonPress-3>", deselect_item)

#=================drop methods====================

def drop_enter(event):
    event.widget.focus_force()
    return event.action

def drop_position(event):
    return event.action

def drop_leave(event):
    return event.action

def drop(event):
    if canvas.dragging:
        return REFUSE_DROP
    if event.data:
        files = canvas.tk.splitlist(event.data)
        for f in files:
            add_file(f)
    return event.action

canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<DropEnter>>', drop_enter)
canvas.dnd_bind('<<DropPosition>>', drop_position)
canvas.dnd_bind('<<DropLeave>>', drop_leave)
canvas.dnd_bind('<<Drop>>', drop)

#=================drag methods====================

def drag_init(event):
    data = ()
    sel = canvas.select_item()
    if sel:
        # in a decent application we should check here if the mouse
        # actually hit an item, but for now we will stick with this
        data = (canvas.filenames[sel],)
        canvas.dragging = True
        return ((ASK, COPY), (DND_FILES, DND_TEXT), data)
    else:
        # don't start a dnd-operation when nothing is selected; the
        # return "break" here is only cosmetical, return "foobar" would
        # probably do the same
        return 'break'

def drag_end(event):
    canvas.dragging = False

canvas.drag_source_register(1, DND_FILES)
canvas.dnd_bind('<<DragInitCmd>>', drag_init)
canvas.dnd_bind('<<DragEndCmd>>', drag_end)

window.update_idletasks()
window.deiconify()
window.mainloop()

#=================end of code===================
