import pygame
import numpy as np
from constants import *

class GameBoard:
    def __init__(self):
        self.grid = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.available_moves = self.grid
        self.marked_moves = 0

    def check_winner(self, display_winner=False):
        """
        Determines if a player has won the game.
        :param display_winner: Whether to visually display the winning lines.
        :return: 0 if no winner, 1 if player 1 wins, 2 if player 2 wins.
        """
        # Check columns
        for col in range(BOARD_SIZE):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != 0:
                if display_winner:
                    color = CIRCLE_COLOR if self.grid[0][col] == 2 else CROSS_COLOR
                    start_pos = (col * CELL_SIZE + CELL_SIZE // 2, 20)
                    end_pos = (col * CELL_SIZE + CELL_SIZE // 2, WINDOW_SIZE - 20)
                    pygame.draw.line(pygame.display.get_surface(), color, start_pos, end_pos, LINE_THICKNESS)
                return self.grid[0][col]

        # Check rows
        for row in range(BOARD_SIZE):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != 0:
                if display_winner:
                    color = CIRCLE_COLOR if self.grid[row][0] == 2 else CROSS_COLOR
                    start_pos = (20, row * CELL_SIZE + CELL_SIZE // 2)
                    end_pos = (WINDOW_SIZE - 20, row * CELL_SIZE + CELL_SIZE // 2)
                    pygame.draw.line(pygame.display.get_surface(), color, start_pos, end_pos, LINE_THICKNESS)
                return self.grid[row][0]

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            if display_winner:
                color = CIRCLE_COLOR if self.grid[1][1] == 2 else CROSS_COLOR
                start_pos = (20, 20)
                end_pos = (WINDOW_SIZE - 20, WINDOW_SIZE - 20)
                pygame.draw.line(pygame.display.get_surface(), color, start_pos, end_pos, LINE_THICKNESS)
            return self.grid[1][1]

        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2] != 0:
            if display_winner:
                color = CIRCLE_COLOR if self.grid[1][1] == 2 else CROSS_COLOR
                start_pos = (20, WINDOW_SIZE - 20)
                end_pos = (WINDOW_SIZE - 20, 20)
                pygame.draw.line(pygame.display.get_surface(), color, start_pos, end_pos, LINE_THICKNESS)
            return self.grid[1][1]

        # No winner found
        return 0

    def place_symbol(self, row, col, player):
        self.grid[row][col] = player
        self.marked_moves += 1

    def is_cell_empty(self, row, col):
        return self.grid[row][col] == 0

    def get_empty_cells(self):
        return [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE) if self.is_cell_empty(row, col)]

    def is_full(self):
        return self.marked_moves == 9

    def is_empty(self):
        return self.marked_moves == 0
