from tkinter import *
import operator
import sympy

# Create the basic window
root = Tk() 
root.geometry("350x430")
root.resizable(0, 0)
root.title("PyCalc")
root.iconphoto(False, PhotoImage(file="plus.png"))

# Create Application
app = root

#
# Input
#

# Input Frame
input_text = StringVar()
input_frame = Frame(app, width=312, height=50, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

# Input Field
input_field = Entry(input_frame, font=("Helvetica", 20, "bold"), textvariable=input_text, width=50, bg="#eee", justify=LEFT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

def clear():
    input_field.delete(0, "end")

def click(item):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul
    }
    op = ""
    num1 = 0
    num2 = 0
    if type(item) != str:
        input_text.set(input_text.get() + str(item))
        if op == "":
            num1 = input_text.get()
        else:
            num2 = input
    elif item == "=":
        input_text.set(sympy.sympify(input_text.get()))

    elif type(item) == str and op == "":
        op = item
        input_text.set(input_text.get() + item)


#
# Buttons
#

# Button Frame
buttons_frame = Frame(app, width=312, height=272.5, bg="grey")
buttons_frame.pack()

# First Button Row
btn_clear = Button(buttons_frame, text="C", fg="black", width=34, height=4, bg="#eee", command=lambda : clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
btn_divide = Button(buttons_frame, text="/", fg="black", width=10, height=4, bg="#eee", command=lambda : click("/")).grid(row=0, column=3, padx=1, pady=1)

# Second Button Row
btn_seven = Button(buttons_frame, text="7", fg="black", width=10, height=4, bg="#eee", command=lambda: click(7)).grid(row=1, column=0, padx=1, pady=1)
btn_eight = Button(buttons_frame, text="8", fg="black", width=10, height=4, bg="#eee", command=lambda: click(8)).grid(row=1, column=1, padx=1, pady=1)
btn_nine = Button(buttons_frame, text="9", fg="black", width=10, height=4, bg="#eee", command=lambda: click(9)).grid(row=1, column=2, padx=1, pady=1)
btn_multiply = Button(buttons_frame, text="*", fg="black", width=10, height=4, bg="#eee", command=lambda: click("*")).grid(row=1, column=3, padx=1, pady=1)

# Third Button Row
btn_four = Button(buttons_frame, text="4", fg="black", width=10, height=4, bg="#eee", command=lambda: click(4)).grid(row=2, column=0, padx=1, pady=1)
btn_five = Button(buttons_frame, text="5", fg="black", width=10, height=4, bg="#eee", command=lambda: click(5)).grid(row=2, column=1, padx=1, pady=1)
btn_six = Button(buttons_frame, text="6", fg="black", width=10, height=4, bg="#eee", command=lambda: click(6)).grid(row=2, column=2, padx=1, pady=1)
btn_minus = Button(buttons_frame, text="-", fg="black", width=10, height=4, bg="#eee", command=lambda: click("-")).grid(row=2, column=3, padx=1, pady=1)

# Fourth Button Row
btn_one = Button(buttons_frame, text="1", fg="black", width=10, height=4, bg="#eee", command=lambda: click(1)).grid(row=3, column=0, padx=1, pady=1)
btn_two = Button(buttons_frame, text="2", fg="black", width=10, height=4, bg="#eee", command=lambda: click(2)).grid(row=3, column=1, padx=1, pady=1)
btn_three = Button(buttons_frame, text="3", fg="black", width=10, height=4, bg="#eee", command=lambda: click(3)).grid(row=3, column=2, padx=1, pady=1)
btn_plus = Button(buttons_frame, text="+", fg="black", width=10, height=4, bg="#eee", command=lambda: click("+")).grid(row=3, column=3, padx=1, pady=1)

# Fifth Button Row

btn_zero = Button(buttons_frame, text="0", fg="black", width=34, height=4, bg="#eee", command=lambda: click(0)).grid(row=4, column=0, columnspan=3, padx=1, pady=1)
btn_equals = Button(buttons_frame, text="=", fg="black", width=10, height=4, bg="#eee", command=lambda: click("=")).grid(row=4, column=3, padx=1, pady=1)


# Program Start
app.mainloop()