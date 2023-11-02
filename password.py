import tkinter as tk
import random
import string

def generate_password():
    username = username_entry.get()
    password_length = int(length_entry.get())

    if password_length <= 0:
        result_password_var.set("Password length must be greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))

    result_password_var.set(generated_password)

def reset():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    result_password_var.set("")

def reset_program():
    reset()

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="lightblue")
root.geometry("260x250")

# Create and place labels, entry fields, and buttons
username_label = tk.Label(root, text="Username:", anchor="center", justify="center")
username_label.grid(row=0, column=0, pady=5, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, pady=5)

length_label = tk.Label(root, text="Number of Characters:", anchor="center", justify="center")
length_label.grid(row=1, column=0, pady=5, sticky="e")

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, pady=5)

password_label = tk.Label(root, text="Password Generated:", anchor="center", justify="center")
password_label.grid(row=2, column=0, pady=5, sticky="e")

result_password_var = tk.StringVar()
result_password_entry = tk.Entry(root, textvariable=result_password_var, state='readonly')
result_password_var.set("")
result_password_entry.grid(row=2, column=1, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=4, column=0, columnspan=2, pady=5)

accept_button = tk.Button(root, text="Accept", command=reset_program)
accept_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
