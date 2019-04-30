import pygame
from boardGui import create_board_matrix
from boardGui import draw_board


def main():
    board = create_board_matrix()
    pygame.init()
    draw_board(board)
    pygame.display.update()


if __name__ == "__main__":
    main()