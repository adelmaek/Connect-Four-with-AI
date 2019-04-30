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


def insert_piece(board, col, piece):
    no_rows, no_cols  = board.shape
    inserted_flag = 0
    for i in range(no_rows-1,0,-1):
        if board[i,col] == 0:
            board[i,col] = piece
            inserted_flag = 1
            break
        else:
            continue
    draw_board(board)
    return board, inserted_flag


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
    pygame.display.update()
def main():
    board = create_board_matrix(6,7)
    pygame.init()
    draw_board(board)
    board, inserted = insert_piece(board,0,2)
    print(board, inserted)
    insert_piece(board,1,1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()