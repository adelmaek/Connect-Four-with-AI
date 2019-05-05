import pygame
from boardGui import create_board_matrix
from boardGui import draw_board
from boardGui import create_Display
from PLAYER_turn import PLAYER_takes_turn
from AI_turn import AI_takes_turn
from define import *


def main():
    board = create_board_matrix(no_rows,no_cols)
    boardBackGround = create_Display(no_rows,no_cols)
    pygame.init()
    draw_board(boardBackGround, board)

    while True:
        print(board)
        board, winner_flag= PLAYER_takes_turn(board,boardBackGround)
        if winner_flag == 1:
            print("PLAYER IS THE WINNER")
            break
        board, winner_flag = AI_takes_turn(board,boardBackGround)
        if winner_flag == 1:
            print("AI IS THE WINNER")
            break





if __name__ == "__main__":
    main()