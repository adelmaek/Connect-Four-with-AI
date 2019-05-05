from boardGui import insert_piece, is_Winning_situation
import pygame
import sys
from pygame.locals import *
from define import *
import math


def PLAYER_takes_turn(board,boardBackground):
    winner_flag = 0
    insertedFlag = 0
    while insertedFlag ==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(boardBackground,WHITE,(0,0,SquareLength*no_cols,SquareLength))
                col_pos = event.pos[0]
                pygame.draw.circle(boardBackground,YELLOW,(col_pos,int(SquareLength/2)),PieceRadius)
                pygame.display.update()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(boardBackground, WHITE, (0, 0, SquareLength*no_cols, SquareLength))
                clickPosition = event.pos[0]
                insertionCol = int(math.floor(clickPosition / SquareLength))
                board,insertedFlag= insert_piece(board, insertionCol, PLAYER_PIECE,boardBackground)

    if is_Winning_situation(board,PLAYER_PIECE):
        print("PLAYER IS WINNER")
        winner_flag = 1
    return board, winner_flag





def main():

    pass



if __name__ == "__main__":
    main()