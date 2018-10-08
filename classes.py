import pygame
from constants import *
import random


class Game:

    def __init__(self):
        self.maze = Maze()
        self.mac_gyver = Character()
        self.guardian = Character()
        self.ether = Object()
        self.needle = Object()
        self.syringe = Object()
        self.window = pygame.display.set_mode((side_size, side_size))

    def initialize_window(self):
        pygame.display.set_caption(title)
        background = pygame.image.load(pic_background).convert_alpha()
        text_font = pygame.font.Font(None, 20)
        i = 0
        for msg in rules:
            rules_text = text_font.render(msg, 1, (10, 10, 10))
            background.blit(rules_text, (20, 520 + i))
            i += 30
        i = 0
        for msg in objects:
            object_text = text_font.render(msg, 1, (10, 10, 10))
            background.blit(object_text, (510, 30 * i))
            i += 2
        self.window.blit(background, (0, 0))

    def initialize_game(self):
        self.maze.get_maze()

        self.mac_gyver.pic = pic_mac_gyver
        self.mac_gyver.x = x_start
        self.mac_gyver.y = y_start

        self.guardian.pic = pic_guardian
        self.guardian.x = x_end
        self.guardian.y = y_end

        self.ether.name = "ether"
        self.ether.pic = pic_ether
        self.ether.generate_object(self.maze, "et")

        self.needle.name = "needle"
        self.needle.pic = pic_needle
        self.needle.generate_object(self.maze, "ne")

        self.syringe.name = "syringe"
        self.syringe.pic = pic_syringe
        self.syringe.generate_object(self.maze, "sy")

    def game_display(self):

        self.maze.display_maze(self.window)
        self.guardian.display_character(self.window)
        self.ether.display_object(self.window)
        self.needle.display_object(self.window)
        self.syringe.display_object(self.window)
        self.mac_gyver.display_character(self.window)

        count = str(self.mac_gyver.object_count)
        text_font = pygame.font.Font(None, 20)
        object_count = text_font.render(count, 1, (10, 10, 10))
        count_window = pygame.image.load(pic_count_window).convert()
        count_window.blit(object_count, (10, 10))
        self.window.blit(count_window, (520, 20))

    def game_loop(self):

        if self.maze.structure[self.mac_gyver.y // sprite_size][self.mac_gyver.x // sprite_size] == "et":
            self.ether.state = 0
            self.maze.structure[self.mac_gyver.y // sprite_size][self.mac_gyver.x // sprite_size] = " "
            self.mac_gyver.object_count += 1
            self.ether.display_dashboard(self.window, self.mac_gyver.object_count)

        if self.maze.structure[self.mac_gyver.y // sprite_size][self.mac_gyver.x // sprite_size] == "ne":
            self.needle.state = 0
            self.maze.structure[self.mac_gyver.y // sprite_size][self.mac_gyver.x // sprite_size] = " "
            self.mac_gyver.object_count += 1
            self.needle.display_dashboard(self.window, self.mac_gyver.object_count)

        if self.maze.structure[self.mac_gyver.y // sprite_size][self.mac_gyver.x // sprite_size] == "sy":
            self.syringe.state = 0
            self.maze.structure[self.mac_gyver.y // sprite_size][self.mac_gyver.x // sprite_size] = " "
            self.mac_gyver.object_count += 1
            self.syringe.display_dashboard(self.window, self.mac_gyver.object_count)

        if self.mac_gyver.x == x_end and self.mac_gyver.y == y_end and self.mac_gyver.object_count == 3:
            won = True
            while won:
                pygame.display.flip()
                pygame.display.set_caption(title)
                self.window = pygame.display.set_mode((510, 510))
                victory = pygame.image.load(pic_victory).convert()
                text_font = pygame.font.Font(None, 36)
                text = text_font.render(victory_text, 1, (10, 10, 10))
                victory.blit(text, (50, 100))
                self.window.blit(victory, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return 1
                        elif event.key == pygame.K_ESCAPE:
                            return 0

        if self.mac_gyver.x == x_end and self.mac_gyver.y == y_end and self.mac_gyver.object_count < 3:
            lost = True
            while lost:
                pygame.display.flip()
                pygame.display.set_caption(title)
                self.window = pygame.display.set_mode((510, 510))
                loss = pygame.image.load(pic_loss).convert()
                text_font = pygame.font.Font(None, 36)
                text = text_font.render(loss_text, 1, (10, 10, 10))
                loss.blit(text, (120, 100))
                self.window.blit(loss, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return 1
                        elif event.key == pygame.K_ESCAPE:
                            return 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
                if event.key == pygame.K_RIGHT:
                    self.mac_gyver.move("r", self.maze)
                if event.key == pygame.K_LEFT:
                    self.mac_gyver.move("l", self.maze)
                if event.key == pygame.K_UP:
                    self.mac_gyver.move("u", self.maze)
                if event.key == pygame.K_DOWN:
                    self.mac_gyver.move("d", self.maze)


class Maze:
    def __init__(self):
        self.structure = []

    def get_maze(self):
        with open("maze.txt", "r") as file:
            structure = []
            for line in file:
                line_maze = []
                for sprite in line:
                    if sprite != '\n':
                        line_maze.append(sprite)
                structure.append(line_maze)
                self.structure = structure

    def display_maze(self, window):
        wall = pygame.image.load(pic_wall).convert()
        framing = pygame.image.load(pic_grill).convert()
        start = pygame.image.load(pic_start).convert()
        end = pygame.image.load(pic_end).convert()
        floor = pygame.image.load(pic_floor).convert()
        line_number = 0
        for line in self.structure:
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
    def __init__(self, pic="", x=0, y=0, sprite_x=0, sprite_y=0):
        self.state = 1
        self.pic = pic
        self.x = x
        self.sprite_x = sprite_x
        self.y = y
        self.sprite_y = sprite_y
        self.object_count = 0

    def display_character(self, window):
        if self.state:
            character = pygame.image.load(self.pic).convert()
            window.blit(character, (self.x, self.y))

    def move(self, way, maze):
        self.sprite_x = self.x // sprite_size
        self.sprite_y = self.y // sprite_size
        if way == "r":
            if self.x < playground_size:
                    if maze.structure[self.sprite_y][self.sprite_x + 1] != "-":
                        self.x += sprite_size

        elif way == "l":
            if self.x > x_start:
                    if maze.structure[self.sprite_y][self.sprite_x - 1] != "-":
                        self.x -= sprite_size

        elif way == "u":
            if self.y > y_start:
                    if maze.structure[self.sprite_y - 1][self.sprite_x] != "-":
                        self.y -= sprite_size

        elif way == "d":
            if self.y < playground_size:
                    if maze.structure[self.sprite_y + 1][self.sprite_x] != "-":
                        self.y += sprite_size


class Object:
    def __init__(self, name=" ", pic=0):
        self.name = name
        self.state = 1
        self.x = 0
        self.y = 0
        self.pic = pic

    def generate_object(self, maze, letter=" "):
        searching = True
        while searching:
            self.x = random.randrange(0, 510, 30)
            self.y = random.randrange(0, 510, 30)
            sprite_x = self.x // sprite_size
            sprite_y = self.y // sprite_size
            if maze.structure[sprite_y][sprite_x] != '-' and maze.structure[sprite_y][sprite_x] != '+' \
                    and maze.structure[sprite_y][sprite_x] != 'o' and self.x != x_start \
                    and self.x != x_end and self.y != y_start and self.y != y_end:
                maze.structure[sprite_y][sprite_x] = letter
                searching = False

    def display_object(self, window):
        if self.state:
            thing = pygame.image.load(self.pic).convert()
            window.blit(thing, (self.x, self.y))

    def display_dashboard(self, window, object_count):
        if self.state == 0:
            thing = pygame.image.load(self.pic).convert()
            window.blit(thing, (dashboard_start, sprite_size*2*object_count+x_start))
