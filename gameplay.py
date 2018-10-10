import classes
import pygame


""" Main function instantiates game and calls every method needed to run the game within the gameloop """


def main():
    pygame.init()
    on = True
    while on:    # Runs as long as the program is on
        game = classes.Game()
        game.initialize_window()
        game.initialize_game()
        playing = True
        while playing:    # Runs as ling as the game is playing
            pygame.display.flip()
            game.game_display()
            status = game.game_loop()    # Returns the status of the loop
            if status == 0:    # User pressed escape to leave the game
                playing = False
                on = False
            if status == 1:     # User pressed entry to play again
                playing = False


main()
