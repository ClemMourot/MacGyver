import pygame
from pygame.locals import *

class Location:
    pass


class Maze:

    def __init(self):
        pass

    def get_maze(self):
        with open("maze.txt", r) as file:
            struct = []
            for lign in file:
                lign_maze = []
                for sprite in lign:
                    if sprite != '\n':
                        lign_maze.append(sprite)
                struct.append(lign_maze)

    def display_maze(self):
        wall = pygame.image.load()

class Character:
    def __init__(self, name, state):
        self.name = name
        self.state = state

class Object:
    def __init__(self, name, state):
        self.name = name
        self.state = state


