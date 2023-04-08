Game of Life
============

History
-------
The Game of Life is a cellular automaton devised by
the British mathematician John Horton Conway in 1970.

It is a zero-player game, meaning that its evolution is
determined by its initial state, requiring no further input.


Rules
-----
The universe of the **Game of Life** is an infinite,
two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states, live or dead.

Every cell interacts with its eight neighbours,
(horizontally, vertically, or diagonally adjacent).

At each step in time, the following transitions occur
simultaneously for all cells in the grid:

- any live cell with fewer than 2 live neighbours dies (underpopulation);
- any live cell with 2 or 3 live neighbours stays alive;
- any live cell with more than 3 live neighbours dies (overpopulation);
- any dead cell with exactly 3 live neighbours becomes alive (reproduction).

In other words:

- live cell with 2 or 3 live neighbours survives;
- dead cell with 3 live neighbours becomes a live cell;
- every other cell dies or stay dead.

Example
-------
In this chart `█` is an alive cell, while empty spaces are dead.

```
   ABCDEFGHIJ            ABCDEFGHIJ    
  +----------+          +----------+     
1 |          |        1 |          |     
2 |    █     |        2 |   ███    |          
3 |   ███    |======> 3 |   █ █    |            
4 |   █      |        4 |   █      |         
  +----------+          +----------+     
```

- Cell B2 is dead and stays dead because it has 0 alive neighbors
- Cell F2 is dead and becomes alive because it has 3 alive neighbors
- Cell E2 is alive and stays alive because it has 3 alive neighbors
- Cell E3 is alive and becomes dead because it has 4 alive neighbors

Your task
---------
Model this system and its evolution.

You can use any language and any data structure you want.

The only requirement is that you must be able to represent
the state of the system at a given generation
and evolve it from one generation to the next.

(Notably, you are _not_ required to graphically represent the evolution.)
