import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)

def exit_app():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# Ana ekranı oluştur
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

# Menubarı oluştur
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menüyü oluştur
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Create a text area
text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

# Run the application
root.mainloop()
