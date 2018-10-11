import pygame
from constants import *
import random


class Game:
    """ class Game gets together every instance needed to create the playground and its characters and objects and
    display them, as well as the game loop """

    def __init__(self):
        """ creates the objects and the window """

        self.maze = Maze()
        self.mac_gyver = Character()
        self.guardian = Character()
        self.ether = Object()
        self.needle = Object()
        self.syringe = Object()
        self.window = pygame.display.set_mode((side_size, side_size))

    def initialize_window(self):
        """ initializes the background, the rules, the base for the object count and their display
        and prints those on the window"""

        pygame.display.set_caption(title)
        background = pygame.image.load(pic_background).convert_alpha()
        text_font = pygame.font.Font(None, 20)
        i = 0   # to add space between the different lines in the message to display
        for msg in rules:   # goes through the list to get every line of the message
            rules_text = text_font.render(msg, 1, (10, 10, 10))
            background.blit(rules_text, (20, 520 + i))  # pastes the message onto the picture
            i += 30
        i = 0
        for msg in objects:
            object_text = text_font.render(msg, 1, (10, 10, 10))
            background.blit(object_text, (510, 30 * i))
            i += 2
        self.window.blit(background, (0, 0))    # pastes the picture onto the window

    def initialize_game(self):
        """ initializes the objects and loads information into their attributes for the beginning of the game """

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
        """ calls for every object their method to display themselves and creates a small zone to display the object
        count that is pasted over the already existing window"""

        self.maze.display_maze(self.window)
        self.guardian.display_character(self.window)
        self.ether.display_object(self.window)
        self.needle.display_object(self.window)
        self.syringe.display_object(self.window)
        self.mac_gyver.display_character(self.window)

        count = str(self.mac_gyver.object_count)    # translates the integer contained in object_count into a string
        text_font = pygame.font.Font(None, 20)
        object_count = text_font.render(count, 1, (10, 10, 10))
        count_window = pygame.image.load(pic_count_window).convert()
        count_window.blit(object_count, (10, 10))
        self.window.blit(count_window, (520, 20))
        # pastes the new image containing the object count over the existing background

    def game_loop(self):
        """ contains everything that makes the game loop and that could change and need display updating """

        # what needs to be done if mac_gyver encounters any of the three objects
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
            # when mac_gyver arrives over the guardian having picked up the three objects
            won = True  # to know when the victory window should be on or not
            while won:
                pygame.display.flip()   # updates the display surface to the screen
                pygame.display.set_caption(title)
                self.window = pygame.display.set_mode((510, 510))
                victory = pygame.image.load(pic_victory).convert()  # displays a victory image as a background
                text_font = pygame.font.Font(None, 36)
                text = text_font.render(victory_text, 1, (10, 10, 10))  # lets the user know what he can do now
                victory.blit(text, (50, 100))
                self.window.blit(victory, (0, 0))
                for event in pygame.event.get():    # gets any event happening
                    if event.type == pygame.KEYDOWN:    # if the user presses a key
                        if event.key == pygame.K_RETURN:    # if the user presses the return key
                            return 1    # lets the main function know it should call the game loop again
                        elif event.key == pygame.K_ESCAPE:  # if the user presses the escape key
                            return 0    # lets the main function know it should terminate the program

        if self.mac_gyver.x == x_end and self.mac_gyver.y == y_end and self.mac_gyver.object_count < 3:
            # when mac_gyver arrives over the guardian without all three objects
            lost = True # to know when the loss window should be on or not
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
                # if the user presses a directional key, Character's method "move" should be called passing
                # the key presses as a string parameter
                if event.key == pygame.K_RIGHT:
                    self.mac_gyver.move("r", self.maze)
                if event.key == pygame.K_LEFT:
                    self.mac_gyver.move("l", self.maze)
                if event.key == pygame.K_UP:
                    self.mac_gyver.move("u", self.maze)
                if event.key == pygame.K_DOWN:
                    self.mac_gyver.move("d", self.maze)


class Maze:
    """ class Maze contains everything to get the maze from the file ans then display it """

    def __init__(self):
        """ creates a list to put the maze in """

        self.structure = []    # to contain the symbols read in the file

    def get_maze(self):
        """ opens, reads the file and while going through the list, filling it with the content of the file """

        with open("maze.txt", "r") as file:    # opens the file in the reading mode
            structure = []
            for line in file:
                line_maze = []
                for sprite in line:
                    if sprite != '\n':
                        line_maze.append(sprite)
                structure.append(line_maze)
                self.structure = structure

    def display_maze(self, window):
        """ goes through the structure to associate a symbol with a picture and display it on the window """

        wall = pygame.image.load(pic_wall).convert()    # loads all the images
        framing = pygame.image.load(pic_grill).convert()
        start = pygame.image.load(pic_start).convert()
        end = pygame.image.load(pic_end).convert()
        floor = pygame.image.load(pic_floor).convert()
        line_number = 0
        for line in self.structure:    # goes through the structure
            sprite_number = 0
            for sprite in line:
                x = sprite_number * sprite_size    # converts the sprite number in pixels
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
    """ class Character contains every attribute and method to create a character, display it and make it move
    according to the user's decisions"""

    def __init__(self, pic="", x=0, y=0, sprite_x=0, sprite_y=0):
        """ initiates all the attributes needed for a character """

        self.state = 1
        self.pic = pic
        self.x = x
        self.sprite_x = sprite_x
        self.y = y
        self.sprite_y = sprite_y
        self.object_count = 0

    def display_character(self, window):
        """ pastes the character picture onto the window """

        if self.state:  # if alive
            character = pygame.image.load(self.pic).convert()
            window.blit(character, (self.x, self.y))

    def move(self, way, maze):
        """ lets the character to change his position according to the user's key pressings
        and tests in the wanted position is allowed to the character or not """

        self.sprite_x = self.x // sprite_size   # converts pixels into sprite numbers
        self.sprite_y = self.y // sprite_size
        if way == "r":
            if self.x < playground_size:    # if the wanted position is inside the playground
                    if maze.structure[self.sprite_y][self.sprite_x + 1] != "-":   # if the wanted position is not a wall
                        self.x += sprite_size   # changes the character's position

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
    """ defines an object and its attributes to generate it randomly and display it accordingly to its state """

    def __init__(self, name=" ", pic=0):
        """ initializes the object's attributes """

        self.name = name
        self.state = 1
        self.x = 0
        self.y = 0
        self.pic = pic

    def generate_object(self, maze, letter=""):
        """ generates the object at a random position checking the position is allowed """

        searching = True
        while searching:    # until the position randomly generated is not allowed
            self.x = random.randrange(0, 510, sprite_size)
            # generates a number between the two ends of the window at the range of the sprite size
            self.y = random.randrange(0, 510, sprite_size)
            sprite_x = self.x // sprite_size    # converts pixels into a sprite number
            sprite_y = self.y // sprite_size
            # checks that the position wanted is allowed
            if maze.structure[sprite_y][sprite_x] == ' ' and self.x != x_start \
                    and self.x != x_end and self.y != y_start and self.y != y_end:
                maze.structure[sprite_y][sprite_x] = letter    # prints a letter identifying the object in the structure
                searching = False   # when a valid position has been found

    def display_object(self, window):
        """ displays when generated """

        if self.state:  # if on the maze
            thing = pygame.image.load(self.pic).convert()
            window.blit(thing, (self.x, self.y))    # displays the object on the playground

    def display_dashboard(self, window, object_count):
        """ displays when picked up"""

        if self.state == 0:    # if picked up
            thing = pygame.image.load(self.pic).convert()
            window.blit(thing, (dashboard_start, sprite_size*2*object_count+x_start))   # displays the object on the dashboard
