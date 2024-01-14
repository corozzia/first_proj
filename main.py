import sys

import pygame

WIDTH = 1200  # ширина игрового окна
HEIGHT = 800  # высота игрового окна
BG_COLOR = (0, 0, 0)

def run_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.quit():
        #         sys.exit()
        pygame.display.flip()
run_game()