import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, size, mines):
        self.master = master
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self.place_mines()
        self.calculate_numbers()
        self.create_widgets()

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in self.mine_positions:
                self.mine_positions.add((x, y))
                self.board[x][y] = 'M'

    def calculate_numbers(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == 'M':
                    continue
                count = 0
                for i in range(max(0, x - 1), min(self.size, x + 2)):
                    for j in range(max(0, y - 1), min(self.size, y + 2)):
                        if self.board[i][j] == 'M':
                            count += 1
                self.board[x][y] = str(count)

    def create_widgets(self):
        for x in range(self.size):
            for y in range(self.size):
                button = tk.Button(self.master, text='', width=3, command=lambda x=x, y=y: self.reveal(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button

    def reveal(self, x, y):
        if self.board[x][y] == 'M':
            self.buttons[x][y].config(text='M', bg='red')
            self.game_over()
        else:
            self.buttons[x][y].config(text=self.board[x][y], state='disabled', relief=tk.SUNKEN)
            if self.board[x][y] == '0':
                for i in range(max(0, x - 1), min(self.size, x + 2)):
                    for j in range(max(0, y - 1), min(self.size, y + 2)):
                        if self.buttons[i][j]['state'] == 'normal':
                            self.reveal(i, j)
        if self.check_win():
            self.win()

    def game_over(self):
        for x, y in self.mine_positions:
            self.buttons[x][y].config(text='M', bg='red')
        tk.messagebox.showinfo("Game Over", "You hit a mine!")

    def check_win(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != 'M' and self.buttons[x][y]['state'] == 'normal':
                    return False
        return True

    def win(self):
        tk.messagebox.showinfo("Congratulations", "You cleared the minefield!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    size = 5
    mines = 5
    game = Minesweeper(root, size, mines)
    root.mainloop()