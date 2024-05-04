import copy
from board import GameBoard

class GameAI:
    def __init__(self, player=2):
        """
        Initializes the AI agent.
        :param player: The player number representing the AI.
        """
        self.player = player  # Player 2 (circles)

    def choose_move(self, game_board: GameBoard):
        """
        Determines the AI's next move using the minimax algorithm.
        :param game_board: The current state of the game board.
        :return: A tuple (row, col) representing the AI's chosen move.
        """
        evaluation, best_move = self.minimax(game_board, False)
        
        # Print the AI's chosen move and evaluation to the terminal
        print(f"AI has chosen to mark the square in pos {best_move} with the evaluation of: {evaluation}")
        
        return best_move

    def minimax(self, board, is_maximizing):
        """
        Minimax algorithm implementation.
        :param board: The current state of the game board.
        :param is_maximizing: A boolean indicating whether the current player is maximizing or minimizing.
        :return: A tuple (evaluation, move) representing the evaluation score and the move.
        """
        # Check the game state
        state = board.check_winner()
        if state == 1:
            return 1, None  # Player 1 wins
        elif state == 2:
            return -1, None  # Player 2 (AI) wins
        elif board.is_full():
            return 0, None  # Draw

        best_move = None
        if is_maximizing:
            best_score = float('-inf')
            empty_cells = board.get_empty_cells()
            for (row, col) in empty_cells:
                temp_board = copy.deepcopy(board)
                temp_board.place_symbol(row, col, 1)  # Player 1's move
                score, _ = self.minimax(temp_board, False)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
            return best_score, best_move
        else:
            best_score = float('inf')
            empty_cells = board.get_empty_cells()
            for (row, col) in empty_cells:
                temp_board = copy.deepcopy(board)
                temp_board.place_symbol(row, col, self.player)  # AI's move
                score, _ = self.minimax(temp_board, True)
                if score < best_score:
                    best_score = score
                    best_move = (row, col)
            return best_score, best_move
