import numpy as np
import pygame
import sys
from pygame.locals import *


def AI_takes_turn():
    pass


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()



if __name__ == "__main__":
    main()