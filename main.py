import pygame

back = pygame.image.load("images/New Piskel.png")
width = 1000
height = 800


def run_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Game")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(back, (0, 0))
        pygame.display.update()


run_game()
