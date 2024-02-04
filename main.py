import pygame

back = pygame.image.load("images/New Piskel.png")
width = 1000
height = 800
score = 0
pygame.font.init()
font_1 = pygame.font.SysFont('arial black', 45)
text_score = font_1.render("score: 0", True, (34, 55, 123))
text_time = font_1.render('time: 0:', True, (34, 55, 123))


def run_game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("my game")
    while True:
        screen.blit(back, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(text_score, (10, 0))
        screen.blit(text_time, (10, 40))
        pygame.display.update()


run_game()
