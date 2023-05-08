from tkinter import *

root = Tk()
root.title("Billing system")
root.geometry('850x720')
bg_color = 'Black'
title = Label(root, text='Concession Stand ', bg=bg_color, fg='white', font=('times new roman', 25, 'bold'))
title.pack(fill=X)

F1 = LabelFrame(root, text='Food & Drinks', font=('times new roman', 20, 'bold'), fg='Black', )
F1.place(x=5, y=90, width=800, height=550)

items = Label(F1, text='Items', font=('Helvetica', 20, 'bold'), fg='black')
items.grid(row=0, column=0, padx=20, pady=15)

n = Label(F1, text='Quantity', font=('Helvetica', 20, 'bold'), fg='black')
n.grid(row=0, column=1, padx=20, pady=15)

cost = Label(F1, text='Cost', font=('Helvetica', 20, 'bold'), fg='black')
cost.grid(row=0, column=2, padx=20, pady=15)

Popcorn = Label(F1, text='Popcorn', font=('times new roman', 15, 'bold'), fg='Black')
Popcorn.grid(row=1, column=0, padx=20, pady=15)

Popcorn_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Popcorn_txt.grid(row=1, column=1, padx=5, pady=5)

Popcorn_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Popcorn_txt.grid(row=1, column=2, padx=20, pady=15)

Hotdog = Label(F1, text='Hotdog', font=('times new roman', 15, 'bold'), fg='Black')
Hotdog.grid(row=2, column=0, padx=20, pady=15)

Hotdog_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Hotdog_txt.grid(row=2, column=1, padx=20, pady=15)

Hotdog_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Hotdog_txt.grid(row=2, column=2, padx=20, pady=15)

Pizza = Label(F1, text='Pizza', font=('times new roman', 15, 'bold'), fg='Black')
Pizza.grid(row=3, column=0, padx=20, pady=15)

Pizza_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Pizza_txt.grid(row=3, column=1, padx=20, pady=15)

Pizza_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Pizza_txt.grid(row=3, column=2, padx=20, pady=15)

Water = Label(F1, text='Water', font=('times new roman', 15, 'bold'), fg='Black')
Water.grid(row=4, column=0, padx=20, pady=15)

Water_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Water_txt.grid(row=4, column=1, padx=20, pady=15)

Water_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Water_txt.grid(row=4, column=2, padx=20, pady=15)

Drink = Label(F1, text='Soda', font=('times new roman', 15, 'bold'), fg='Black')
Drink.grid(row=5, column=0, padx=20, pady=15)

Drink_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Drink_txt.grid(row=5, column=1, padx=20, pady=15)

Drink_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Drink_txt.grid(row=5, column=2, padx=20, pady=15)

total = Label(F1, text='Total', font=('times new roman', 20, 'bold'), fg='Black')
total.grid(row=6, column=0, padx=20, pady=15)

total_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
total_txt.grid(row=6, column=1, padx=20, pady=15)

total_txt = Entry(F1, font='aerial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
total_txt.grid(row=6, column=2, padx=20, pady=15)


def open_win():
    new = Toplevel(root)
    new.geometry("650x720")
    new.title("Receipt")

    frame = Frame(new, relief=GROOVE, bd=10)
    frame.place(x=5, y=10, width=635, height=700)
    Label(frame, text='Receipt', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
    # add a scrollbar.
    textarea = Text(frame, font='arial 15 bold')

    textarea.pack(fill=BOTH)


receipt_button = Button(root, text="Final Receipt", bg=bg_color, fg='white', font=('Arial', 12, 'bold'), relief=RAISED,
                        bd=15, command=open_win)
receipt_button.pack(side=BOTTOM, padx=220, pady=50, )

root.mainloop()
