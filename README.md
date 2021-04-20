# Kutyaszorító game

This game uses the Minimax algorithm to try and beat the player. Clone in and launch the game like this:
```python
python console.py 1 3 3
```
With the first argument you can choose who starts the game(1 for the bot and 0 for the user), the second argument is the board size(in the example above this means it's a 3x3 board) and the last one is the depth of the search tree.

# How to play

The game starts with the opponents in the middle on the opposite sides of the board, p1 is player one and p2 is player two:

|       | p1          |   |
| ------------- |:-------------:| -----:|
|        |  |  |
|  |     p2   |  |

A turn is composed of a move to a neighboring tile and an exclusion of any empty field from the game:

|       |         |   |
| ------------- |:-------------:| -----:|
|        | p1  |  |
| x |     p2   |  |

The goal is to take away all the neighboring tiles from the opponent either by excluding them or by stepping on them, when no free space is left, you won.

Have fun!

# TODO

Some of them are:
* helpful error messages
* give another try to move for the user in case of an impossible move
* graphical interface
* resolve end of game situation