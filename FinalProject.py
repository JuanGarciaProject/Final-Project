from tkinter import *

root = Tk()
root.title("Billing system")
root.geometry('850x720')
bg_color = 'Black'
title = Label(root, text='Concession Stand ', bg=bg_color, fg='white', font=('times new roman', 25, 'bold'),
              relief=GROOVE)
title.pack(fill=X)
# This displays the Items that are served in the concession stand and gives you an entry box where you can enter the
# quantity and prices of each Item
products = LabelFrame(root, text='Food & Drinks', font=('Arial', 15, 'bold'), fg='Black', )
products.place(x=5, y=90, width=800, height=550)

items = Label(products, text='Items', font=('Arial', 20, 'bold'), fg='black')
items.grid(row=0, column=0, padx=20, pady=15)

n = Label(products, text='Quantity', font=('Arial', 20, 'bold'), fg='black')
n.grid(row=0, column=1, padx=20, pady=15)

cost = Label(products, text='Cost', font=('Arial', 20, 'bold'), fg='black')
cost.grid(row=0, column=2, padx=20, pady=15)

Popcorn = Label(products, text='Popcorn', font=('Arial', 15, 'bold'), fg='Black')
Popcorn.grid(row=1, column=0, padx=20, pady=15)

Popcorn_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Popcorn_txt.grid(row=1, column=1, padx=5, pady=5)

Popcorn_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Popcorn_txt.grid(row=1, column=2, padx=20, pady=15)

Hotdog = Label(products, text='Hotdog', font=('Arial', 15, 'bold'), fg='Black')
Hotdog.grid(row=2, column=0, padx=20, pady=15)

Hotdog_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Hotdog_txt.grid(row=2, column=1, padx=20, pady=15)

Hotdog_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Hotdog_txt.grid(row=2, column=2, padx=20, pady=15)

Pizza = Label(products, text='Pizza', font=('Arial', 15, 'bold'), fg='Black')
Pizza.grid(row=3, column=0, padx=20, pady=15)

Pizza_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Pizza_txt.grid(row=3, column=1, padx=20, pady=15)

Pizza_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Pizza_txt.grid(row=3, column=2, padx=20, pady=15)

Water = Label(products, text='Water', font=('Arial', 15, 'bold'), fg='Black')
Water.grid(row=4, column=0, padx=20, pady=15)

Water_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Water_txt.grid(row=4, column=1, padx=20, pady=15)

Water_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Water_txt.grid(row=4, column=2, padx=20, pady=15)

Drinks = Label(products, text='Total', font=('Arial', 20, 'bold'), fg='Black')
Drinks.grid(row=5, column=0, padx=20, pady=15)

Drinks_text = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Drinks_text.grid(row=5, column=1, padx=20, pady=15)

Drinks_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
Drinks_txt.grid(row=5, column=2, padx=20, pady=15)

total = Label(products, text='Total', font=('Arial', 20, 'bold'), fg='Black')
total.grid(row=6, column=0, padx=20, pady=15)

total_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
total_txt.grid(row=6, column=1, padx=20, pady=15)

total_txt = Entry(products, font='Arial 15 bold', relief=SUNKEN, bd=3, justify=CENTER)
total_txt.grid(row=6, column=2, padx=20, pady=15)


# this will open a new window to where the receipt will be created.
def open_win():
    new = Toplevel(root)
    new.geometry("650x720")
    new.title("Receipt")

    receipt = Frame(new, relief=GROOVE, bd=10)
    receipt.place(x=5, y=10, width=635, height=700)
    Label(receipt, text='Receipt', font='Arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
    textarea = Text(receipt, font='arial 15 bold')
    textarea.pack(fill=BOTH)




# The purpose of this button is to send the Price of each item to the Receipt Window
receipt_button = Button(root, text="Final Receipt", bg=bg_color, fg='white', font=('Arial', 12, 'bold'), relief=RAISED,
                        bd=15, command=open_win)
receipt_button.pack(side=BOTTOM, padx=220, pady=50)

root.mainloop()
