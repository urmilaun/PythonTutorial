from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry("900x800")
#for png images
photo=PhotoImage(file="logo.png")

#for jpg file
image=Image.open("logo.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()

root.mainloop()