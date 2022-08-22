from sys import exit
from pygame.locals import *
from StrategyGame import *
import random

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aircraft War Game')

BULLETSHOT_SOUNDTEST = pygame.mixer.Sound('image/sound/bullet.wav')
OPPONENT1_DOWN_SOUNDTEST = pygame.mixer.Sound('image/sound/opponent1_down.wav')
GAMEOVER_SOUNDTEST = pygame.mixer.Sound('image/sound/game_over.wav')
BULLETSHOT_SOUNDTEST.set_volume(0.3)
OPPONENT1_DOWN_SOUNDTEST.set_volume(0.3)
GAMEOVER_SOUNDTEST.set_volume(0.3)
pygame.mixer.music.load('image/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

GAME_BACKGROUND = pygame.image.load('image/image/background.png').convert()
GAME_OVER = pygame.image.load('image/image/gameover.png')
filename = 'image/image/aircraft_shooter.png'
AIRCRAFT_IMAGES = pygame.image.load(filename)

AIRCRAFT_PLAYER = []
AIRCRAFT_PLAYER.append(pygame.Rect(0, 99, 102, 126)) 
AIRCRAFT_PLAYER.append(pygame.Rect(165, 360, 102, 126))
AIRCRAFT_PLAYER.append(pygame.Rect(165, 234, 102, 126)) 
AIRCRAFT_PLAYER.append(pygame.Rect(330, 624, 102, 126))
AIRCRAFT_PLAYER.append(pygame.Rect(330, 498, 102, 126))
AIRCRAFT_PLAYER.append(pygame.Rect(432, 624, 102, 126))
AIRCRAFT_PLAYER_POSITION = [200, 600]
OPPONENT = Opponent(AIRCRAFT_IMAGES, AIRCRAFT_PLAYER, AIRCRAFT_PLAYER_POSITION)

# Define the surface related parameters used by the bullet object
AIRCRAFT_BULLET = pygame.Rect(1004, 987, 9, 21)
BULLET_IMAGES = AIRCRAFT_IMAGES.subsurface(AIRCRAFT_BULLET)

# Define the surface related parameters used by the opponent object
OPPONENT1 = pygame.Rect(534, 612, 57, 43)
OPPONENT1_IMAGES = AIRCRAFT_IMAGES.subsurface(OPPONENT1)
OPPONENT1_DOWN_IMAGES = []
OPPONENT1_DOWN_IMAGES.append(AIRCRAFT_IMAGES.subsurface(pygame.Rect(267, 347, 57, 43)))
OPPONENT1_DOWN_IMAGES.append(AIRCRAFT_IMAGES.subsurface(pygame.Rect(873, 697, 57, 43)))
OPPONENT1_DOWN_IMAGES.append(AIRCRAFT_IMAGES.subsurface(pygame.Rect(267, 296, 57, 43)))
OPPONENT1_DOWN_IMAGES.append(AIRCRAFT_IMAGES.subsurface(pygame.Rect(930, 697, 57, 43)))

CHALLENGER1 = pygame.sprite.Group()

# Store the destroyed aircraft for rendering the wrecking sprite animation
CHALLENGER_DOWN = pygame.sprite.Group()

SHOOT_DISTANCE = 0
CHALLENGER_DISTANCE = 0

OPPONENT_DOWN_INDEX = 16

SCORE = 0

CLOCK = pygame.time.Clock()

RUNNING = True

while RUNNING:
    # Control the maximum frame rate of the game is 60
    CLOCK.tick(60)

    # Control the firing of the bullet frequency and fire the bullet
    if not OPPONENT.is_hit:
        if SHOOT_DISTANCE % 15 == 0:
            BULLETSHOT_SOUNDTEST.play()
            OPPONENT.shoot(BULLET_IMAGES)
        SHOOT_DISTANCE += 1
        if SHOOT_DISTANCE >= 15:
            SHOOT_DISTANCE = 0

    # Generating opponent aircraft
    if SHOOT_DISTANCE % 50 == 0:
        CHALLENGER1_POSITION = [random.randint(0, SCREEN_WIDTH - OPPONENT1.width), 0]
        CHALLENGERS1 = Challenger(OPPONENT1_IMAGES, OPPONENT1_DOWN_IMAGES, CHALLENGER1_POSITION)
        CHALLENGER1.add(CHALLENGERS1)
    CHALLENGER_DISTANCE += 1
    if CHALLENGER_DISTANCE >= 100:
        CHALLENGER_DISTANCE = 0

    # Move the bullet and delete if it is exceeds the window
    for bullet in OPPONENT.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            OPPONENT.bullets.remove(bullet)