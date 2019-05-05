import random
import pygame
import sys
from pygame.locals import *
from boardGui import insert_piece
from define import *

def AI_takes_turn(board,boardBackGround):
    col = random.randint(0, 6)
    isnertionFlag = 0
    while isnertionFlag ==0:
       board, isnertionFlag =  insert_piece(board,col,AI_PIECE, boardBackGround)
    return board


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()