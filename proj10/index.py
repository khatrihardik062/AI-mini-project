
import math


def printb(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")


def checkwin(board):
    wincon = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for con in wincon:
        if (board[con[0]] == board[con[1]] ==
                board[con[2]] and board[con[0]] in ["X", "O"]):
            return board[con[0]]

    if all(spot in ["X", "O"] for spot in board):
        return "Tie"

    return None


def minimax(board, depth, ismax):
    result = checkwin(board)

    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Tie":
        return 0

    if ismax:
        bestscore = -math.inf

        for i in range(9):
            if board[i] not in ["X", "O"]:
                saved = board[i]
                board[i] = "O"

                score = minimax(board, depth + 1, False)

                board[i] = saved
                bestscore = max(score, bestscore)

        return bestscore

    else:
        bestscore = math.inf

        for i in range(9):
            if board[i] not in ["X", "O"]:
                saved = board[i]
                board[i] = "X"

                score = minimax(board, depth + 1, True)

                board[i] = saved
                bestscore = min(score, bestscore)

        return bestscore


def getaimove(board):
    bestscore = -math.inf
    bestmove = None

    for i in range(9):
        if board[i] not in ["X", "O"]:
            saved = board[i]
            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = saved

            if score > bestscore:
                bestscore = score
                bestmove = i

    return bestmove


def ttt():
    board = [str(i) for i in range(1, 10)]

    print("Welcome to TIC TAC TOE vs Unbeatable AI")
    print("You are X (goes first). AI is O.")

    while True:
        printb(board)

        winner = checkwin(board)

        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"Player {winner} won!")
            break

        while True:
            try:
                move = int(input("Your turn, choose a spot (1-9): ")) - 1

                if 0 <= move <= 8 and board[move] not in ["X", "O"]:
                    board[move] = "X"
                    break

                print("Invalid move. Try again.")

            except ValueError:
                print("Please enter a number between 1 and 9.")

        if checkwin(board):
            continue

        print("AI is thinking...")

        aimove = getaimove(board)

        if aimove is not None:
            board[aimove] = "O"


if __name__ == "__main__":
    ttt()
