import numpy as np
import pygame
import sys
from pygame.locals import *

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
SquareLength = 100

def create_board_matrix(no_rows,no_cols):
    return np.zeros((no_rows,no_cols),dtype= np.int8)


def draw_board(board):
    no_rows, no_cols = board.shape
    boardBackground = pygame.display.set_mode((no_cols * SquareLength, (no_rows + 1)  * SquareLength  ))
    boardBackground.fill(WHITE)
    for i in range(no_rows):
        for j in range(no_cols):
            pygame.draw.rect(boardBackground,BLUE,(j*SquareLength,i*SquareLength + SquareLength, SquareLength,SquareLength))
            if board[i,j] == 0:
                pygame.draw.circle(boardBackground, WHITE,(
                    int(j*SquareLength + SquareLength / 2),int(i*SquareLength + SquareLength + SquareLength / 2)),
                                   int(SquareLength/2 - 4))
            elif board[i,j] == 1:
                pygame.draw.circle(boardBackground, RED, (
                int(j * SquareLength + SquareLength / 2), int(i * SquareLength + SquareLength + SquareLength / 2)),
                                   int(SquareLength / 2 - 4))
            elif board[i,j] == 2:
                pygame.draw.circle(boardBackground, YELLOW, (
                int(j * SquareLength + SquareLength / 2), int(i * SquareLength + SquareLength + SquareLength / 2)),
                                   int(SquareLength / 2 - 4))
            else:
                print("Error: unresolved board vlaue")

def main():
    board = create_board_matrix(6,7)
    pygame.init()
    draw_board(board)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()