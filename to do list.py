import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} [Done]")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Create widgets
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
mark_done_button = tk.Button(root, text="Mark as Done", command=mark_done)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
task_listbox = tk.Listbox(root, width=50, height=15)

# Place widgets
task_entry.pack(pady=10)
add_button.pack(pady=5)
delete_button.pack(pady=5)
mark_done_button.pack(pady=5)
clear_button.pack(pady=5)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()
