import random
import pygame
import sys
from pygame.locals import *
from boardGui import insert_piece, is_Winning_situation
from define import *

def AI_takes_turn(board,boardBackGround):
    col = random.randint(0, 6)
    winner_flag = 0
    isnertionFlag = 0
    while isnertionFlag ==0:
       board, isnertionFlag =  insert_piece(board,col,AI_PIECE, boardBackGround)
       if is_Winning_situation(board, AI_PIECE):
           winner_flag = 1
    return board, winner_flag


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()