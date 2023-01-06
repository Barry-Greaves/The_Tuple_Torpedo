# The Tuple Torpedo

The Tuple Torpedo is a Python based battleships game the players an computer take turns trying to sink each other's ships. The game is played on square grids, with a number of ships placed on each grid.The first player to sink all of the other player's ships wins the game.

![tuple_tornado](https://user-images.githubusercontent.com/107034179/210928143-23ae2b0a-3190-49c2-bb82-bbc322d559cf.png)

Deployed app: https://the-tuple-torpedo.herokuapp.com/

## How to Play
To start the game, select yes when asked if you want to play and follow the prompts to select a rank level.

Once the game has started, you will be shown your own board and the computer's board. You will then be asked to enter coordinates for your shot. .

If your shot hits one of the computer's ships, you will be told that you hit a ship and you will get to take another turn. If your shot misses, the computer will take its turn.

The game continues until one player sinks all of the other player's ships, at which point the game will end and the winner will be announced.

## Features

### Difficulty Levels

Tuple Torpedo offers five difficulty levels. The user is asked to select their rank which assigns a difficulty level

![Screen Shot 2023-01-06 at 03 34 30](https://user-images.githubusercontent.com/107034179/210924942-b4056288-505c-4a68-a846-f640ca29c132.png)


### Board Sizes 

Based on the users rank they are assigned a different board size from 4X4 for Rookies all the way up to 16X16 for the mighty Admirals.

![Screen Shot 2023-01-06 at 03 39 52](https://user-images.githubusercontent.com/107034179/210925350-30e9fd20-cf46-4795-8835-3288c0727010.png)

- Rookie: 4x4 board, 4 ships
- Lieutenant: 6x6 board, 6 ships
- Commander: 10x10 board, 10 ships
- Captain: 12x12 board, 12 ships
- Admiral: 16x16 board, 16 ships

## Generative Messages

There are several points in Tuple Torpedo where the user will receive different messages depending on the state of the game. Some examples include:

- If the user selects that they do not want to play they will receive 
- When the user selects their difficulty level, they will receive a different message depending on their choice using an if/elif statement
- When the user takes a turn, they will receive a message telling them whether their shot hit or missed.
- If the user sinks or misses one of the computer's ships, they will receive one of many possible different messages generated using the print random choice function which selects a random print statement from a list.
- If the user loses the game, they will receive a message telling them that they lost and the game will end.
- If the user wins the game, they will receive a message telling them that they won and the game will end.

![Screen Shot 2023-01-06 at 03 50 38](https://user-images.githubusercontent.com/107034179/210926440-97005589-8a02-48c3-a92d-3b9292958632.png)

![Screen Shot 2023-01-06 at 03 53 28](https://user-images.githubusercontent.com/107034179/210926865-4a0b7ac8-55ea-49e8-b42d-decebc2c367f.png)

![Screen Shot 2023-01-06 at 03 53 05](https://user-images.githubusercontent.com/107034179/210926867-95cc9ad0-cba8-4c58-87c9-2003140c3bbe.png)

![Screen Shot 2023-01-06 at 03 50 14](https://user-images.githubusercontent.com/107034179/210926930-05d30b3c-2a13-48cd-83fe-c48c654c2fe3.png)

These messages are displayed using the print function and are intended to inform the user of the current state of the game and what their next steps should be.

## Data Model

The TupleTorpedoGame class uses several data structures to model the game state and store information about the player and computer boards, as well as the ships on each board.

The player and computer boards are represented as lists of lists of strings, where each string represents a cell on the board. The value of each cell is either "." if the cell has not been attacked, "S" if it contains a ship, "M" if it was a missed shot, or "X" if it was a successful shot.

The player and computer ships are represented as lists of tuples, where each tuple contains the (row, col) coordinates of a ship on the board.

The game also keeps track of the difficulty level, board size, and number of ships for each game using instance variables.

Overall, the TupleTorpedoGame class uses these data structures and variables to model the state of the game and store information about the player and computer boards and ships, as well as the current game settings. This information is used by the various methods in the class to update the game state and check for wins or losses

### Random

The import random statement is used to import the random module, which provides functions for generating random numbers and selecting random elements from a list.

### Time

The time module provides functions for working with time and date values.

In the TupleTorpedoGame class, the time module is only used in the print_boards method to add a delay between printing the player board and the computer board. This is done using the time.sleep function, which causes the program to pause for a specified number of seconds.

By using the time module, the TupleTorpedoGame class is able to add a pause between printing the player and computer boards, which helps build tension and makes the game more visually appealing and easier to follow.

## Testing

I tested the project using the Code Institue PEP8 linter. It did not throw up any major errors, just a lot of white space and sytax errors which were easy to solve. Some line of code were too long and some of these are in the final code because the break line function was not working on print statements unless I changed the indentation, which gave another error in PEP8.

This is the third itteration of a Battleships app using Python, the majority of the testing was done using the terminal in Github.

![Screen Shot 2023-01-06 at 03 07 15](https://user-images.githubusercontent.com/107034179/210928932-52d4a0dc-c802-4a91-a625-1fa63dd90e06.png)

## Notes

- The game does not currently support two player mode.
- The game does not have any way to save progress, so once a game is over it cannot be resumed.
- The Admiral level board is a little to big to provide a good user experience as they cannot view both boards at once. This does add to the difficulty level, but anyone who assigns themselves the rank of Admiral should be able to handle it. 

## Bugs

If the user enters letters for their coordinates it creates an error. I could not implement the is alpha method correctly into the loop and unfortunately this is still an issue. 

## Future Plans

- Fix the outstanding bug outlined abouve. 
- Add support for two player mode.
- Add the ability to save and resume games.
- Add more customization options, such as allowing players to choose the size and placement of their ships.

## Credits

[Code Institute Python Essentials](codeinstitute.net)

More concepts were learnt in [Python Intermediate Project Assignment: Learn How to make Battleships](https://www.youtube.com/watch?v=MgJBgnsDcF0&t=236s)

