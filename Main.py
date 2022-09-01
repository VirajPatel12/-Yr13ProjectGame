import os
import pygame
import os
import time
import random
import tkinter
from pygame.locals import *
pygame.font.init()
main = tkinter.Tk()
main.title("Space Invaders")
main.geometry('1000x1000')
# adding extra wedgets below
main.mainloop()


# Background load image command + scales it according to dimensions.
BACKGROUND = pygame.image.load('Background.png')

#create screen 
screen = pygame.display.set_mode((800, 600))
#list variables below
running = True
while running:
    screen.blit(BACKGROUND, (0, 0))

# Clock Object

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("Arial", 50, bold=False, italic=False)
    clock = pygame.time.Clock()

    def redraw_tab(): #updates 60 timmes per second drawings inside fuction
        WIN.blit(BG, (0,0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255 ))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255 ))   

        WIN.blit(lives_label, (10, 10))   
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10)) 

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_tab()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()