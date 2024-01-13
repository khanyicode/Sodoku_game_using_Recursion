import tkinter as tk

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - -")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def find_empty_recursive(board, row, col):
    if row == len(board):
        return None  # Reached the end of the board, no empty cell found

    if col == len(board[row]):
        return find_empty_recursive(board, row + 1, 0)  # Moves to the next row

    if board[row][col] == 0:
        return row, col  # Found an empty cell

    return find_empty_recursive(board, row, col + 1)  # Move to the next column

def is_valid(board, number, position):
    # Check the row
    if number in board[position[0]]:
        return False

    # Check the column
    for i in range(len(board)):
        if board[i][position[1]] == number:
            return False

    return True

def is_subbox_valid(board, start_row, start_col):
    # This set keeps track of numbers in the subbox
    seen_numbers = set()

    # Iterates through the subbox
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            current_number = board[i][j]

            # Checks if the number is in the set
            if current_number in seen_numbers:
                return False
            elif current_number != 0:
                seen_numbers.add(current_number)  # Add the number to the set

    return True

def solve_sudoku(board):
    empty = find_empty_recursive(board, 0, 0)

    if not empty:
        return True  # No empty cells left, puzzle is solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If a solution is found, stop searching

            board[row][col] = 0  # If no solution found, backtrack

    return False  # No valid number found for this cell

def recursive_call():
    pass

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        self.canvas = tk.Canvas(self.master, width=450, height=450)
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        for i in range(9):
            for j in range(9):
                x0, y0 = j * 50, i * 50
                x1, y1 = x0 + 50, y0 + 50

                self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

                if board[i][j] != 0:
                    self.canvas.create_text(x0 + 25, y0 + 25, text=str(board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()

    

    
      
            
            