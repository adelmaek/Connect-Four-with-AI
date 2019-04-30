import pygame
from boardGui import create_board_matrix
from boardGui import draw_board
from boardGui import create_Display
import sys
from pygame.locals import *
from PLAYER_turn import PLAYER_takes_turn
from AI_turn import AI_takes_turn
from define import *


def main():
    board = create_board_matrix(no_rows,no_cols)
    boardBackGround = create_Display(no_rows,no_cols)
    pygame.init()
    draw_board(boardBackGround, board)

    while True:
        board = PLAYER_takes_turn(board,boardBackGround)

        # board = AI_takes_turn(board)





if __name__ == "__main__":
    main()