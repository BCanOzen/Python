import tkinter as tk
from tkinter import messagebox, font


# Method to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir task girin.")


# Method to delete a task
def delete_task():
    try:
        task_index = listbox.curselection()
        listbox.delete(task_index)
    except:
        messagebox.showwarning("Uyarı", "Silinecek bir görev seçin.")


# Main application class
# Create the window
root = tk.Tk()

root.title('Yapılacaklar Listesi')

# Custom font
custom_font = font.Font(family="Helvetica", size=12)

# Text entry box
entry = tk.Entry(root, width=50, font=custom_font)
entry.pack()

# Add task button
add_task_button = tk.Button(root, text='Görev Ekle', command=add_task, font=custom_font, bg="#add8e6")
add_task_button.pack()

# Delete task button
delete_task_button = tk.Button(root, text='Görevi Sil', command=delete_task, font=custom_font, bg="#ffa07a")
delete_task_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10, font=custom_font)
listbox.pack()

# Start the application
root.mainloop()
