import numpy as np
import pygame
import sys
from pygame.locals import *
from define import *
def initialWindow():
    pass
def board_is_full(board):
    for c in range(no_cols):
        for r in range(no_rows):
            if board[r][c] == 0:
                return False
    return True

def is_Winning_situation(board,pieceColor):
    # horizontal
    for c in range(no_cols - 3):
        for r in range(no_rows):
            if board[r][c] == pieceColor and board[r][c + 1] == pieceColor and board[r][c + 2] == pieceColor and board[r][
                        c + 3] == pieceColor:
                return True

    #  vertical
    for c in range(no_cols):
        for r in range(no_rows - 3):
            if board[r][c] == pieceColor and board[r + 1][c] == pieceColor and board[r + 2][c] == pieceColor and board[r + 3][
                c] == pieceColor:
                return True

    # diagonal positive
    for c in range(no_cols - 3):
        for r in range(no_rows - 3):
            if board[r][c] == pieceColor and board[r + 1][c + 1] == pieceColor and board[r + 2][c + 2] == pieceColor and board[r + 3][
                        c + 3] == pieceColor:
                return True

    # diagonal negative
    for c in range(no_cols - 3):
        for r in range(3, no_rows):
            if board[r][c] == pieceColor and board[r - 1][c + 1] == pieceColor and board[r - 2][c + 2] == pieceColor and board[r - 3][
                        c + 3] == pieceColor:
                return True


def create_Display(no_rows,no_cols):
    display = pygame.display.set_mode((no_cols * SquareLength, (no_rows + 1) * SquareLength))
    return display

def create_board_matrix(no_rows,no_cols):
    return np.zeros((no_rows,no_cols),dtype= np.int8)


def insert_piece(board, col, pieceColor,boardBackground):
    no_rows, no_cols  = board.shape
    inserted_flag = 0
    for i in range(no_rows-1,-1,-1):
        if board[i,col] == 0:
            board[i,col] = pieceColor
            inserted_flag = 1
            break
        else:
            continue
    draw_board(boardBackground,board)

    return board, inserted_flag


def draw_board(boardBackground, board):
    no_rows, no_cols = board.shape
    boardBackground.fill(BACKGROUND_COLOR)
    for i in range(no_rows):
        for j in range(no_cols):
            pygame.draw.rect(boardBackground,BLUE,(j*SquareLength,i*SquareLength + SquareLength, SquareLength,SquareLength))
            if board[i,j] == 0:
                pygame.draw.circle(boardBackground, BACKGROUND_COLOR,(
                    int(j*SquareLength + SquareLength / 2),int(i*SquareLength + SquareLength + SquareLength / 2)),
                                   PieceRadius)
            elif board[i,j] == 1:
                pygame.draw.circle(boardBackground, RED, (
                int(j * SquareLength + SquareLength / 2), int(i * SquareLength + SquareLength + SquareLength / 2)),
                                   PieceRadius)
            elif board[i,j] == 2:
                pygame.draw.circle(boardBackground, YELLOW, (
                int(j * SquareLength + SquareLength / 2), int(i * SquareLength + SquareLength + SquareLength / 2)),
                                   PieceRadius)
            else:
                print("Error: unresolved board vlaue")
    pygame.display.update()



def main():
    board = create_board_matrix(6,7)

    pygame.init()

    draw_board(board)

    board, inserted = insert_piece(board, 0, 2)
    board, inserted = insert_piece(board, 0, 1)
    board, inserted = insert_piece(board, 0, 1)
    board, inserted = insert_piece(board, 0, 1)
    board, inserted = insert_piece(board, 0, 1)
    board, inserted = insert_piece(board, 0, 2)
    board, inserted = insert_piece(board, 1, 1)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()