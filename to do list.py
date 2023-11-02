import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI elements
root.configure(bg="lightblue")
entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
listbox = tk.Listbox(root, width=40, height=10)

# Place GUI elements on the window
entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
listbox.pack()

# Start the main event loop
root.mainloop()