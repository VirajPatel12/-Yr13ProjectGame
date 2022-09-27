import pygame

pygame.init()

# Setting screen variable. Screen is the window of the game.

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
pygame.display.update()

start_img = pygame.image.load('play.jpeg').convert_alpha()

# Button class

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), ()))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#Create button instances
start_button = Button(100, 200, start_img)


run = True
while run:
    # Background Colour (function to change colour of screen)
    screen.fill((52, 78, 91))
    start_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                print("Pause")
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()