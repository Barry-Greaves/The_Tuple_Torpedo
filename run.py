import random

class TupleTorpedoGame:
    """
    Contruct game class that defines difficulty level,
    board size and number of ships
    """
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board_size = 0
        self.num_ships = 0
        self.player_board = []
        self.computer_board = []
        self.hidden_computer_board = []
        self.player_ships = []
        self.computer_ships = []

        self.create_player_board()
        self.place_ships_player()
        self.create_computer_board()
        self.place_ships_computer()
