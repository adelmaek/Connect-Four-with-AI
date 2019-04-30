import numpy as np
import pygame
import sys
from pygame.locals import *
from define import *


def PLAYER_takes_turn(board,backGround):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(backGround,WHITE,(0,0,SquareLength*no_cols,SquareLength))
            col_pos = event.pos[0]
            pygame.draw.circle(backGround,YELLOW,(col_pos,int(SquareLength/2)),PieceRadius)
            pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            pass





def main():

    pass



if __name__ == "__main__":
    main()