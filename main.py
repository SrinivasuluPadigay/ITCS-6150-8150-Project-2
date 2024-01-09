"""
main.py
This is the main program of N-Queens problem
It takes interacts with the end user and takes the following input
    1. N value of N-Queens
    2. Number of times you want the N-Queens Problem
    3. Variant of N-Queens you want to run
"""
import traceback

import hill_climbing_search
import hill_climbing_search_with_sideway_moves
import random_restart_hill_climbing

def start():
    try:
        # get N-queens n-value and validate it
        print("Please enter the N value of N-queens problem (or) press enter to consider N=8")
        n_val = input("Input=")
        if not n_val:
            n_val = 8
        elif n_val.isdigit():
            n_val = int(n_val)
        else:
            raise ValueError()

        # get N-queens variant selection and validate it
        print("Select the N-Queen Variant:\n1. Hill climbing search\n2. Hill-climbing search with sideways move\n3. Random-restart hill-climbing search")
        n_queens_variant = input("Input=").strip()
        if n_queens_variant not in {'1', '2', '3'}:
            raise ValueError()

        # get the number of times we want to run the N-Queens Problem
        print("Enter the number of times you want to run (or) press enter to consider runs=1000")
        runs = input("Input=")
        if not runs:
            runs = 1000
        elif runs.isdigit():
            runs = int(runs)
        else:
            raise ValueError()

        if n_queens_variant == '1':
            hill_climbing_search.process(n_val, runs)
        elif n_queens_variant == '2':
            hill_climbing_search_with_sideway_moves.process(n_val, runs)
        else:
            random_restart_hill_climbing.process(n_val, runs)
    except ValueError:
        print("Error: Invalid input entered!\t Please try again.\n\n")
    except Exception as e:
        traceback.print_exc()

if __name__ == '__main__':
    while 1:
        start()