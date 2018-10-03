import classes
import pygame
from pygame import *
from constants import *


def main():
    pygame.init()
    pygame.display.set_caption("Mac Gyver game")
    window = pygame.display.set_mode((510, 510))
    maze = classes.Maze()
    maze.get_maze()
    mac_gyver = classes.Character()
    mac_gyver.pic = "ressource\mac_gyver.png"
    mac_gyver.x = x_start
    mac_gyver.y = y_start

    guardian = classes.Character()
    guardian.pic = "ressource\guardian.png"
    guardian.x = x_end
    guardian.y = y_end

    playing = True


    while playing:
        maze.display_maze(window)
        mac_gyver.display_character(window)
        guardian.display_character(window)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    playing = False
                if event.key == K_RIGHT:
                    mac_gyver.move("r", maze)
                if event.key == K_LEFT:
                    mac_gyver.move("l", maze)
                if event.key == K_UP:
                    mac_gyver.move("u", maze)
                if event.key == K_DOWN:
                    mac_gyver.move("d", maze)




main()