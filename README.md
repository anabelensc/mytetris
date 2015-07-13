#Tetris clone

A small clone of Tetris that I made in my free time.

## System requirements

The game has been developed using pygame 1.9.1 and python 2.7.6.

## Running the game

The game is simply run with the command:

```
    python main.py
```

#### Game controls

     - Left arrow: Moves the piece one position to the left.
     - Right arrow: Moves the piece one position to the right. 
     - Down arrow: Hold the key down to increase the fall velocity of the piece.
     - Up arrow: Rotates the piece.
     - P: Pauses the game.
     - Esc: Quits the game.

## Some design notes

### Modules 

The game is structured in three components:
    
    - Graphics: contains functions and data to render rectangles and text.
    - Input: manages the keyboard input.
    - Game layers: the game logic is divided in design in four responsibility layers.
        * InitLayer: shows the initial game menu.  
        * GameLayer: runs the game loop, performing the input handling, game update and rendering.
        * GameOverLayer: shows the game over screen.
        * PauseLayer: shows the pause screen when the game is stopped.
    
### Game logic

The game logic is responsible for the general rules of the game. It represents the game status 
as a logical board of blocks of different colors. Each game piece is a shape represented internally by a 4x4 matrix of blocks, where each block can be either colored or empty.

#### Simulation steps

In order to make the game run at the same speed on every platform, the game loop simulates fixed update time steps of 50 milliseconds each.  

#### Level difficulty and score

The level difficulty drives the velocity of the falling piece. At a higher game level, the piece will fall faster. The game level increases every time ten lines are cleared out.

The game score is based on the number of lines that are cleared out. Whenever a line is cleared, a certain score value is added to the player's total score. The accumulated score value depends on the number of line that is cleared at the current level, according to the table shown below.

|Level   |1 line   | 2 lines |3 lines  |4 lines   | More than 4 lines |
|-------:|--------:|--------:|--------:|---------:|------------------:|
| 0      |    40   |     100 |    300  |   1200   |  1200             |
| 1      |    80   |     200 |    600  |   2400   |  2400             |
| .      |     .   |      .  |      .  |      .   |     .             |
| .      |     .   |      .  |      .  |      .   |     .             |
| .      |     .   |      .  |      .  |      .   |     .             |
| n      |40*(n+1) |100*(n+1)|300*(n+1)|1200*(n+1)|1200*(n+1)         |

