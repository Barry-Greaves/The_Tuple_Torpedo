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
        
        #Changes board size based on difficulty level 
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

    def create_player_board(self):
        """
        Create battleships board for the player
        """
        for i in range(self.board_size):
            self.player_board.append(["."] * self.board_size)
    
    def create_computer_board(self):
        """
        Create battleships board for the computer
        """
        for i in range(self.board_size):
            self.computer_board.append(["."] * self.board_size)
            self.hidden_computer_board.append(["."] * self.board_size)
    
    def place_ships_player(self):
        """
        Place ships on the player's board"
        """
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.player_board[row][col] == ".":
                    self.player_ships.append((row, col))
                    self.player_board[row][col] = "S"
                    placed = True

    def place_ships_computer(self):
        """
        Place ships on computer's hidden board so the player cannot see them"
        """
        for i in range(self.num_ships):
            placed = False
            while not placed:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
                if self.hidden_computer_board[row][col] == ".":
                    self.computer_ships.append((row, col))
                    self.hidden_computer_board[row][col] = "S"
                    placed = True

    def check_shot_player(self, row, col):
        """
        Check if the player's shot has hit one of the computer's battleships
        """
        if (row, col) in self.player_ships:
            self.player_board[row][col] = "X"
            return True
        else:
            self.player_board[row][col] = "M"
         
            return False

    def check_shot_computer(self, row, col):
        """
        Check if the player's shot has hit one of the computer's battleships
        """
        if (row, col) in self.player_ships:
            self.computer_board[row][col] = "X"
            self.hidden_computer_board[row][col] = "X"
            return True
        else:
            self.computer_board[row][col] = "M"
            self.hidden_computer_board[row][col] = "X"
            return False