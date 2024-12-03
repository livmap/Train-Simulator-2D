import pygame

def loadImage(name, w=None, h=None):

    img = pygame.image.load("/Users/princemaphupha/Desktop/Games/TrainDriver/assets/" + name)
    if(w != None):
        img = pygame.transform.scale(img, (w, h))

    return img

