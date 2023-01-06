# The Tuple Torpedo

The Tuple Torpedo is a Python based battleships game the players an computer take turns trying to sink each other's ships. The game is played on square grids, with a number of ships placed on each grid.The first player to sink all of the other player's ships wins the game.


## How to Play
To start the game, select yes when asked if you want to play and follow the prompts to select a rank level.

Once the game has started, you will be shown your own board and the computer's board. You will then be asked to enter coordinates for your shot. .

If your shot hits one of the computer's ships, you will be told that you hit a ship and you will get to take another turn. If your shot misses, the computer will take its turn.

The game continues until one player sinks all of the other player's ships, at which point the game will end and the winner will be announced.

## Difficulty Levels
Tuple Torpedo offers five difficulty levels, each with a different board size and number of ships:

- Rookie: 4x4 board, 4 ships
- Lieutenant: 6x6 board, 6 ships
- Commander: 10x10 board, 10 ships
- Captain: 12x12 board, 12 ships
- Admiral: 16x16 board, 16 ships

## Notes

The game does not currently support two player mode.
The game does not have any way to save progress, so once a game is over it cannot be resumed.

## Bugs

If the user enters letters for their coordinates it creates an error. I could not implement the is alpha method correctly into the loop and unfortunately this is still an issue. 

## Future Plans

- Fix the outstanding bug outlined abouve. 
- Add support for two player mode.
- Add the ability to save and resume games.
- Add more customization options, such as allowing players to choose the size and placement of their ships.

