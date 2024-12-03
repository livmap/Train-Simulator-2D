import pygame
from utilities import *
from train import *
from track import *
 
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

track = Track(60, 4)

train_width = track.w + (2 * track.t)
train_height = (track.w / 343) * 700

train = Train((SCREEN_WIDTH - train_width) / 2, 500, track.w, train_height)

# Load Images

train_img = loadImage("train.png", train.w, train.h)


pygame.joystick.init()
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()


clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    if joystick:
   
        xAxis = joystick.get_axis(0)  
        yAxis = joystick.get_axis(1)
        train.velocity += yAxis
    
    train.y += train.velocity
    if train.velocity > 0:
        train.velocity -= track.friction
    elif train.velocity < 0:
        train.velocity += track.friction


    screen.fill(GRASSGREEN)
    
    pygame.draw.line(screen, BLACK, ((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2, 0), ((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2, SCREEN_HEIGHT), track.t)
    pygame.draw.line(screen, BLACK, (((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2) + track.w, 0), (((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2) + track.w, SCREEN_HEIGHT), track.t)


    screen.blit(train_img, (train.x, train.y))
    
    pygame.display.flip()
     
    clock.tick(FPS)
 
pygame.quit()
