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
font2 = pygame.font.SysFont(None, 40)

# Define Colour
TEXT_COL = (255, 255, 255)

# button images
resume_image = pygame.image.load("ResumeButton.png").convert_alpha()
quit_image = pygame.image.load("QuitButton.png").convert_alpha()

# button instances
resume_button = ButtonClass.Button(0, 0, resume_image, 1)
quit_button = ButtonClass.Button(430, 400, quit_image, 1)

# define temporary variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False
pos = (0, 0)

# colours

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

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

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1

def check_winner():

    global winner
    global game_over

    y_pos = 0
    for x in markers:

        if sum(x) == 3:
            winner = 1
            game_over = True

        if sum(x) == 3:
            winner = 2
            game_over = True

            # row check
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True

        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[2][2] == 3:
        winner = 1
        game_over = True

    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[2][2] == -3:
        winner = 2
        game_over = True


def draw_bg():
    screen.fill((100, 100, 100))

for x in range(3):
    row = [0] * 3
    markers.append(row)

print(markers) # lists different numbers

def draw_winner():
    win_text = 'Player' + str(winner) + " Wins!"

run = True
while run:
    # Background Colour (function to change colour of screen)
    draw_grid()
    draw_markers()

    if game_paused == True: # below makes space = pause, which puts a menu.
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
            # This is a click cycle, so when you click/release, a variable becomes true/false
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos() # Gives mouse coordinates/location
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()



        pygame.display.update()

pygame.quit()