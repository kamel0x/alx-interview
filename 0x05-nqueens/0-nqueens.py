#!/usr/bin/python3
""" Solve n queen problem """
import sys


argv = sys.argv


def is_safe(board, row, col, n):
    """ check if a box is safe """

    # Check if no queens are in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def n_queens_backtrack(board, row, n, solutions):
    """ solve the end queen with backtracking """
    if row == n:
        solution = []
        for r, ro in enumerate(board):
            for c, col in enumerate(ro):
                if col == 1:
                    solution.append([r, c])
        solutions.append(solution)

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            n_queens_backtrack(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def printer(solutions):
    """ print the solution """
    for solution in solutions:
        print(solution)


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    n_queens_backtrack(board, 0, n, solutions)
    printer(solutions)


def main(argv):
    """ main function """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    num = argv[1]
    try:
        num = int(num)
    except ValueError:
        print("N must be a number")
        exit(1)

    if num < 4:
        print("N must be at least 4")
        exit(1)
    solve_n_queens(num)


if __name__ == '__main__':
    main(argv)
