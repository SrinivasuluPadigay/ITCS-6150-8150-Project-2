"""
random_restart_hill_climbing.py
Solves N-Queens problem with Random restart without Side-way Moves
"""
import traceback

import hill_climbing_search

def random_restart_hill_climbing(n, sideways_move=False, max_sideways_moves=0):
    """
    Implements the random-restart hill-climbing algorithm to solve the N-Queens problem.

    Args:
    n (int): The size of the board (number of queens).
    sideways_move (bool): Whether to allow sideways moves or not.
    max_sideways_moves (int): The maximum number of allowed sideways moves.

    Returns:
    tuple: A tuple containing three elements:
        - restarts (int): The number of random restarts used.
        - total_steps (int): The total number of steps taken by the algorithm.
        - board (list): The final board configuration.
    """
    restarts = 0
    total_steps = 0

    while True:
        success, steps, board = hill_climbing_search.hill_climbing(n, sideways_move, max_sideways_moves)
        total_steps += steps

        if success:
            return restarts, total_steps, board

        restarts += 1

def process(n, runs):
    """
    Runs the random-restart hill-climbing algorithm for the given number of times and prints the required results.

    Args:
    n (int): The size of the board (number of queens).
    runs (int): The number of times to run the algorithm.
    """
    total_restarts_without_sideways = 0
    total_steps_without_sideways = 0

    total_restarts_with_sideways = 0
    total_steps_with_sideways = 0

    for _ in range(runs):
        restarts, steps, _ = random_restart_hill_climbing(n)
        total_restarts_without_sideways += restarts
        total_steps_without_sideways += steps

        restarts, steps, _ = random_restart_hill_climbing(n, sideways_move=True, max_sideways_moves=100)
        total_restarts_with_sideways += restarts
        total_steps_with_sideways += steps

    avg_restarts_without_sideways = total_restarts_without_sideways / runs
    avg_steps_without_sideways = total_steps_without_sideways / runs

    avg_restarts_with_sideways = total_restarts_with_sideways / runs
    avg_steps_with_sideways = total_steps_with_sideways / runs

    print(f"Random-Restart Hill-Climbing for (n={n}):")
    print(f"Average number of random restarts required without sideways move: {round(avg_restarts_without_sideways,2)}")
    print(f"Average number of steps required without sideways move: {round(avg_steps_without_sideways,2)}")
    print(f"Average number of random restarts used with sideways move: {round(avg_restarts_with_sideways,2)}")
    print(f"Average number of steps required with sideways move: {round(avg_steps_with_sideways,2)}")
    print()
