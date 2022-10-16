import pygame, sys
import Button

pygame.init()

# Setting screen variable. Screen is the window of the game.
ScreenWidth = 1280
ScreenHeight = 720
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Menu")
pygame.display.update()

# Game variables
game_paused = False

# Define Fonts
font = pygame.font.SysFont("arialblack", 40)

# Define Colour
TEXT_COL = (255, 255, 255)

# button images
resume_image = pygame.image.load("ResumeButton.png").convert_alpha()
quit_image = pygame.image.load("QuitButton.png").convert_alpha()

# button instances
resume_button = Button.Button(400, 125, resume_image, 1)
quit_button = Button.Button(430, 400, quit_image, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    # Background Colour (function to change colour of screen)
    screen.fill((52, 78, 91))

    if game_paused == True:
        if resume_button.draw(screen):
            game_paused = False
        if quit_button.draw(screen):
            run = False
    else:
        draw_text("Press space to pause", font, TEXT_COL, 400, 280) # alligns and draws font

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                print("Pause")
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()