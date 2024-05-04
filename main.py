import pygame
import sys
from constants import *
from board import GameBoard
from ai import GameAI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic Tac Toe AI")
        self.reset_game()
        
    def reset_game(self):
        self.board = GameBoard()
        self.ai = GameAI()
        self.current_player = 1  # Player 1 starts with crosses
        self.game_mode = 'ai'  # Game mode can be either 'pvp' or 'ai'
        self.is_running = True
        self.draw_board()
    
    def draw_board(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grid_lines()
        pygame.display.update()
        
    def draw_grid_lines(self):
        # Draw vertical lines
        pygame.draw.line(self.screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, WINDOW_SIZE), LINE_THICKNESS)
        pygame.draw.line(self.screen, LINE_COLOR, (WINDOW_SIZE - CELL_SIZE, 0), (WINDOW_SIZE - CELL_SIZE, WINDOW_SIZE), LINE_THICKNESS)
        
        # Draw horizontal lines
        pygame.draw.line(self.screen, LINE_COLOR, (0, CELL_SIZE), (WINDOW_SIZE, CELL_SIZE), LINE_THICKNESS)
        pygame.draw.line(self.screen, LINE_COLOR, (0, WINDOW_SIZE - CELL_SIZE), (WINDOW_SIZE, WINDOW_SIZE - CELL_SIZE), LINE_THICKNESS)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                self.handle_key_events(event)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_events(event)
                
    def handle_key_events(self, event):
        if event.key == pygame.K_g:
            self.toggle_game_mode()
            
        if event.key == pygame.K_r:
            self.reset_game()
            
    def handle_mouse_events(self, event):
        if not self.is_running:
            return
            
        pos = event.pos
        row = pos[1] // CELL_SIZE
        col = pos[0] // CELL_SIZE
        
        if self.board.is_cell_empty(row, col):
            self.make_move(row, col)
            if self.check_game_over():
                return
                
            if self.game_mode == 'ai' and self.current_player == self.ai.player:
                ai_move = self.ai.choose_move(self.board)
                self.make_move(*ai_move)
                self.check_game_over()
                
    def make_move(self, row, col):
        self.board.place_symbol(row, col, self.current_player)
        self.draw_symbol(row, col)
        self.switch_player()
        
    def draw_symbol(self, row, col):
        if self.current_player == 1:
            self.draw_cross(row, col)
        elif self.current_player == 2:
            self.draw_circle(row, col)
            
        pygame.display.update()
        
    def draw_cross(self, row, col):
        start_desc = (col * CELL_SIZE + OFFSET, row * CELL_SIZE + OFFSET)
        end_desc = (col * CELL_SIZE + CELL_SIZE - OFFSET, row * CELL_SIZE + CELL_SIZE - OFFSET)
        pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_THICKNESS)
        
        start_asc = (col * CELL_SIZE + OFFSET, row * CELL_SIZE + CELL_SIZE - OFFSET)
        end_asc = (col * CELL_SIZE + CELL_SIZE - OFFSET, row * CELL_SIZE + OFFSET)
        pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_THICKNESS)
        
    def draw_circle(self, row, col):
        center_pos = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.circle(self.screen, CIRCLE_COLOR, center_pos, CIRCLE_RADIUS, CIRCLE_THICKNESS)
        
    def switch_player(self):
        self.current_player = 1 if self.current_player == 2 else 2
        
    def toggle_game_mode(self):
        self.game_mode = 'ai' if self.game_mode == 'pvp' else 'pvp'
        
    def check_game_over(self):
        winner = self.board.check_winner(True)  # Call with display_winner=True
        if winner != 0 or self.board.is_full():
            self.is_running = False
            return True
        return False
    
    def run(self):
        # Main game loop

        while True:
            self.handle_events()
            pygame.display.update()


if __name__ == "__main__":
    main_game = Game()
    main_game.run()
