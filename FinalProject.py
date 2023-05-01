from tkinter import *

root = Tk()
root.title('Receipt Maker')
root.geometry('1280x720')
bg_color = 'black'

title = Label(root, text='Billing  system ', bg=bg_color, fg='white', font=('times new roman', 25, 'bold'))
title.pack(fill=X)
F1 = LabelFrame(root, text='product details', font=('times new roman', 15, 'bold'), fg='black')
F1.place(x=5, y=90, width=800, height=500)
root.mainloop()
