# Chapter_10_Challenge_1
# By: Brianna Melius and Zach G
# Date: March 3, 2015

# Edit the Mad Lib Program

from tkinter import *

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for the name of a person
        Label(self,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        # create a label and text entry for a plural noun
        Label(self,
              text = "Plural Noun:"
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)


        # create a label and text entry for a verb
        Label(self,
              text = "Verb:"
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
     
        # create a label for adjectives check buttons
        Label(self,
              text = "Adjective(s):"
              ).grid(row = 4, column = 0, sticky = W)

        # create itchy check button
        self.is_loud = BooleanVar()
        Checkbutton(self,
                    text = "loud",
                    variable = self.is_loud
                    ).grid(row = 5, column = 0, sticky = W)

        # create joyous check button
        self.is_quiet = BooleanVar()
        Checkbutton(self,
                    text = "quiet",
                    variable = self.is_quiet
                    ).grid(row = 6, column = 0, sticky = W)

        # create electric check button
        self.is_beautiful = BooleanVar()
        Checkbutton(self,
                    text = "beautiful",
                    variable = self.is_beautiful
                    ).grid(row = 7, column = 0, sticky = W)

        # create a label for body parts radio buttons
        Label(self,
              text = "Body Part:"
              ).grid(row = 4, column = 1, sticky = W)

        # create variable for single, body part
        self.body_part = StringVar()
        self.body_part.set(None)
  
        # create body part radio buttons
        body_parts = ["butt", "arm", "eyeball"]
        row = 5
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = row, column = 1, sticky = W)
            row += 1

        # create a submit button
        Button(self,
               text = "Click for story",
               command = self.tell_story
               ).grid(row = 8, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 9, column = 0, columnspan = 4)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_loud.get():
            adjectives += "loud, "
        if self.is_quiet.get():
            adjectives += "quiet, "
        if self.is_beautiful.get():
            adjectives += "beautiful, "
        body_part = self.body_part.get()

        # create the story
        story = person
        story += ", was walking through the dark, creepy forest alone when suddenly they heard a noise."
        story += "Turing around " + person + " realized they had stepped on some dangerous "
        story += noun.title()
        story += ". Picking it up they inspected the precious " + noun.title() + " realizing it actually was a "
        story += noun
        story += " that they had found. "
        story += "Not so far in the distance they heard a "
        story += adjectives
        story += " roar. A peculiar feeling overwhelmed the explorer. "
        story += "Scared and alone the adventurer felt a feeling of regret in their "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Never "
        story += verb
        story += " into the forest alone! The end."
        
        # display the story                                
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# main
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()

