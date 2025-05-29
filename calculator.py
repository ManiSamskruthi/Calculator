import tkinter as tk

# Function to update the expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total  # Reset expression to the result
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the input
def clear():
    global expression
    expression = ""
    equation.set("")

# Main GUI window
root = tk.Tk()
root.configure(background="light grey")
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
equation = tk.StringVar()

# Input field
expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), justify='right')
expression_field.grid(columnspan=4, ipadx=8, ipady=15, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    else:
        action = lambda x=text: press(x)
    tk.Button(root, text=text, command=action, height=2, width=7, font=('Arial', 14)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text='Clear', command=clear, height=2, width=31, font=('Arial', 14)).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
