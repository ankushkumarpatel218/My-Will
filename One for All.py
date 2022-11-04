from tkinter import *
from PIL import ImageTk, Image
root = Tk()

# Width x Height
root.geometry('700x500')

# width , height
root.minsize(600, 500)
root.maxsize(1400, 830)

# for jpg
# photo = Image.open("pht1.jpg")
# img = ImageTk.PhotoImage(photo)
# lab = Label(image=img)
# lab.pack()

# for png
# photo = PhotoImage(file='pht1.png')
# lab = Label(image=photo)
# lab.pack()

root.title('My GUI!')

# text - add the text
# bg - background
# fg - foreground
# font - set the font
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# lab = Label(text="ONE PIECE does exist!", bg='black', fg='white', pady=20, padx=40, font='comicsansms 30 bold', borderwidth=3, relief=RIDGE)
# lab.pack(anchor='n', side=TOP, fill='x')

# ANCHOR - nw , sw , ne , se , sn
# SIDE - TOP , BOTTOM , LEFT , RIGHT





root.mainloop()
