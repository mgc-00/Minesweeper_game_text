https://github.com/mgc-00/

Minesweeper (Text-Based) – Python Implementation

Overview

This is a text-based implementation of the classic Minesweeper game in Python. 
The game generates a 10x10 grid with 15 randomly placed mines. 
Players can reveal cells, flag suspected mines, and win by uncovering all non-mine cells.
________________________________________
How to Play

1.	The game starts with a hidden grid.
2.	Players take turns choosing a row and column to reveal a cell.
3.	If the cell contains a mine, the game is over.
4.	If the cell is empty, it will reveal adjacent cells recursively until numbered cells are reached.
5.	If the cell contains a number, it indicates how many mines are adjacent.
6.	Players can flag cells they suspect contain mines.
7.	The game continues until:
o	All non-mine cells are revealed (You Win! 🎉)
o	A mine is revealed (Game Over! 💥)
8.	After the game ends, players have the option to restart or quit.
________________________________________
Game Algorithm

1. Initializing the Game:
•	A 10x10 grid is created.
•	15 mines are placed randomly on the grid.
•	Non-mine cells are initialized as empty.
2. Displaying the Grid:
•	The grid starts hidden.
•	Players see only " . " for unrevealed cells and " F " for flagged cells.
•	Once revealed, cells display:
o	"X" for mines.
o	A number (0-8) for adjacent mines.
3. User Input Handling:
•	The player selects a row and column (e.g., 2 3).
•	Input is validated to ensure it's within the board’s bounds.
4. Cell Reveal Logic:
•	If the cell is a mine, the player loses.
•	If the cell is empty, it reveals itself and adjacent cells recursively until a numbered cell is reached.
•	If the cell has a number, only that cell is revealed.
5. Counting Adjacent Mines:
•	Each numbered cell shows the count of mines in adjacent cells.
•	Edge cases are handled to prevent errors near borders.
6. Flagging Cells:
•	Players can flag cells they believe contain mines (F).
•	Flagging prevents accidental reveals.
7. Win Condition Check:
•	If all non-mine cells are revealed, the player wins.
•	If a mine is revealed, the game ends.
8. Restarting the Game:
•	After winning or losing, players can choose to restart or exit.
•	The board is cleared, and a new game begins.
________________________________________
How to Run the Game

1. Install Python (If Not Installed)

Ensure you have Python 3.x installed. You can download it from:

https://www.python.org/downloads/

2. Run the Game

Save the script as minesweeper.py and run:

________________________________________
Executable file 

A compiled .exe of the game can be found in the dist folder.
   
   