"""
hill_climbing_search.py
This is the heart of the N-Queens Problem
Solves N-Queens problem without Side-way Moves (or) Random restart
"""
import random

def generate_random_integers(n):
    """
    This function generates a list of n random integers between 0 and n - 1 inclusive.
    We use these numbers to form a random board for the N-Queens problem.

    Args:
    n (int): The number of random integers to generate.
    Here it is the size of the board (number of queens)

    Returns:
    list:  A list containing n random integers between 0 and n - 1.
    This list represents the board. The index of the list represents the column,
          and the value at each index represents the row where a queen is placed.
    """
    # Initialize an empty list to store the random numbers
    random_numbers = []

    # Use a for loop to generate n random numbers
    for _ in range(n):
        # Generate a random integer between 0 and n - 1 inclusive
        random_integer = random.randint(0, n - 1)

        # Append the random integer to the list
        random_numbers.append(random_integer)

    return random_numbers

def is_solution(board):
    """
    Checks if the given board configuration is a solution to the N-Queens problem.

    Args:
    board (list): The board configuration to check.

    Returns:
    bool: True if the board is a solution, False otherwise.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if i != j:
                # Two queens can attack each other if they are in the same row, same column,
                # or if the difference between their row numbers is equal to the difference
                # between their column numbers (which means they are on the same diagonal).
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    return False
    return True

def get_neighbors(board):
    """
    Generates all possible neighbors of the current board by moving each queen to every other row in its column.

    Args:
    board (list): The current board configuration.

    Returns:
    list: A list of all possible neighbors.
    """
    neighbors = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] != j:
                neighbor = board.copy()
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors


def heuristic_function(board):
    """
    Calculates the objective function value for the board configuration. The objective function
    value is the number of pairs of queens that do not attack each other.

    Args:
    board (list): The board configuration.

    Returns:
    int: The objective function value.
    """
    non_attacking_pairs = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] != board[j] and abs(board[i] - board[j]) != abs(i - j):
                non_attacking_pairs += 1

    return non_attacking_pairs

def hill_climbing(n, sideways_move=False, max_sideways_moves=0):
    """
    Implements the hill-climbing algorithm to solve the N-Queens problem.

    Args:
    n (int): The size of the board (number of queens).
    sideways_move (bool): Whether to allow sideways moves or not.
    max_sideways_moves (int): The maximum number of allowed sideways moves.

    Returns:
    tuple: A tuple containing three elements:
        - success (bool): True if the algorithm found a solution, False otherwise.
        - steps (int): The number of steps taken by the algorithm.
        - board (list): The final board configuration.
    """
    board = generate_random_integers(n)
    steps = 0
    sideways_moves = 0

    while True:
        neighbors = get_neighbors(board)
        neighbor_values = [heuristic_function(neighbor) for neighbor in neighbors]

        best_neighbor = neighbors[neighbor_values.index(max(neighbor_values))]
        best_neighbor_value = max(neighbor_values)

        if best_neighbor_value <= heuristic_function(board):
            if sideways_move and sideways_moves < max_sideways_moves and best_neighbor_value == heuristic_function(board):
                sideways_moves += 1
            else:
                break
        else:
            sideways_moves = 0

        board = best_neighbor
        steps += 1

        if is_solution(board):
            return True, steps, board

    return False, steps, board
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
        success, steps, _ = hill_climbing(n_val)
        if success:
            successes += 1
            total_steps_on_success += steps
        else:
            total_steps_on_failure += steps

    success_rate = (successes / runs) * 100
    failure_rate = 100 - success_rate

    average_steps_on_success = total_steps_on_success / successes if successes > 0 else 0
    average_steps_on_failure = total_steps_on_failure / (runs - successes) if runs - successes > 0 else 0

    print(f"Hill-Climbing for (n={n_val}):")
    print(f"Success Rate: {round(success_rate,2)}%")
    print(f"Failure Rate: {round(failure_rate,2)}%")
    print(f"Average Steps on Success: {round(average_steps_on_success, 2)}")
    print(f"Average Steps on Failure: {round(average_steps_on_failure,2)}")

    # Show the search sequences from four random initial configurations
    for _ in range(4):
        _, _, board = hill_climbing(n_val)
        print("Search Sequence:", board)
    print()