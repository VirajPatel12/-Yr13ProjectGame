import pygame # Importing variables
from pygame.locals import *
import ButtonClass

pygame.init() # Initialises Pygame

# Setting screen variable. Screen is the window of the game.
ScreenWidth = 300 # Will use height and width dimensions further when making the board, etc
ScreenHeight = 300
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight)) # Dimensions for the display
pygame.display.set_caption("TicTacToe") # Game title
pygame.display.update() # Updates changes

# Variable for pausing the game
game_paused = False # Variable making for a "pause" when Tic Tac Toe playyed

# Font variables
font = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont(None, 40)



# button images
resume_image = pygame.image.load("ResumeButton.png").convert_alpha()
quit_image = pygame.image.load("QuitButton.png").convert_alpha()


# Button instances, again rect has coordinates of text

quit_button = ButtonClass.Button(-30, 150, quit_image, 1)
again_rect = Rect(ScreenWidth // 2 - 80, ScreenHeight // 2, 160, 50)

# Define temporary variables (for the start of my Tic Tac Toe game)
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False


# Colours for the project

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
TEXT_COL = (255, 255, 255)

# Drawing grid function, draws 3 by 3 lines for Tic Tac Toe
def draw_grid():
    background_colour = (28, 170, 156)
    grid = (50, 50, 50)
    screen.fill(background_colour)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (ScreenWidth, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, ScreenHeight), line_width)

# Draws the text fot the menu
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Function for drawing the markers (crosses, and zeros) for the game
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

# Function important to check for the winner/winning conditions
def check_winner():

    global winner
    global game_over

    y_pos = 0
    for x in markers:

        if sum(x) == 3:
            winner = 1 # States different occasions for the different winner below
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

# Defined a background function
def draw_bg():
    screen.fill((0,0,0))

# For loops for the markers
for x in range(3):
    row = [0] * 3
    markers.append(row)

print(markers) # Lists different numbers

# Defines function to "draw" (write text) for the conditions of the winner, and option to retry (with buttons)
def draw_winner(winner):
    win_text = 'Player' + str(winner) + " Wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (ScreenWidth // 2 - 100, ScreenHeight // 2 - 60, 200, 50))
    screen.blit(win_img, (ScreenWidth // 2 - 150, ScreenHeight // 2 - 50))

    again_text = 'Play Again?' # dimensions
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (ScreenWidth // 2 - 110, ScreenHeight // 2 + 10))


# Main game loop

run = True
while run:
    # Background Colour (function to change colour of screen).
    draw_grid()
    draw_markers() # Stating functions for the Tic Tac Toe basis.

    if game_paused == True: # Below makes space = pause, which puts a menu.
        draw_bg()
        draw_text("Press Space", font, TEXT_COL, 10, 0)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # States if space pressed, game appears from pause menu.
                    game_paused = False

        if quit_button.draw(screen):
            run = False # If clicked on quit button (in pause menu), game quits.
    else:
        draw_text("Press Space", font, TEXT_COL, 10, 0) # alligns and draws font

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
                    check_winner() # After the clicking interaction, goes back to check winner function to meet winning conditions


    if game_over == True: # Game over variable
        if game_paused == True:
            draw_bg() # below is coded to keep the pause menu and not let winning text overlap
            draw_text("Press space to unpause", font, TEXT_COL, 0, 0)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_paused = False

            if quit_button.draw(screen):
                run = False
        else:
            draw_winner(winner) # Draws the winner
            # check if user has clicked on again button
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos() # Has mouse position
                if again_rect.collidepoint(pos):
                    # Variable reset in order to meet the 'retry' option
                    markers = []
                    pos = []
                    player = 1
                    winner = 0
                    game_over = False
                    for x in range(3):
                        row = [0] * 3
                        markers.append(row)


    pygame.display.update() # Updates after changes, important

pygame.quit()