import pygame
import math

def loadImage(name, w=None, h=None):

    img = pygame.image.load("/Users/princemaphupha/Desktop/Games/TrainDriver/assets/" + name)
    if(w != None):
        img = pygame.transform.scale(img, (w, h))

    return img

def distance(x1, y1, w1, h1, x2, y2, w2, h2):

    dist = 0

    cx1 = x1 + (w1 / 2)
    cy1 = y1 + (h1 / 2)
    cx2 = x2 + (w2 / 2)
    cy2 = y2 + (h2 / 2)

    dist = math.sqrt((math.pow(cx2 - cx1, 2)) + math.pow(cy2 - cy1, 2))

    return dist
