"""
Minesweeper Game using Pygame

This is a text-based implementation of the classic Minesweeper game in Python. 
The game generates a 10x10 grid with 15 randomly placed mines. 
Players can reveal cells, flag suspected mines, and win by uncovering all non-mine cells.

Author: MGC https://github.com/mgc-00/ 07/02/2025
"""

import random
import os
import pygame

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_flagged = False
        self.is_revealed = False
        self.adjacent_mines = 0

    def reveal(self):
        self.is_revealed = True

    def toggle_flag(self):
        self.is_flagged = not self.is_flagged

    def set_adjacent_mines(self, count):
        self.adjacent_mines = count

class Board:
    def __init__(self, num_rows, num_cols, num_mines):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.cells = [[Cell() for _ in range(num_cols)] for _ in range(num_rows)]
        self.initialize_board()

    def initialize_board(self):
        self.place_mines()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.set_adjacent_mines(row, col)

    def place_mines(self):
        mine_positions = random.sample(range(self.num_rows * self.num_cols), self.num_mines)
        for pos in mine_positions:
            row, col = divmod(pos, self.num_cols)
            self.cells[row][col].is_mine = True

    def set_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.num_rows, row + 2)):
            for c in range(max(0, col - 1), min(self.num_cols, col + 2)):
                if (r != row or c != col) and self.cells[r][c].is_mine:
                    count += 1
        self.cells[row][col].set_adjacent_mines(count)

    def reveal_adjacent_cells(self, row, col):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                r, c = row + dr, col + dc
                if 0 <= r < self.num_rows and 0 <= c < self.num_cols:
                    adjacent_cell = self.cells[r][c]
                    if not adjacent_cell.is_revealed and not adjacent_cell.is_flagged:
                        adjacent_cell.reveal()
                        if adjacent_cell.adjacent_mines == 0:
                            self.reveal_adjacent_cells(r, c)

    def reveal_cell(self, row, col):
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            cell = self.cells[row][col]
            if not cell.is_revealed and not cell.is_flagged:
                cell.reveal()
                if cell.is_mine:
                    return False
                if cell.adjacent_mines == 0:
                    self.reveal_adjacent_cells(row, col)
        return True

    def flag_cell(self, row, col):
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            cell = self.cells[row][col]
            if not cell.is_revealed:
                cell.toggle_flag()

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("   " + " ".join(f"{col:2}" for col in range(self.num_cols)))

        for i, row in enumerate(self.cells):
            row_display = f"{i:2} "  
            for cell in row:
                if cell.is_revealed:
                    row_display += f" {cell.adjacent_mines if not cell.is_mine else 'X'} "
                elif cell.is_flagged:
                    row_display += " F "
                else:
                    row_display += " . "
            print(row_display)

class Game:
    def __init__(self, board):
        self.board = board
        self.game_over = False
        self.win = False

    def start_game(self):
        self.board = Board(self.board.num_rows, self.board.num_cols, self.board.num_mines)
        self.game_over = False
        self.win = False
        os.system('cls' if os.name == 'nt' else 'clear')

    def play(self):
        while not self.game_over:
            self.board.display_board()
            row, col = UserInterface.get_user_input(self.board)
            if not self.board.reveal_cell(row, col):
                self.game_over = True
            else:
                self.check_win()

    def check_win(self):
        if all(cell.is_revealed or cell.is_mine for row in self.board.cells for cell in row):
            self.game_over = True
            self.win = True

    def end_game(self):
        self.board.display_board()
        print("You win!" if self.win else "Game over! You hit a mine.")

class UserInterface:
    @staticmethod
    def get_user_input(board):
        while True:
            try:
                row = int(input(f"Enter row (0-{board.num_rows - 1}): "))
                col = int(input(f"Enter col (0-{board.num_cols - 1}): "))
                if 0 <= row < board.num_rows and 0 <= col < board.num_cols:
                    return row, col
                print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Enter numbers only.")

if __name__ == '__main__':
    while True:
        board = Board(10, 10, 15)  # 10x10 board with 15 mines
        game = Game(board)
        game.start_game()
        game.play()
        game.end_game()

        restart = input("Do you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            break

    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Minesweeper")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
