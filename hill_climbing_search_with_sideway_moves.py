"""
hill_climbing_search_with_sideway_moves.py
Solves N-Queens problem with Side-way Moves and without Random restart
"""

import hill_climbing_search

def process(n_val, runs):
    """
        Runs the hill-climbing algorithm for the given number of times and prints the required results.

        Args:
        n (int): The size of the board (number of queens).
        runs (int): The number of times to run the algorithm.
    """
    successes = 0
    total_steps_on_success = 0
    total_steps_on_failure = 0

    for _ in range(runs):
        success, steps, _ = hill_climbing_search.hill_climbing(n_val, sideways_move=True, max_sideways_moves=100)
        if success:
            successes += 1
            total_steps_on_success += steps
        else:
            total_steps_on_failure += steps

    success_rate = (successes / runs) * 100
    failure_rate = 100 - success_rate

    average_steps_on_success = total_steps_on_success / successes if successes > 0 else 0
    average_steps_on_failure = total_steps_on_failure / (runs - successes) if runs - successes > 0 else 0

    print(f"Hill-Climbing with Side-way Move for (n={n_val}):")
    print(f"Success Rate: {round(success_rate,2)}%")
    print(f"Failure Rate: {round(failure_rate,2)}%")
    print(f"Average Steps on Success: {round(average_steps_on_success,2)}")
    print(f"Average Steps on Failure: {round(average_steps_on_failure,2)}")

    # Show the search sequences from four random initial configurations
    for _ in range(4):
        _, _, board = hill_climbing_search.hill_climbing(n_val, sideways_move=True, max_sideways_moves=100)
        print("Search Sequence:", board)
    print()