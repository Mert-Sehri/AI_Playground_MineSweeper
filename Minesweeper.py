import random

class Minesweeper:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[' ' for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self.place_mines()
        self.calculate_numbers()

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

    def reveal(self, x, y):
        if self.board[x][y] == 'M':
            return False
        self.revealed[x][y] = self.board[x][y]
        if self.board[x][y] == '0':
            for i in range(max(0, x - 1), min(self.size, x + 2)):
                for j in range(max(0, y - 1), min(self.size, y + 2)):
                    if self.revealed[i][j] == ' ':
                        self.reveal(i, j)
        return True

    def display(self):
        print("   " + " ".join(str(i) for i in range(self.size)))
        print("  +" + "--" * self.size + "+")
        for idx, row in enumerate(self.revealed):
            print(f"{idx} |" + " ".join(row) + "|")
        print("  +" + "--" * self.size + "+")
        print()

    def play(self):
        while True:
            self.display()
            x, y = map(int, input("Enter coordinates to reveal (row col): ").split())
            if not self.reveal(x, y):
                print("Game Over! You hit a mine.")
                break
            if all(self.revealed[i][j] != ' ' for i in range(self.size) for j in range(self.size) if self.board[i][j] != 'M'):
                print("Congratulations! You cleared the minefield.")
                break

if __name__ == "__main__":
    size = 5
    mines = 5
    game = Minesweeper(size, mines)
    game.play()