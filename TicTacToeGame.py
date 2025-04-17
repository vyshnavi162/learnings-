def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False


def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    
    for _ in range(9):
        display_board(board)
        move = int(input(f"Player {current_player}, enter your move (0-8): "))
        
        while board[move] != ' ' or move < 0 or move > 8:
            move = int(input("Invalid move. Try again: "))
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    display_board(board)
    print("It's a tie!")


if __name__ == "__main__":
    tic_tac_toe()