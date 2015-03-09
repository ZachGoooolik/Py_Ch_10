# Chapter_10_Challenge_2
# By: Zach Golik and Brianna Melius
# Date: March 4, 2015

# Convert the Guess My Number program using a GUI.

from tkinter import *
import random

class Application(Frame):
    """ GUI application that guesses a number between 1 and 100. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        """ Create widgets to guess the number the computer has guessed. """
        # create instruction label
        self.tries = 0
        Label(self,
              text = """         Welcome to 'Guess My Number'!
          I'm thinking of a number between 1 and 100.
         Try to guess it in as few attempts as possible.
                        """
              ).grid(row = 0, column = 0, columnspan = 2, sticky = N)
        # create a label and text entry for a number guess
        Label(self,
              text = "Guess: "
              ).grid(row = 1, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 1, column = 1, sticky = W)

        # create a random number
        Button(self,
               text = "Random Number",
               command = self.random_num
               ).grid(row = 2, column = 1, sticky = W)

        # create a submit button
        Button(self,
               text = "Guess",
               command = self.guess_loop
               ).grid(row = 1, column = 2, sticky = W)

        # shows amount of tries
        Label(self,
              text = "Tries: " + str(self.tries)
              ).grid(row = 2, column = 0, sticky = W)

        # create body
        self.guess_txt = Text(self, width = 50, height = 5, wrap = WORD)
        self.guess_txt.grid(row = 7, column = 0, columnspan = 4)

    def random_num(self):
        self.the_number = random.randint(1, 100)
        status = "Number has been changed"
        self.guess_txt.delete(0.0, END)
        self.guess_txt.insert(0.0, status)

    def guess_loop(self):
        tries = self.tries
        guess = int(self.guess_ent.get())
        the_number = self.the_number
        
        if guess == the_number:
            answer = "You guessed it! The number was " + str(the_number)
            tries = 0
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, answer)
        elif guess < the_number:
            tries += 1
            answer = "Higher..."
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, answer)
        elif guess > the_number:
            tries += 1
            answer = "Lower..."
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, answer)


root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()
