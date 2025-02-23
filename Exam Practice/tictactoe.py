import math


# Print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# Check if the current player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Minimax with Alpha-Beta Pruning
def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if all(cell != ' ' for row in board for cell in row):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best_score


# Function to get the best move for the AI (Max player)
def get_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = alpha_beta_pruning(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


# Function to handle the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Cell already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please choose a number between 1 and 9.")


# Main game loop
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        player_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("You win!")
            break
        if all(cell != ' ' for row in board for cell in row):
            print("It's a draw!")
            break

        # AI's turn
        print("AI is making a move...")
        best_move = get_best_move(board)
        if best_move:
            board[best_move[0]][best_move[1]] = 'X'
            print_board(board)
            if check_winner(board, 'X'):
                print("AI wins!")
                break
            if all(cell != ' ' for row in board for cell in row):
                print("It's a draw!")
                break


# Start the game
tic_tac_toe()
