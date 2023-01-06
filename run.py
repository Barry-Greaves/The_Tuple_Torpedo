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

        if self.difficulty == "Rookie":
            self.board_size = 4
            self.num_ships = 4
        elif self.difficulty == "Lieutenant":
            self.board_size = 6
            self.num_ships = 6
        elif self.difficulty == "Commander":
            self.board_size = 10
            self.num_ships = 10
        elif self.difficulty == "Captain":
            self.board_size = 12
            self.num_ships = 12
        elif self.difficulty == "Admiral":
            self.board_size = 16
            self.num_ships = 16
