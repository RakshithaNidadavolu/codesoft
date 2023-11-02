from logging import root
import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="lightpink")


# Input fields
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)

entry_num1.pack()
entry_num2.pack()

# Operation selection
operation_var = tk.StringVar()
operation_var.set("+")

operation_label = tk.Label(window, text="Choose operation:")
operation_label.pack()

                  
addition_radio = tk.Radiobutton(window, text="+", variable=operation_var, value="+")
subtraction_radio = tk.Radiobutton(window, text="-", variable=operation_var, value="-")
multiplication_radio = tk.Radiobutton(window, text="*", variable=operation_var, value="*")
division_radio = tk.Radiobutton(window, text="/", variable=operation_var, value="/")

addition_radio.pack()
subtraction_radio.pack()
multiplication_radio.pack()
division_radio.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()


# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the tkinter main loop
window.mainloop()
