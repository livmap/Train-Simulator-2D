import pygame
import math
import random

from utilities import *
from train import *
from track import *
from interChange import *


pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
 
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Train Simulator - 2D")
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRASSGREEN = (0, 200, 100)
DIRTBROWN = (150, 75, 0)

world = []
railNetwork = []
railNetwork2 = []


departure = (0, 0)
arrival = (150, 2000)

leftY = 2000
leftX = 150

track_width = 60
track_thick = 4

track_x_init = ((SCREEN_WIDTH - track_width) / 2) - track_thick


for x in range(15):
    if x == 0:
        railItem = Track(track_x_init, SCREEN_HEIGHT, track_width, 200, track_thick)
        railNetwork.append(railItem)
        railItem2 = Track(track_x_init + track_width, SCREEN_HEIGHT, track_width, 200, track_thick)
        railNetwork2.append(railItem2)
    else:
        railPrev = railNetwork[x - 1]
        railItem = Track(railPrev.endX, railPrev.endY, track_width, 200, track_thick)
        railNetwork.append(railItem)

        railPrev2 = railNetwork2[x - 1]
        railItem2 = Track(railPrev2.endX, railPrev2.endY, track_width, 200, track_thick)
        railNetwork2.append(railItem2)

interItem = InterChange(railNetwork[14].endX, railNetwork[14].endY, track_width, track_thick, 60, 250)
interItem2 = InterChange(railNetwork[14].endX + track_width, railNetwork[14].endY, track_width, track_thick, 60, 250)
railNetwork.append(interItem)
railNetwork2.append(interItem2)

for x in range(len(railNetwork) - 1, len(railNetwork) - 1 + 15):
    if x == 0:
        railItem = Track(track_x_init, SCREEN_HEIGHT, track_width, 200, track_thick)
        railNetwork.append(railItem)
        railItem2 = Track(track_x_init + track_width, SCREEN_HEIGHT, track_width, 200, track_thick)
        railNetwork2.append(railItem2)
    else:
        railPrev = railNetwork[x]
        railItem = Track(railPrev.endX, railPrev.endY, track_width, 200, track_thick)
        railNetwork.append(railItem)

        railPrev2 = railNetwork2[x]
        railItem2 = Track(railPrev2.endX, railPrev2.endY, track_width, 200, track_thick)
        railNetwork2.append(railItem2)

numRails = len(railNetwork)

interItem = InterChange(railNetwork[numRails - 1].endX, railNetwork[numRails - 1].endY, track_width, track_thick, 120, 250)
interItem2 = InterChange(railNetwork[numRails - 1].endX + track_width, railNetwork[numRails - 1].endY, track_width, track_thick, 120, 250)
railNetwork.append(interItem)
railNetwork2.append(interItem2)

numRails = len(railNetwork)

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

track = railNetwork[0]

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

yAxis = 0
xAxis = 0

renderYMove = 0
xShift = 0
x_shift_init = 0
overInterChange = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    lastRail = None
    currentRail = None
    

    for x in range(numRails):
        if railNetwork[x].y >= renderYMove and railNetwork[x].endY < renderYMove:
            lastRail = railNetwork[x]

    overInterChange = False

    for x in range(numRails):
        if railNetwork[x].y - renderYMove >= (train.y + (train.h / 2)) and railNetwork[x].endY - renderYMove < (train.y + (train.h / 2)):
            currentRail = railNetwork[x]
            if currentRail.x != currentRail.endX:
                overInterChange = True
                
            else:
                overInterChange = False

    
    index = 0
    if lastRail != None:
        index = railNetwork.index(lastRail)
    else:
        index = numRails - 1

    h = 0
    startIndex = 0

    while h < SCREEN_HEIGHT and startIndex >= 0:
        h += railNetwork[index].yChange
        startIndex -= index

    if joystick:
   
        xAxis = joystick.get_axis(0)  
        yAxis = joystick.get_axis(1)
        lt = joystick.get_axis(2)
        rt = joystick.get_axis(5)

        train.velocity += yAxis / 50
    
    if train.y > 300:
        train.y += train.velocity
    else:
        renderYMove += train.velocity
        
    if train.velocity > 0:
        train.velocity -= track.friction
        train.velocity -= 0.295 * (math.pow(train.velocity, 2)) * 1.1125 * (0.00001)
            
    elif train.velocity < 0:
        train.velocity += track.friction
        train.velocity += 0.295 * (math.pow(train.velocity, 2)) * 1.1125 * (0.00001)            

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
    
    drawWorld()

    for x in range(startIndex, index + 1):
        
        pygame.draw.line(screen, BLACK, (railNetwork[x].x + xShift, railNetwork[x].y - renderYMove), (railNetwork[x].endX + xShift, railNetwork[x].endY - renderYMove), railNetwork[x].t)
        pygame.draw.line(screen, BLACK, (railNetwork2[x].x + xShift, railNetwork2[x].y - renderYMove), (railNetwork2[x].endX + xShift, railNetwork2[x].endY - renderYMove), railNetwork2[x].t)

    if overInterChange:
        gradient = ( currentRail.y - currentRail.endY ) / ( currentRail.endX - currentRail.x )
        yChange = (currentRail.y - renderYMove) - (train.y + (train.h / 2))
        xShift = x_shift_init -(yChange / gradient)
    else:
        x_shift_init = xShift

    velocity_text = font.render("VELOCITY: " + str(-1 * int(train.velocity)) + " KM/H", True, BLACK)
    throttle_text = None
    
    if -1 * int(yAxis * 100) >= 0:
        if -1 * int(yAxis * 100) > train.dangerThrottle:
            throttle_text = font.render("THROTTLE: " + str(-1 * int(yAxis * 100)) + " %", True, RED)
        else:
            throttle_text = font.render("THROTTLE: " + str(-1 * int(yAxis * 100)) + " %", True, BLACK) 
    else:
        throttle_text = font.render("BRAKES ENGAGED", True, RED) 

    distance_text = font.render("DISTANCE: " + str(int(count * (1 / 360))) + " M", True, BLACK)

    screen.blit(velocity_text, (10, 10))
    screen.blit(throttle_text, (10, 30))
    screen.blit(distance_text, (10, 50))

    screen.blit(train_img, (train.x, train.y))
    
    pygame.display.flip()
     
    clock.tick(FPS)
 
pygame.quit()
