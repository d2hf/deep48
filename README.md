# deep48
An numpy enviroment for applying machine learning to the 2048 game.


<h2> Game logic </h3>

The game enviroment provided simulates the 2048 game. The player 
starts with a 4x4 grid with 2 random values whom values can be
2 or 4.
The goal of the player is to merge tiles until the 2048 tile is 
formed. Tiles are made when adjancent tiles of the same value
are swiped against each other.

<h5> Implementation in python </h5>
To achive the desired logic the starting point was sliding the 
tiles to the left. An iteration on the objects of the same row
checks if there are any adjacent tiles of the same value, if so
they are merged to its double.

To do the same on other directions methods of numpy arrays were
implemented to simulate swiping to the left side. E.g. To merge 
itens on the right direction, the game matrix is mirrored, the
logic performs the merging and then when it is done the matrix is
unmirrored. To achieve the same objective in the vertical axis
the mirroring is used when necessary with the transposed matrix.

