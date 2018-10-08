import classes
import pygame
from pygame import *
from constants import *


def main():
    on = True
    while on:
        pygame.init()
        pygame.display.set_caption(title)
        window = pygame.display.set_mode((side_size, side_size))
        background = pygame.image.load(pic_background).convert_alpha()
        text_font = pygame.font.Font(None, 20)
        i = 0
        for msg in rules:
            rules_text = text_font.render(msg, 1, (10, 10, 10))
            background.blit(rules_text, (20, 530+i))
            i += 35
        i = 0
        for msg in objects:
            object_text = text_font.render(msg, 1, (10, 10, 10))
            background.blit(object_text, (510, 30 * i))
            i += 2
        window.blit(background, (0, 0))

        maze = classes.Maze()
        maze.get_maze()

        mac_gyver = classes.Character()
        mac_gyver.pic = pic_mac_gyver
        mac_gyver.x = x_start
        mac_gyver.y = y_start

        guardian = classes.Character()
        guardian.pic = pic_guardian
        guardian.x = x_end
        guardian.y = y_end

        ether = classes.Object()
        ether.name = "ether"
        ether.pic = pic_ether
        ether.generate_object(maze, "et")

        needle = classes.Object()
        needle.name = "needle"
        needle.pic = pic_needle
        needle.generate_object(maze, "ne")

        syringe = classes.Object()
        syringe.name = "syringe"
        syringe.pic = pic_syringe
        syringe.generate_object(maze, "sy")

        playing = True

        while playing:
            pygame.display.flip()

            maze.display_maze(window)
            guardian.display_character(window)
            ether.display_object(window)
            needle.display_object(window)
            syringe.display_object(window)
            mac_gyver.display_character(window)

            count = str(mac_gyver.object_count)
            object_count = text_font.render(count, 1, (10, 10, 10))
            count_window = pygame.image.load(pic_count_window).convert()
            count_window.blit(object_count, (10, 10))
            window.blit(count_window, (520, 20))

            if maze.struct[mac_gyver.y // sprite_size][mac_gyver.x // sprite_size] == "et":
                ether.state = 0
                maze.struct[mac_gyver.y // sprite_size][mac_gyver.x // sprite_size] = " "
                mac_gyver.object_count += 1
                ether.display_dashboard(window, mac_gyver.object_count)

            if maze.struct[mac_gyver.y // sprite_size][mac_gyver.x // sprite_size] == "ne":
                needle.state = 0
                maze.struct[mac_gyver.y // sprite_size][mac_gyver.x // sprite_size] = " "
                mac_gyver.object_count += 1
                needle.display_dashboard(window, mac_gyver.object_count)

            if maze.struct[mac_gyver.y // sprite_size][mac_gyver.x // sprite_size] == "sy":
                syringe.state = 0
                maze.struct[mac_gyver.y // sprite_size][mac_gyver.x // sprite_size] = " "
                mac_gyver.object_count += 1
                syringe.display_dashboard(window, mac_gyver.object_count)

            if mac_gyver.x == x_end and mac_gyver.y == y_end and mac_gyver.object_count == 3:
                playing = False
                won = True
                while won:
                    pygame.display.flip()
                    pygame.display.set_caption(title)
                    window = pygame.display.set_mode((510, 510))
                    victory = pygame.image.load(pic_victory).convert()
                    text_font = pygame.font.Font(None, 36)
                    text = text_font.render(victory_text, 1, (10, 10, 10))
                    victory.blit(text, (50, 100))
                    window.blit(victory, (0, 0))
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                won = False
                                on = False
                            elif event.key == K_RETURN:
                                won = False

            if mac_gyver.x == x_end and mac_gyver.y == y_end and mac_gyver.object_count < 3:
                playing = False
                lost = True
                while lost:
                    pygame.display.flip()
                    pygame.display.set_caption(title)
                    window = pygame.display.set_mode((510, 510))
                    loss = pygame.image.load(pic_loss).convert()
                    text_font = pygame.font.Font(None, 36)
                    text = text_font.render(loss_text, 1, (10, 10, 10))
                    loss.blit(text, (120, 100))
                    window.blit(loss, (0, 0))
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                lost = False
                                on = False
                            elif event.key == K_RETURN:
                                lost = False

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        on = False
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
