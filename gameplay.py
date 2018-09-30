import classes
import pygame
from pygame.locals import *


def main():
    pygame.init()
    pygame.display.set_caption("Mac Gyver game")
    window = pygame.display.set_mode((510, 510))
    maze = classes.Maze()
    maze.get_maze()
    mac_gyver = classes.Character()
    mac_gyver.pic = "ressource\mac_gyver.png"

    guardian = classes.Character()
    guardian.pic = "ressource\guardian.png"

    playing = True
    maze.display_maze(window)
    mac_gyver.display_character(window)
    guardian.display_character(window)
    pygame.display.flip()

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                playing = False


main()