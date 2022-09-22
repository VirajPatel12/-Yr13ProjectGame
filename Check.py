import pygame, sys

pygame.init()

# Setting screen variable. Screen is the window of the game.

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
pygame.display.update()

# Game variables
game_paused = False

# Define Fonts
font = pygame.font.SysFont("arialblack", 40)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Define Colours
TEXT_COL = (255, 255, 255)


run = True
while run:
    # Background Colour (function to change colour of screen)
    screen.fill((52, 78, 91))

    if game_paused == True:
        pass
    else:
        draw_text("Press space to pause", font, TEXT_COL, 160, 250)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                print("Pause")
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()