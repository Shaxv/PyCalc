from tkinter import *
from tkinter.font import *

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.main_font = Font(family="Helvetica", size=20, weight="bold")        
        self.input_text = StringVar()
        self.counter()
        self.buttons()

    def counter(self):
        self.counterFrame = Frame(self, width=400, height=50, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.counterFrame.pack(side="top")
        self.counter = Entry(self.counterFrame, font=self.main_font, textvariable=self.input_text, width=50, bg="#eee", justify=RIGHT).grid(row=0, column=0)

    def buttons(self):
        self.buttonFrame = Frame(self, width=500, height=272, bg="grey")
        self.buttonFrame.pack()

        def btn_equal():
            pass
        
        def btn_add(item):
            self.counter.insert(0, str(item))
            print(self.counter.get())

        def btn_clear():
            self.counter.delete(0, "end")

        self.clear = Button(self.buttonFrame, text="Clear", fg="black", bd=0, bg="#eee", height=2, width=10, command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        self.add = Button(self.buttonFrame, text="Add", fg="black", bd=0, bg="#eee", height=2, width=10, command=lambda: btn_add("anyad")).grid(row=0, column=3, padx=1, pady=1)


# Create the basic window
root = Tk() 
root.geometry("350x450")
root.resizable(0, 0)
root.title("The Calculator")

# Create Application
app = App(master=root)

# Program start
app.mainloop()

"""

expression = ""

# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()
 
# Let us creating a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()
 
# first row
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1) 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()"""