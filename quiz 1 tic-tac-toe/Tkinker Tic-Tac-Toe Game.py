import tkinter as tk
from tkinter import messagebox

player = "X"
buttons = [[None]*3 for _ in range(3)]

def check_winner():
    # Return winning cells if someone wins
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return [(i,0), (i,1), (i,2)]
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return [(0,i), (1,i), (2,i)]
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return [(0,0), (1,1), (2,2)]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return [(0,2), (1,1), (2,0)]
    return None

def button_click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        winner_cells = check_winner()
        if winner_cells:
            # Highlight winning buttons
            for r,c in winner_cells:
                buttons[r][c]["bg"] = "lightgreen"
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            root.after(1000, reset_board)
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            root.after(1000, reset_board)
        else:
            player = "O" if player == "X" else "X"
            label.config(text=f"Player {player}'s turn")

def reset_board():
    global player
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""
            buttons[r][c]["bg"] = "SystemButtonFace"
    player = "X"
    label.config(text=f"Player {player}'s turn")

# Tkinter setup
root = tk.Tk()
root.title("Tic-Tac-Toe")
label = tk.Label(root, text=f"Player {player}'s turn", font=("Arial", 20))
label.grid(row=0, column=0, columnspan=3)

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                                  command=lambda r=r, c=c: button_click(r, c))
        buttons[r][c].grid(row=r+1, column=c, padx=5, pady=5)

root.mainloop()
