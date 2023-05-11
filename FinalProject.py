from tkinter import *

root = Tk()
root.title("Billing system")
root.geometry('850x720')
bg_color = 'Black'

# Title of the application
title = Label(root, text='Concession Stand ', bg=bg_color, fg='white', font=('times new roman', 25, 'bold'))
title.pack(fill=X)

# Frame for food and drinks
products = LabelFrame(root, text='Food & Drinks', font=('Arial', 15, 'bold'), fg='Black')
products.place(x=5, y=90, width=800, height=550)

# Labels and Entry widgets for each item
items = Label(products, text='Items', font=('Arial', 20, 'bold'), fg='black')
items.grid(row=0, column=0, padx=20, pady=15)

n = Label(products, text='Quantity', font=('Arial', 20, 'bold'), fg='black')
n.grid(row=0, column=1, padx=20, pady=15)

cost = Label(products, text='Cost', font=('Arial', 20, 'bold'), fg='black')
cost.grid(row=0, column=2, padx=20, pady=15)

# labels the for the type of product offered at the concession stand
Popcorn = Label(products, text='Popcorn', font=('Arial', 15, 'bold'), fg='Black')
Popcorn.grid(row=1, column=0, padx=20, pady=15)

Popcorn_qty_txt = Entry(products, font='Arial 15 bold', )
Popcorn_qty_txt.grid(row=1, column=1, padx=5, pady=5)

Popcorn_cost_txt = Entry(products, font='Arial 15 bold', )
Popcorn_cost_txt.grid(row=1, column=2, padx=20, pady=15)

Hotdog = Label(products, text='Hotdog', font=('Arial', 15, 'bold'), fg='Black')
Hotdog.grid(row=2, column=0, padx=20, pady=15)

Hotdog_qty_txt = Entry(products, font='Arial 15 bold', )
Hotdog_qty_txt.grid(row=2, column=1, padx=20, pady=15)

Hotdog_cost_txt = Entry(products, font='Arial 15 bold', )
Hotdog_cost_txt.grid(row=2, column=2, padx=20, pady=15)

Pizza = Label(products, text='Pizza', font=('Arial', 15, 'bold'), fg='Black')
Pizza.grid(row=3, column=0, padx=20, pady=15)

Pizza_qty_txt = Entry(products, font='Arial 15 bold', )
Pizza_qty_txt.grid(row=3, column=1, padx=20, pady=15)

Pizza_cost_txt = Entry(products, font='Arial 15 bold', )
Pizza_cost_txt.grid(row=3, column=2, padx=20, pady=15)

Water = Label(products, text='Water', font=('Arial', 15, 'bold'), fg='Black')
Water.grid(row=4, column=0, padx=20, pady=15)

Water_qty_txt = Entry(products, font='Arial 15 bold', )
Water_qty_txt.grid(row=4, column=1, padx=20, pady=15)

Water_cost_txt = Entry(products, font='Arial 15 bold', )
Water_cost_txt.grid(row=4, column=2, padx=20, pady=15)

Drink = Label(products, text='Soda', font=('Arial', 15, 'bold'), fg='Black')
Drink.grid(row=5, column=0, padx=20, pady=15)

Drink_qty_txt = Entry(products, font='Arial 15 bold', )
Drink_qty_txt.grid(row=5, column=1, padx=20, pady=15)

Drink_cost_txt = Entry(products, font='Arial 15 bold', )
Drink_cost_txt.grid(row=5, column=2, padx=20, pady=15)

# this button is used to exit the program
exit_b = Button(products, text='Exit', bg=bg_color, fg='white', font=('Arial', 12, 'bold'), command=exit)
exit_b.grid(row=7, column=0, padx=20, pady=15)


def open_win():
    new = Toplevel(root)
    new.geometry("650x720")
    new.title("Receipt")

    frame = Frame(new)
    frame.place(x=5, y=10, width=635, height=700)
    Label(frame, text='Receipt', font='Arial 15 bold', ).pack(fill=X)

    textarea = Text(frame, font='arial 15 bold')
    textarea.pack(fill=BOTH)

    # Get the values from the Entry fields
    popcorn_qty = Popcorn_qty_txt.get()
    popcorn_cost = Popcorn_cost_txt.get()
    hotdog_qty = Hotdog_qty_txt.get()
    hotdog_cost = Hotdog_cost_txt.get()
    pizza_qty = Pizza_qty_txt.get()
    pizza_cost = Pizza_cost_txt.get()
    water_qty = Water_qty_txt.get()
    water_cost = Water_cost_txt.get()
    soda_qty = Drink_qty_txt.get()
    soda_cost = Drink_cost_txt.get()

    # Calculate the total cost of each item
    popcorn_total = float(popcorn_qty) * float(popcorn_cost)
    hotdog_total = float(hotdog_qty) * float(hotdog_cost)
    pizza_total = float(pizza_qty) * float(pizza_cost)
    water_total = float(water_qty) * float(water_cost)
    soda_total = float(soda_qty) * float(soda_cost)

    Total = (popcorn_total + hotdog_total + pizza_total + water_total + soda_total)

    # Formats the receipt in order to get the layout of each data type under its own label
    receipt_text = f"""\
    Item          Quantity       Cost       Total
    ------------------------------------------------------------------------
    Popcorn    {popcorn_qty}      {popcorn_cost}             {popcorn_total}
    Hotdog      {hotdog_qty}       {hotdog_cost}              {hotdog_total}
    Pizza        {pizza_qty}        {pizza_cost}               {pizza_total}
    Water        {water_qty}        {water_cost}               {water_total}
    Soda          {soda_qty}         {soda_cost}                {soda_total}
    Total                                                   {Total}
    ----------------------------------------"""

    # Insert the formatted receipt into the Text widget
    textarea.insert(INSERT, receipt_text)


# Button to open the receipt window
receipt_button = Button(root, text="Final Receipt", bg=bg_color, fg='white', font=('Arial', 12, 'bold'),
                        command=open_win)
receipt_button.pack(side=BOTTOM, padx=220, pady=50)

root.mainloop()

