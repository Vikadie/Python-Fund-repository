import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #create widgets
        self.label = tk.Label(text = "Catch me if you can!")
        self.button = tk.Button(text = "Catch me!", command = self.on_click)

        #place widgets
        self.label.pack(side = "left")
        self.button.pack(side = "left")

        # bind functions to events
        # mouse is over -> move button
        # leave button -> clear text
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        #if self.button.pack(side == "left") or self.button.pack(side = None):
        self.button.pack(side = "right", padx = x, pady = y)
        #elif self.button.pack(side == "right"):
        #    self.button.pack(side="left", padx = x, pady = y)

    def on_leave(self, event):
        self.label.config(text = "Almost!")

    def on_click(self):
        self.label.config(text = "You win!")


# create the application
app = Application()
app.master.title("Catch the Button!")
app.master.minsize(width = 400, height = 200)

# start the program
app.mainloop()