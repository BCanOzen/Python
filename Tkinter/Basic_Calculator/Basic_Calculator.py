import tkinter as tk


def on_click(button_text):
    if button_text == "C":
        ekran_yazisi.set("")
    elif button_text == "=":
        try:
            result = str(eval(ekran_yazisi.get()))
            ekran_yazisi.set(result)
        except Exception as e:
            ekran_yazisi.set("Error")
    else:
        current_text = ekran_yazisi.get()
        ekran_yazisi.set(current_text + button_text)


# Ana ekranı oluştur
root = tk.Tk()
root.title("Simple Calculator")

# Hesaplama ekranındaki yazıların tutulacağı ekranı belirle
ekran_yazisi = tk.StringVar()

# Hesaplama ekranını oluştur
entry = tk.Entry(root, textvariable=ekran_yazisi, justify='right', font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Butonların yazılarını belirle
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]



# Butonları gride yerleştir
for i, button_text in enumerate(buttons):
    button = tk.Button(root, text=button_text, command=lambda x=button_text: on_click(x), font=('Arial', 18))
    row, col = divmod(i, 4)
    button.grid(row=row + 1, column=col, sticky='nsew')

# Grid hücrelerini yeniden boyutlandırılabilir yap
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Uygulamayı çalıştır
root.mainloop()
