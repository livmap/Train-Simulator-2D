import pygame

from utilities import *
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRASSGREEN = (0, 255, 100)
 
# initialize pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Train Simulator - 2D")

track_width = 60
track_rail = 3

train_width = track_width + (2* track_rail)

train_img = loadImage("train.png", train_width, (train_width / 343) * 700)
 
# clock is used to set a max fps
clock = pygame.time.Clock()
FPS = 60

 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(GRASSGREEN)
    
    pygame.draw.line(screen, BLACK, ((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2, 0), ((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2, SCREEN_HEIGHT), track_rail)
    pygame.draw.line(screen, BLACK, (((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2) + track_width, 0), (((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2) + track_width, SCREEN_HEIGHT), track_rail)

    # flip() updates the screen to make our changes visible

    screen.blit(train_img, ((SCREEN_WIDTH - (track_width + (track_rail * 2))) / 2, 500))
    
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(FPS)
 
pygame.quit()