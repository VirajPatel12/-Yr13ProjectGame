import pygame # Imports basic
class Button(): # Button class to import to Main.py
    def __init__(self, x, y, image, scale): # Function within class to make Rect for button/image/scale
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface): # Draws the button itself, and the mouse interaction for tthe class
        action = False
        # Recieves the mouse button
        pos = pygame.mouse.get_pos()

        # Checked the clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draws button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action # Returns/turns off

