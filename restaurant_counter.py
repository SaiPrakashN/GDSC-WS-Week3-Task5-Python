from tkinter import *
from tkinter.ttk import *


def main():
    root = Tk()
    root.title("Login Window")
    root.geometry("600x450")

    courier_new_greek_font = "Courier New Greek"
    courier_new_font = "Courier New"
    dubai_medium_font = "Dubai Medium"
    georgia_font = "Georgia"
    lucida_font = "Lucida Calligraphy"
    verdana_font = "Verdana"
    active_blue_colour = "#03045E"

    # items_frame = Frame(root)
    buttons_frame = Frame(root)

    style = Style()
    style.configure('TButton', font=(lucida_font, 10, 'bold', 'underline'),
                    borderwidth='6', activebackground=active_blue_colour,
                    background='cyan')
    style.configure('TLabel', font=(verdana_font, 10))
    style.configure('TEntry', font=courier_new_font)

    items = ["Pizza", "Burger", "Donut", "Ice Cream", "Chicken", "Mutton"]
    costs = [220, 180, 150, 120, 140, 190]
    values = [IntVar() for _ in range(len(items))]
    counts = [StringVar() for _ in range(len(items))]

    gap = Label(root, text="\n")
    gap2 = Label(root, text="\n")
    display = Label(root)

    def take_inputs():
        total = 0
        for j in range(len(items)):
            item_value = [0 if counts[j].get() == "" else int(counts[j].get())]
            total += item_value[0] * costs[j]
        display.configure(text="Total Cost: " + str(total),
                          font=(dubai_medium_font, 18))
        display.pack()
        print(total)

    Label(root, text="Welcome", font=(georgia_font, 30)).pack()
    Label(root, text="\n").pack()

    instruction_frame = Frame(root)
    Label(instruction_frame, text="Items\t",
          font=(courier_new_greek_font, 13)).pack(side=LEFT)
    Label(instruction_frame, text="Num of Items",
          font=(courier_new_greek_font, 13)).pack(side=RIGHT)
    instruction_frame.pack()
    # Label(root, text="\n").pack()

    pizza_frame = Frame(root)
    Label(pizza_frame, text=items[0], width=12).pack(side=LEFT)
    Entry(pizza_frame, textvariable=counts[0]).pack(side=RIGHT)

    burger_frame = Frame(root)
    Label(burger_frame, text=items[1], width=12).pack(side=LEFT)
    Entry(burger_frame, textvariable=counts[1]).pack(side=RIGHT)

    donut_frame = Frame(root)
    Label(donut_frame, text=items[2], width=12).pack(side=LEFT)
    Entry(donut_frame, textvariable=counts[2]).pack(side=RIGHT)

    ice_cream_frame = Frame(root)
    Label(ice_cream_frame, text=items[3], width=12).pack(side=LEFT)
    Entry(ice_cream_frame, textvariable=counts[3]).pack(side=RIGHT)

    chicken_frame = Frame(root)
    Label(chicken_frame, text=items[4], width=12).pack(side=LEFT)
    Entry(chicken_frame, textvariable=counts[4]).pack(side=RIGHT)

    mutton_frame = Frame(root)
    Label(mutton_frame, text=items[5], width=12).pack(side=LEFT)
    Entry(mutton_frame, textvariable=counts[5]).pack(side=RIGHT)

    Button(buttons_frame, text='Order',
           command=take_inputs).pack(side=RIGHT, padx=10)

    Button(buttons_frame, text='Cancel',
           command=root.destroy).pack(side=LEFT, padx=10)

    # heading_label.pack()
    pizza_frame.pack()
    burger_frame.pack()
    donut_frame.pack()
    ice_cream_frame.pack()
    chicken_frame.pack()
    mutton_frame.pack()
    gap.pack()
    buttons_frame.pack()
    gap2.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
