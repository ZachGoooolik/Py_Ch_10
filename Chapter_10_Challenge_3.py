# Chapter_10_Challenge_3
# By: Zachary Golik and Brianna Melius
# Date: March 5, 2015

# Create 'Order Up!' program that displays the users food choices
# and shows the user how much the bill is going to be

from tkinter import *

class Application(Frame):
    """ GUI application that acts as a restaurant. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get customers order. """
        # food values
        self.cheeseburger = 3.00
        self.fries = 1.50
        self.soda = 1.00
        self.salad = 4.00
        self.apples = 0.50
        self.water = 0.00
        self.bagel = 2.75
        self.muffin = 1.50
        self.coffee = 2.00
  
        # create instructions
        Label(self,
              text = "                                          Pick what you would like to order off of the list provided"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create solid line separating
        Label(self,
              text = "                                      -----------------------------------------------------------------------------------------------"
              ).grid(row = 1, column = 0, columnspan = 2, sticky = W)

        # create cheeseburger check button
        self.is_cheeseburger = BooleanVar()
        Checkbutton(self,
                    text = "Cheeseburger: $3.00",
                    variable = self.is_cheeseburger
                    ).grid(row = 2, column = 0, sticky = W)

        # create french fry button
        self.is_fries = BooleanVar()
        Checkbutton(self,
                    text = "French Fries: $1.50",
                    variable = self.is_fries
                    ).grid(row = 2, column = 1, sticky = W)

        # create soft drink button
        self.is_soda = BooleanVar()
        Checkbutton(self,
                    text = "Soft Drink: $1.00",
                    variable = self.is_soda
                    ).grid(row = 2, column = 2, sticky = W)

        # create salad button
        self.is_salad = BooleanVar()
        Checkbutton(self,
                    text = "Salad: $4.00",
                    variable = self.is_salad
                    ).grid(row = 3, column = 0, sticky = W)

        # create apple slices button
        self.is_apples = BooleanVar()
        Checkbutton(self,
                    text = "Apple Slices: $.50",
                    variable = self.is_apples
                    ).grid(row = 3, column = 1, sticky = W)

        # create water button
        self.is_water = BooleanVar()
        Checkbutton(self,
                    text = "Water: free",
                    variable = self.is_water
                    ).grid(row = 3, column = 2, sticky = W)

        # create bagel button
        self.is_bagel = BooleanVar()
        Checkbutton(self,
                    text = "Bagel: $2.75",
                    variable = self.is_bagel
                    ).grid(row = 4, column = 0, sticky = W)

        # create muffin button
        self.is_muffin = BooleanVar()
        Checkbutton(self,
                    text = "Muffin: $1.50",
                    variable = self.is_muffin
                    ).grid(row = 4, column = 1, sticky = W)

        # create coffee button
        self.is_coffee = BooleanVar()
        Checkbutton(self,
                    text = "Coffee: $2.00",
                    variable = self.is_coffee
                    ).grid(row = 4, column = 2, sticky = W)

        # create submit button
        Button(self,
               text = "Submit Order",
               command = self.bill
               ).grid(row = 5, column = 0, sticky = W)

        # create body
        self.order_txt = Text(self, width = 100, height = 10, wrap = WORD)
        self.order_txt.grid(row = 6, column = 0, columnspan = 3)

    def bill(self):
        self.total = 0
        total = self.total
        if self.is_cheeseburger.get():
            total += self.cheeseburger
        if self.is_fries.get():
            total += self.fries
        if self.is_soda.get():
            total += self.soda
        if self.is_salad.get():
            total += self.salad
        if self.is_apples.get():
            total += self.apples
        if self.is_water.get():
            total += self.water
        if self.is_bagel.get():
            total += self.bagel
        if self.is_muffin.get():
            total += self.muffin
        if self.is_coffee.get():
            total += self.coffee

        bills = "Your total is going to be: $" + str(total) + "."
        self.order_txt.delete(0.0, END)
        self.order_txt.insert(0.0, bills)
        

root = Tk()
root.title("Order Up!")
app = Application(root)
root.mainloop()
