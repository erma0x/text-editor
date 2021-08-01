from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import os
import sys


root = Tk()
root.title("Norman Text Editor")
root.geometry("450x600")
root.configure(background="white")
root.config(cursor="hand2")

# canvas for background        
C = Canvas(root, bg="blue", height=250, width=300)

# background image
image = ImageTk.PhotoImage(file = sys.path[0]+"/bg.gif")
background = Label(image=image)
background.bind('<Configure>')
background.place(x=-400,y=-100)

# adding path showing box
pathh = Entry(root, width=40)
pathh.place(x=55,y=500)
    
# adding writing space
txtarea = Text(root,width=40, height=20)
txtarea.place(x=60,y=40)

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),))

    pathh.insert(END, tf)
    tf = open(tf)
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()


def saveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(txtarea.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()


# buttons
Button(
    root,
    text="Open File",
    command=openFile,
    height = 1, width = 6 ).place(x=100,y=450)

Button(
        root,
        text="Save File",
        command=saveFile,
        height = 1, width = 6 ).place(x=200,y=450)


Button(
    root,
    text="Exit",
    command=lambda: root.destroy(),
    height = 1, width = 6 ).place(x=300,y=450)


        # # adding vertical scrollbars in TextEditor
        # ver_sb = Scrollbar(root, orient=VERTICAL)
        # ver_sb.pack(side=RIGHT)

        # # adding horizontal scrollbars in TextEditor
        # hor_sb = Scrollbar(root, orient=HORIZONTAL)
        # hor_sb.pack(side=BOTTOM, fill=BOTH)



        # # binding scrollbar with text area vertical axis
        # txtarea.config(root,yscrollcommand=ver_sb.set)
        # ver_sb.config(command=txtarea.yview)

        # # binding scrollbar with text area horizontal axis
        # txtarea.config(xscrollcommand=hor_sb.set)
        # hor_sb.config(command=txtarea.xview)


    



#e = TextEditor(root)
#root.place(x=0,y=0)#(fill=BOTH, expand=YES)

root.mainloop()
