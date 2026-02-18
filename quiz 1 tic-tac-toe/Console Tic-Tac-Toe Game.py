# Console Tic-Tac-Toe with winning line

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return pos  # return the winning positions
    return None

def highlight_winner(board, pos):
    # replace winning cells with '*' for visibility
    for i in pos:
        board[i] = '*' + board[i] + '*'

def tic_tac_toe():
    board = [" "]*9
    player = "X"
    moves = 0
    print("Welcome to Tic-Tac-Toe!")
    print("Choose a box number from 1 to 9 like this:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
    
    while moves < 9:
        print_board(board)
        try:
            move = int(input(f"Player {player}, choose a box (1-9): "))
            if move < 1 or move > 9:
                print("Invalid box! Type a number from 1 to 9.")
                continue
            index = move - 1
            if board[index] != " ":
                print("Box already taken! Try again.")
                continue
            board[index] = player
            moves += 1
            winning_pos = check_winner(board, player)
            if winning_pos:
                highlight_winner(board, winning_pos)
                print_board(board)
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Invalid input! Type a number from 1 to 9.")
    print_board(board)
    print("It's a tie!")

# Start the game
tic_tac_toe()