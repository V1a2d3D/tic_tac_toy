import tkinter
import random
import time


class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300, bg="black")
        self.bind("<Button-1>", self.click)
        self.state = [None] * 9
        self.draw_lines()

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill="white")
        self.create_line(200, 0, 200, 300, fill="white")
        self.create_line(0, 100, 300, 100, fill="white")
        self.create_line(0, 200, 300, 200, fill="white")

    def add_x(self, column, row):
        self.create_line(
            column * 100 + 25, row * 100 + 25,
            column * 100 + 75, row * 100 + 75,
            width=5, fill="chartreuse1")

        self.create_line(
            column * 100 + 25, row * 100 + 75,
            column * 100 + 75, row * 100 + 25,
            width=5, fill="chartreuse1")

    def add_o(self, column, row):
        self.create_oval(
            column * 100 + 25, row * 100 + 25,
            column * 100 + 75, row * 100 + 75,
            width=5, outline="aquamarine2")

    def bot_move(self):
        indexes = []
        for index, cell in enumerate(self.state):
            if cell is None:
                indexes.append(index)
        index = random.choice(indexes)
        self.state[index] = "o"
        time.sleep(0.2)
        self.add_o(index % 3, index // 3)

    def click(self, event):
        column = event.x // 100
        row = event.y // 100
        index = row * 3 + column
        if self.state[index] is None:
            self.state[index] = "x"
            self.add_x(column, row)
            result = self.get_winner()
            if result == "X_WON":
                self.create_text(150, 150, text=f"{result}", fill="deep pink", font=('Arial', 60))
                self.new_game()
            elif result == "O_WON":
                self.create_text(150, 150, text=f"{result}", fill="deep pink", font=('Arial', 60))
                self.new_game()
            elif result == "DRAW":
                self.create_text(150, 150, text=f"{result}", fill="deep pink", font=('Arial', 60))
                self.new_game()

            if result is None:
                self.bot_move()
                result = self.get_winner()
                if result == "X_WON":
                    self.create_text(150, 150, text=f"{result}", fill="deep pink", font=('Arial', 60))
                    self.new_game()
                elif result == "O_WON":
                    self.create_text(150, 150, text=f"{result}", fill="deep pink", font=('Arial', 60))
                    self.new_game()
                elif result == "DRAW":
                    self.create_text(150, 150, text=f"{result}", fill="deep pink", font=('Arial', 60))
                    self.new_game()

    def get_winner(self):
        options = []
        for column, row in enumerate(range(0, 9, 3)):
            options.append(self.state[row:(row + 3)])
            options.append(self.state[column::3])

        options.append(self.state[::4])
        options.append(self.state[2:7:2])

        if ["x", ] * 3 in options:
            return "X_WON"
        elif ["o", ] * 3 in options:
            return "O_WON"
        elif None not in self.state:
            return "DRAW"

    def new_game(self):
        time.sleep(2.0)
        self.delete('all')
        self.state = [None] * 9
        self.draw_lines()


main_window = tkinter.Tk()
main_window.title("Tic-Tac-Toe")
game = TicTacToe(main_window)
game.pack()

main_window.mainloop()
