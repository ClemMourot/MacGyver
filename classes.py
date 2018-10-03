import pygame
from constants import *

pygame.init()

class Maze:
    def __init__(self):
        self.struct = []

    def get_maze(self):
        with open("maze.txt", "r") as file:
            struct = []
            for line in file:
                line_maze = []
                for sprite in line:
                    if sprite != '\n':
                        line_maze.append(sprite)
                struct.append(line_maze)
                self.struct = struct

    def display_maze(self, window):
        wall = pygame.image.load("ressource\wall.png").convert()
        framing = pygame.image.load("ressource\grill.jpg").convert()
        start = pygame.image.load("ressource\start.jpg").convert()
        end = pygame.image.load("ressource\end.jpg").convert()
        floor = pygame.image.load("ressource\\floor.jpg").convert()
        line_number = 0
        for line in self.struct:
            sprite_number = 0
            for sprite in line:
                x = sprite_number * sprite_size
                y = line_number * sprite_size
                if sprite == '-':
                    window.blit(wall, (x, y))
                if sprite == '+':
                    window.blit(framing, (x, y))
                if sprite == 's':
                    window.blit(start, (x, y))
                if sprite == 'e':
                    window.blit(end, (x, y))
                if sprite == ' ':
                    window.blit(floor, (x, y))
                sprite_number += 1
            line_number += 1




class Character:
    def __init__(self, pic = "", x = 0, y = 0, sprite_x = 0, sprite_y = 0):
        self.state = 1
        self.pic = pic
        self.x = x
        self.sprite_x = sprite_x
        self.y = y
        self.sprite_y = sprite_y

    def display_character(self, window):
        if self.state:
            character = pygame.image.load(self.pic).convert()
            window.blit(character, (self.x, self.y))

    def move(self, way, maze):
        self.sprite_x = self.x // sprite_size
        self.sprite_y = self.y // sprite_size
        if way == "r":
            if self.x < size_side:
                    if maze.struct[self.sprite_y][self.sprite_x + 1] != "-":
                        self.x += sprite_size

        elif way == "l":
            if self.x > x_start:
                    if maze.struct[self.sprite_y][self.sprite_x - 1] != "-":
                        self.x -= sprite_size

        elif way == "u":
            if self.y > y_start:
                    if maze.struct[self.sprite_y - 1][self.sprite_x] != "-":
                        self.y -= sprite_size

        elif way == "d":
            if self.y < size_side:
                    if maze.struct[self.sprite_y + 1][self.sprite_x] != "-":
                        self.y += sprite_size



class Object:
    def __init__(self, name, state):
        self.name = name
        self.state = state



