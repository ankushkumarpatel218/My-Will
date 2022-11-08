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

frame = Frame(root, bg='red', borderwidth=3, relief=RIDGE)
frame.pack(side=LEFT)
lab = Label(frame, text='Shanks is badass!')
lab.pack()

frm = Frame(root,text="Emperor")

root.mainloop()
