import pygame

back = pygame.image.load("images/New Piskel.png")

def run_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("My Game")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(back, (0, 0))
        pygame.display.update()


run_game()
