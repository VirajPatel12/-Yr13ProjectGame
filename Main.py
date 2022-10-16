import pygame
from pygame.locals import *
import ButtonClass

pygame.init()

# Setting screen variable. Screen is the window of the game.
ScreenWidth = 300
ScreenHeight = 300
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("TicTacToe")
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
resume_button = ButtonClass.Button(0, 0, resume_image, 1)
quit_button = ButtonClass.Button(430, 400, quit_image, 1)

line_width = 6
markers = []
def draw_grid():
    background_colour = (28, 170, 156)
    grid = (50, 50, 50)
    screen.fill(background_colour)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (ScreenWidth, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, ScreenHeight), line_width)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_bg():
    screen.fill((100, 100, 100))

for x in range(3):
    row = [0] * 3
    markers.append(row)

print(markers)



run = True
while run:
    # Background Colour (function to change colour of screen)
    draw_grid()

    if game_paused == True:
        draw_bg()
        if resume_button.draw(screen):
            game_paused = False

        if quit_button.draw(screen):
            run = False
    else:
        draw_text("Press space to pause", font, TEXT_COL, 0, 0) # alligns and draws font

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                print("Pause")
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()