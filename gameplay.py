import classes
import pygame


def main():
    pygame.init()
    on = True
    while on:
        game = classes.Game()
        game.initialize_window()
        game.initialize_game()
        playing = True
        while playing:
            pygame.display.flip()
            game.game_display()
            status = game.game_loop()
            if status == 0:
                playing = False
                on = False
            if status == 1:
                playing = False


main()
