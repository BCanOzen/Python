import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title('X-O Oyunu')
root.resizable(0,0)


current_player = 'X'

buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='',
                                  font=('normal', 40),
                                  width=6, height=3, background='#E0F4FF',
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)


def on_click(i, j):
    global current_player
    if buttons[i][j]['text'] == '' and current_player:
        buttons[i][j]['text'] = current_player
        if check_winner():
            messagebox.showinfo("Oyun Bitti", f"Oyuncu {current_player} kazandı!")
            reset_game()
        elif is_board_full():
            messagebox.showinfo("Oyun Bitti", "Berabere!")
            reset_game()
        else:
            current_player = 'X' if current_player == 'O' else 'O'

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

def is_board_full():
    for row in buttons:
        for button in row:
            if button['text'] == '':
                return False
    return True

def reset_game():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''
    current_player = 'X'


root.mainloop()
