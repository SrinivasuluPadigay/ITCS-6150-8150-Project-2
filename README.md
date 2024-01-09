ITCS 6150/8150 - Intelligent Systems
Programming Project 1 - Solving N-queens problem using hill-climbing search and its variants

# N-Queens Solver

This project solves the N-Queens problem using hill-climbing search and its variants, such as hill-climbing search with sideways moves and random-restart hill-climbing.

Programming Language: Python 3.6 or later (For installing use this link https://www.python.org/downloads/)
Compiler: MSC v.1934 64 bit (AMD64)

Submitted By: Group 13

## Problem Statement

The N-Queens problem involves placing N queens on an NxN chessboard such that no two queens can attack each other. This means that no two queens should be placed in the same row, column, or diagonal.


## Files:

1. `main.py`: This is the main file that orchestrates the solving of the N-Queens based on user input. It handles input validation.

2. `hill_climbing_search.py`: Solves N-Queens problem without Side-way Moves (or) Random restart

3. `hill_climbing_search_with_sideway_moves.py`: Solves N-Queens problem with Side-way Moves and without Random restart

4. `random_restart_hill_climbing.py`: Solves N-Queens problem with Random restart without Side-way Moves

## How to use:

1. Run `main.py`.
   
2. You'll be prompted to enter the 'N' value of N-Queens problem (or) press enter to select N=8

2. Next, input the variant of hill-climbing you want to run 
    - Input `1` for hill climbing without side-way move function.
    - Input `2` for hill climbing with side-way move function.
	- Input `3` for random restart hill climbing with and without side-way move function.

3. Finally, input `Number of times you want to repeat/run the problem` (or) press enter to select to run for 1000 times

## Output

The program will output the following statistics:

- Success and failure rates
- Average number of steps when the algorithm succeeds
- Average number of steps when the algorithm fails
- Search sequences from random initial configurations

These statistics will be reported for each of the algorithms implemented in the program.

## Dependencies:
- Python Standard Library

## Notes:

- The `Board` is represented as a list. The index of the list represents the column, and the value at each index represents the row where a queen is placed.
Example: [7, 4, 6, 0, 2, 5, 1, 3] is a Board configuration for 8X8 board 

- The number of side-way moves are limited to 100

- As N-value or Number of times you want to repeat/run the problem increases the execution time will also increase, have patience and give it some time to generate output.

- Random board generated can be duplicates. 

## Troubleshooting:

If you encounter any errors or invalid inputs, the program will provide an appropriate message and prompt you to try again.