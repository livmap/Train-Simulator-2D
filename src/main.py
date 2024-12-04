import pygame
import math
import random

from utilities import *
from train import *
from track import *
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRASSGREEN = (0, 255 * 0.1, 100 * 0.1)
DIRTBROWN = (150, 75, 0)

world = []

for x in range(70):
    world.append([])

for x in range(70):
    for y in range(100):
        num = random.randint(0,1)
        block = None

        if num == 0:
            block = "GRASS"
        else:
            block = "DIRT"

        world[x ].append(block)



def drawWorld():
    for x in range(70):
        for y in range(100):
            if world[x ][y ] == "GRASS":
                pygame.draw.rect(screen, GRASSGREEN, ((y ) * 10, (x ) * 10, 10, 10))
            elif world[x ][y ] == "DIRT":
                pygame.draw.rect(screen, DIRTBROWN, ((y ) * 10, (x ) * 10, 10, 10))

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
count = 0
ticker = 0

font = pygame.font.Font(None, 36)

lt = 0
rt = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    if joystick:
   
        xAxis = joystick.get_axis(0)  
        yAxis = joystick.get_axis(1)
        lt = joystick.get_axis(2)
        rt = joystick.get_axis(5)

        train.velocity += yAxis / 10
    
    if train.y > 300:
        train.y += train.velocity
    if train.velocity > 0:
        train.velocity -= track.friction
        train.velocity -= 0.295 * (math.pow(train.velocity, 2)) * 1.1125 * (0.0001)
            
    elif train.velocity < 0:
        train.velocity += track.friction
        train.velocity += 0.295 * (math.pow(train.velocity, 2)) * 1.1125 * (0.0001)
 
            

    if train.velocity < 0:
        count -= train.velocity
        number = int(count  / 100) 
        
        if number != ticker:
            del world[-1]
            newLine = []
            for x in range(100):
                num = random.randint(0,1)
                block = None

                if num == 0:
                    block = "GRASS"
                else:
                    block = "DIRT"

                newLine.append(block)

            world.insert(0, newLine)
            ticker = number

    #screen.fill(GRASSGREEN)
    
    drawWorld()
    pygame.draw.line(screen, BLACK, ((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2, 0), ((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2, SCREEN_HEIGHT), track.t)
    pygame.draw.line(screen, BLACK, (((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2) + track.w, 0), (((SCREEN_WIDTH - (track.w + (track.t * 2))) / 2) + track.w, SCREEN_HEIGHT), track.t)    

    text_surface = font.render("VELOCITY: " + str(-1 * int(train.velocity)) + " KM/H", True, BLACK)
    screen.blit(text_surface, (10, 10))

    screen.blit(train_img, (train.x, train.y))
    
    pygame.display.flip()

    
     
    clock.tick(FPS)
 
pygame.quit()
