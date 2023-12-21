board =[[5 ,3, 0, 0, 7, 0,0, 0, 0],
        [6, 0, 0, 1, 9, 5,0, 0, 0],
        [0, 9 ,8 ,0, 0, 0,0 ,6 ,0],
        [8, 0 ,0, 0, 6, 0,0, 0 ,3],
        [4 ,0, 0 ,8 ,0, 3,0 ,0 ,1],
        [7 ,0, 0 ,0 ,2, 0,0, 0 ,6],
        [0, 6, 0, 0, 0, 0,2 ,8 ,0],
        [0, 0, 0, 4 ,1, 9,0 ,0 ,5],
        [0 ,0, 0 ,0 ,8 ,0,0 ,7, 9]] 

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - -")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()
        
print_board(board)
            
            
def find_empty_recursive(board, row, col):
    if row == len(board):
        return None  # Reached the end of the board, no empty cell found

    if col == len(board[row]):
        return find_empty_recursive(board, row + 1,0)  # Moves to the next row

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
    # This set  keeps track of numbers in the subbox
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

def recursive_call():
 pass

    

    
      
            
            