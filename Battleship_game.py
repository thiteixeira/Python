#!/usr/bin/env python


from random import randint


def print_board(board):
    for row in board:
        print (" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def play_game():
    board = []
    board_size = 5
    for x in range(0, board_size):
        board.append(["O"] * board_size)

    print('The board is of size {}'.format(board_size))

    ship_row = random_row(board)
    ship_col = random_col(board)

    chances = 5
    print('You will have {} turns to guess the position of the ship'.format(chances))

    for turn in range(chances):
        print("Turn {}".format(turn + 1))
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game Over")
            print_board(board)

print('Welcome to Battlefield!')
play_game()
