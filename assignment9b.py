import pygame, sys, random
from pygame.locals import *

def color(min,max):
    r=random.randint(min,max)
    g=random.randint(min,max)
    b=random.randint(min,max)
    return r,g,b

pygame.init()
FPS=60#frames per second
fpsClock=pygame.time.Clock()
red=255
green=0
blue=0

screen=pygame.display.set_mode((1152,720),0,32)
img=pygame.image.load('images/plane.png')
bullet=pygame.image.load('images/bullet.png')
img2=pygame.transform.rotate(img, 0)
pygame.display.set_caption('Animation')

backimg=pygame.image.load('images/sky.png').convert()


imgx=50
imgy=605
bulletx=1152
bullety=450
position=1
pygame.key.set_repeat(10,100)

while True:#game loop
    screen.fill((255,255,255))    
    screen.blit(backimg,(0,0))  
    screen.blit(bullet,(bulletx,bullety))
    screen.blit(img2,(imgx,imgy))
    #---------------------------------------
    if bulletx>-36:
        bulletx-=5
    else:
        bulletx=1152
        bullety=random.randint(40,450)
    
    pygame.display.update()
    fpsClock.tick(FPS)
