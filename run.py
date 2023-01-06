import random
import time

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
            self.computer_board[row][col] = "X"
            self.hidden_computer_board[row][col] = "X"
            return True
        else:
            self.computer_board[row][col] = "M"
            self.hidden_computer_board[row][col] = "X"
            return False

    def check_shot_computer(self, row, col):
        """
        Check if the computer's shot has hit one of the computer's battleships
        """
        if (row, col) in self.player_ships:
            self.player_board[row][col] = "X"
            return True
        else:
            self.player_board[row][col] = "M" 
            return False

    def check_win_player(self):
        """
        Check if the player has won the game
        """
        for row in self.hidden_computer_board:
            if "S" in row:
                return False
        return True

    def check_win_computer(self):
        """
        Check if the computer has won the game
        """
        for row in self.player_board:
            if "S" in row:
                return False
        return True

    def print_player_board(self):
        """
        Prints player's board to CLI
        """
        for row in self.player_board:
            print(" ".join(row))

    def print_computer_board(self):
        """
        Prints computer's board to CLI
        """
        print("\nThe enemy's board:")
        for row in self.computer_board:
            print(" ".join(row))
    
    def computers_turn(self):
        """
        Creates a random shot for the computer to take at the player
        """
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)
        return row, col

valid_ranks = ["Rookie", "Lieutenant", "Commander", "Captain", "Admiral"]
hit_statements = ["Direct hit! You sunk the enemey's battleship", "Success! You incinerated their ship", "The enemy is running scared, you destroyed their battleship!" "Wow you are like the Navy version of Tom Cruise in Top Gun. What a great shot" "How did you make that one? The enemy can't take many more hits like that!"]
miss_statements = ["Bad shot! We don't have unlimited ammo. Get it together!", "Missed again. Well the next one better hit, we will be in real trouble soon", "Uh oh, that one was way off. It's ok it happens to the best of us, try to actually aim next time", "That was so close, we will get them next time"]

def main():
    """
    Main function which initializes the game loop
    """
    print("-----------------------------\nWelcome to The Tuple Torpedo\nA Python CLI Battleships game\nS == Ship, X == Hit, M == Miss\n-----------------------------")

    play = input("\nWould you like to play a The Tuple Torpedo? Yes or No?")
    while play.lower() != "y" and play.lower() != "yes":
        play = input("Come on don't be a coward. The Tuple Torpedo awaits. What say you? Yes or No?")
    
    name = input("\nEnter your name: ")
    
    difficulty = input("Please select your rank: Rookie, Lieutenant, Commander, Captain or Admiral: ")
    while difficulty not in valid_ranks:
        print("Select your rank from the list provided. You must be a rookie right?")
        difficulty = input("Please select your rank: Rookie, Lieutenant, Commander, Captain or Admiral: ")
   
    if difficulty == "Rookie":
        print(f"\nHello Rookie {name}, don't mess this up.")
    elif difficulty == "Lieutenant":
        print(f"\nHello Lieutenant {name}, let's get locked and loaded.")
    elif difficulty == "Commander":
        print(f"\nHello Commander {name}, it is good to have you with us today, let's take em out!")
    elif difficulty == "Captain":
        print(f"\nHello Captain {name}, let's blow the enemy out of the water.")
    elif difficulty == "Admiral":
        print(f"\nHello Admiral {name}, it is an honour to be working with you sir")

    
    # Create instance of game using difficulty level selected
    game = TupleTorpedoGame(difficulty)
    game.create_player_board()
    game.create_computer_board()
    game.place_ships_player()
    game.place_ships_computer()

    #Prompt user to take their turn
    while True:
        print(f"\n{difficulty} {name}'s board:")
        game.print_player_board()
        game.print_computer_board()
        row = int(input("\nEnter coordinates for torpedo launch: row (0-{}): ".format(game.board_size - 1)))
        while row < 0 or row >= game.board_size:
            print("Invalid row. Please enter a valid row.")
            row = int(input("Enter row (0-{}): ".format(game.board_size - 1)))
        col = int(input("Enter coordinates for torpedo launch: column (0-{}): ".format(game.board_size - 1)))
        while col < 0 or col >= game.board_size:
            print("Invalid column. Please enter a valid column.")
            col = int(input("Enter column (0-{}): ".format(game.board_size - 1)))

        #Wait a moment for the torpedo to land, or not ....       
        timer = ["................\n\n"]
        for dots in timer: 
            print(dots, end='', flush=True) 
            time.sleep( 1 )
        
        #Check if the player's shot has landed
        if game.check_shot_player(row, col):
            print(random.choice(hit_statements))
        else:
            print(random.choice(miss_statements))

        #Check if the game has been won
        if game.check_win_player():
            print("You are the Tuple Torpedo Champion!")
            break
        
        #Wait a moment for the torpedo to land, or not ....     
        timer = ["................\n\n"]
        for dots in timer: 
            print(dots, end='', flush=True) 
            time.sleep( 1 )

        #Check if the computer's shot has landed
        row, col = game.computers_turn()
        if game.check_shot_computer(row, col):
            print("The enemy hit your ship at {}, {}!".format(row, col))
        else:
            print("The enemy missed your ship at {}, {}. Now its time to take them out!".format(row, col))

        timer = ["................\n\n"]
        for dots in timer: 
            print(dots, end='', flush=True) 
            time.sleep( 1 )
        
        #Check if the game has been won
        if game.check_win_computer():
            print("The enemy has defeated you!")
            break

main()

