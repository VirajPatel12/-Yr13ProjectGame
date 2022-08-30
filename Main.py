import os
import pygame
import os
import time
import random
import tkinter
main = tkinter.Tk()
main.title("Space Invaders")
main.geometry('1000x1000')
# adding extra wedgets below
main.mainloop()

# loading icons/assets for the game (paste images)(os.path.join)
red_ship = 
pink_ship = 
yellow_ship =

# player ship (main own ship)

blue_ship = 

# Bullets

blue_bullets = 
pink_bullets = 
yellow_bullets = 
red_bullets = 

# Background load image
BG = color()


# Clock Object

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_tab(): #updates 60 timmes per second drawings inside fuction
        

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_tab()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()