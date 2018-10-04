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
    mac_gyver.pic = "resources\mac_gyver.png"
    mac_gyver.x = x_start
    mac_gyver.y = y_start

    guardian = classes.Character()
    guardian.pic = "resources\guardian.png"
    guardian.x = x_end
    guardian.y = y_end

    ether = classes.Object()
    ether.name = "ether"
    ether.pic = "resources\ether.png"
    ether.generate_object(maze)

    needle = classes.Object()
    needle.name = "needle"
    needle.pic = "resources\eedle.png"
    needle.generate_object(maze)

    syringe = classes.Object()
    syringe.name = "syringe"
    syringe.pic = "resources\syringe.png"
    syringe.generate_object(maze)

    playing = True

    while playing:
        maze.display_maze(window)
        mac_gyver.display_character(window)
        guardian.display_character(window)
        ether.display_object(window)
        needle.display_object(window)
        syringe.display_object(window)
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
