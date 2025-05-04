#!/usr/bin/env python
# coding: utf-8

# In[9]:


def print_board(board, tried_row=None, tried_col=None, unsafe=False):
    for i in range(len(board)):
        row = ""
        for j in range(len(board)):
            if board[i][j] == 1:
                row += "Q "
            elif unsafe and i == tried_row and j == tried_col:
                row += "- "
            else:
                row += ". "
        print(row)
    print("-" * 20)

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_bt(board, row):
    if row == len(board):
        print("Solution found by Backtracking:")
        print_board(board)
        return True

    for col in range(len(board)):
        print(f"Trying to place Queen at ({row}, {col})")
        if is_safe(board, row, col):
            board[row][col] = 1
            print_board(board)
            if solve_n_queens_bt(board, row + 1):
                return True
            board[row][col] = 0
            print(f"Backtracking from ({row}, {col})")
        else:
            print(f" Unsafe to place at ({row}, {col})")
            print_board(board, row, col, unsafe=True)
    return False

def branch_and_bound_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    row_lookup = [False] * N
    slash_code_lookup = [False] * (2 * N - 1)
    backslash_code_lookup = [False] * (2 * N - 1)

    slash_code = [[r + c for c in range(N)] for r in range(N)]
    backslash_code = [[r - c + N - 1 for c in range(N)] for r in range(N)]

    def solve(col):
        if col >= N:
            print("Solution found by Branch and Bound:")
            print_board(board)
            return True
        for row in range(N):
            print(f"Trying to place Queen at ({row}, {col})")
            if not row_lookup[row] and not slash_code_lookup[slash_code[row][col]] and not backslash_code_lookup[backslash_code[row][col]]:
                board[row][col] = 1
                row_lookup[row] = True
                slash_code_lookup[slash_code[row][col]] = True
                backslash_code_lookup[backslash_code[row][col]] = True
                print_board(board)
                if solve(col + 1):
                    return True
                board[row][col] = 0
                row_lookup[row] = False
                slash_code_lookup[slash_code[row][col]] = False
                backslash_code_lookup[backslash_code[row][col]] = False
                print(f"Backtracking from ({row}, {col})")
            else:
                print(f"Unsafe to place at ({row}, {col})")
                print_board(board, row, col, unsafe=True)
        return False

    solve(0)

# ============ MAIN ============
try:
    N = int(input("Enter the value of N for N-Queens: "))
    if N < 1:
        print("N must be at least 1.")
    else:
        print("\n=== Backtracking N-Queens ===")
        bt_board = [[0 for _ in range(N)] for _ in range(N)]
        solve_n_queens_bt(bt_board, 0)

        print("\n=== Branch and Bound N-Queens ===")
        branch_and_bound_n_queens(N)
except ValueError:
    print("Please enter a valid integer.")



# In[ ]:




