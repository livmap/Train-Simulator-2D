import pygame
from utilities import *
from train import *
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRASSGREEN = (0, 255, 100)
 
# Initialize pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
 
# Create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Train Simulator - 2D")

track_width = 75
track_rail = 4

train_width = track_width + (2 * track_rail)
train_height = (train_width / 343) * 700

train = Train(500, 500, track_width, train_height)



train_img = loadImage("train.png", train.w, train.h)

# Initialize joystick
pygame.joystick.init()
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# Clock is used to set a max fps
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Joystick controls
    if joystick:
        # Axis 0 (horizontal movement)
        xAxis = joystick.get_axis(0)  # Returns a float between -1.0 and 1.0
        yAxis = joystick.get_axis(1)
        train.y += yAxis * 5  # Adjust speed as needed


    
    # Clear the screen
    screen.fill(GRASSGREEN)
    
    pygame.draw.line(screen, BLACK, ((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2, 0), ((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2, SCREEN_HEIGHT), track_rail)
    pygame.draw.line(screen, BLACK, (((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2) + track_width, 0), (((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2) + track_width, SCREEN_HEIGHT), track_rail)

    # Draw the train
    screen.blit(train_img, (train.x, train.y))
    
    # Flip the display
    pygame.display.flip()
     
    # How many updates per second
    clock.tick(FPS)
 
pygame.quit()
