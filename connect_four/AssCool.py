#Name: Ashin Alex

import Ass
import tkinter as tk
from tkinter import simpledialog
from Ass import GameBoard

class GameGUI:
    def __init__(self):
        self.board_size = self.get_board_size()
        self.player_name = self.get_player_name()
        self.board = GameBoard(self.board_size)
        self.player = 1
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.geometry("400x450")  
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        self.score_label = tk.Label(self.window, text=f"{self.player_name}: 0  AI: 0", font=("Arial", 16))  
        self.score_label.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)  
        self.window.mainloop()
        

    def get_board_size(self):
        while True:
            size = tk.simpledialog.askinteger("Board Size", "Enter the board size (between 4 and 11):")
            if size is None:
                return None
            if 4 <= size <= 10:
                return size
            else:
                tk.messagebox.showerror("Invalid Size", "Please enter a valid board size between 3 and 11.")
    
    def get_player_name(self):
        player_name = tk.simpledialog.askstring("Name", "Enter your name buddy!")
        return player_name

    def draw_board(self):
        self.canvas.delete("all")
        #game board
        cell_size = 400 // self.board_size
        for row in range(self.board_size):
            for col in range(self.board_size):
                x1 = col * cell_size
                y1 = (self.board_size - 1 - row) * cell_size  
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="cyan")
        #disks
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board.items[col][row] == 1:
                    x = col * cell_size + cell_size // 2
                    y = (self.board_size - 1 - row) * cell_size + cell_size // 2  
                    self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")
                elif self.board.items[col][row] == 2:
                    x = col * cell_size + cell_size // 2
                    y = (self.board_size - 1 - row) * cell_size + cell_size // 2  
                    self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="green")

    def handle_click(self, event):
        column = event.x // (400 // self.board_size)
        if self.board.add(column, self.player):
            self.draw_board()
            if self.board.game_over():
                self.canvas.unbind("<Button-1>")
                winner = self.get_winner()
                self.canvas.create_text(200, 200, text=f"Game Over !!! \n{winner}", font=("Arial", 24), fill="red")
            else:
                if self.player == 1:
                    column, points = self.board.column_resulting_in_max_points(2)
                    self.board.add(column, 2)
                    self.draw_board()
                    if self.board.game_over():
                        self.canvas.unbind("<Button-1>")
                        winner = self.get_winner()
                        self.canvas.create_text(200, 200, text=f"Game Over !!! \n{winner}", font=("Arial", 24), fill="red")
                self.player = 1
        self.update_score()  

    def get_winner(self):
        if self.board.points[0] > self.board.points[1]:
            return f"{self.get_player_name} winns \n You are smarter than AI"
        elif self.board.points[0] < self.board.points[1]:
            return "AI winns \n AI is smarter than you"
        else:
            return "It's a tie."

    def update_score(self):
        self.score_label.config(text=f"{self.player_name}: {self.board.points[0]}  AI: {self.board.points[1]}", font=("Arial", 16))

    def start_game(self):
        self.window.mainloop()

game = GameGUI()
game.start_game()



