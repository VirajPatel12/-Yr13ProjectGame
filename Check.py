import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Button Demo")

# Game loop
run = True:
while run:


    for event in pygame.event.get():
        if pygame.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()