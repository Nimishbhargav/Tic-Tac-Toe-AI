import math
import sys

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_states:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != EMPTY:
            return board[condition[0]]
    if EMPTY not in board:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if winner == 'Tie':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval_score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval_score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def play_game():
    board = [EMPTY] * 9
    print("==============================================")
    print("🎮 Unbeatable Tic-Tac-Toe AI Initialized! 🎮")
    print("You are 'X' | AI is 'O'")
    print("Positions are numbered 1 to 9 (Top-Left to Bottom-Right)")
    print("==============================================")
    
    print_board([str(i+1) for i in range(9)])
    
    while True:
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in range(9) and board[move] == EMPTY:
                    board[move] = HUMAN
                    break
                print("Invalid move! Try an empty square.")
            except ValueError:
                print("Please enter a valid number.")
        
        print_board(board)
        if check_winner(board): break
            
        print("AI is calculating the best move...")
        ai_move = find_best_move(board)
        if ai_move != -1:
            board[ai_move] = AI
            
        print_board(board)
        if check_winner(board): break

    winner = check_winner(board)
    if winner == 'Tie':
        print("🤝 It's a Perfect Tie! (The best you can do against this AI)")
    elif winner == AI:
        print("🤖 AI Wins! Better luck next time.")

if __name__ == "__main__":
    play_game()
