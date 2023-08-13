import pygame
from Entities.Menu import Menu
from Entities.Game import Game
import sys


def run():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Perotto Relativotto")

    clock = pygame.time.Clock()

    menu = Menu(pygame, screen)

    while True:
        menu_result = menu.process_events()

        if menu_result == "iniciar_jogo":
            game = Game(pygame)
            game.run()

        menu.draw()

        pygame.display.flip()
        clock.tick(60)


run()