import sys

import pygame


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("My Game")

back = pygame.image.load("images/New Piskel.png")
screen.blit(back, (0, 0))
def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

run_game()