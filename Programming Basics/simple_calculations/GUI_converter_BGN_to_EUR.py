import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.pack() # method for visualization in tkinter package
        self.create_widgets() # function where we create the widgets (all the components)

    def create_widgets(self):
        #create widgets
        self.label = tk.Label(text = "Value Converter BGN/EUR") # static text with the name of the window
        self.number_entry = tk.Entry() # here we will enter the amount to be converted
        self.convert_button = tk.Button(text = "Convert", command = self.convert)
        self.output = tk.Label() # another label - text for the result (output)

        #place widgets
        self.label.pack(side="left")
        self.number_entry.pack(side="left")
        self.convert_button.pack(side="left")
        self.output.pack(side="left")

    def convert(self):
        entry = self.number_entry.get()

        try:
            value = float(entry)
            result = round(value / 1.95583,2)

            self.output.config(text = str(value) + "BGN = " + str(result) + " EUR", bg = "green", fg = "white")
            # bg - background, fg - font color
        except ValueError:
            self.output.config(text = "That's not a number!", bg = "red", fg = "black")




# create the application
app = Application()
app.master.title("BGN to EUR converter")

# start the program
app.mainloop()
