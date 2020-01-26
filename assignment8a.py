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

screen=pygame.display.set_mode((1200,700),0,32)
pygame.display.set_caption('Animation')

imgx=50
imgy=50

while True:#game loop
    screen.fill((255,255,255))
    circle=pygame.draw.circle(screen,(red,green,blue),(imgx,imgy),50)
    #---------------------------------------
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                imgx=imgx-10
                red,green,blue=color(0,255)
            elif event.key==K_RIGHT:
                imgx=imgx+10
                red,green,blue=color(0,255)
            elif event.key==K_UP:
                imgy=imgy-10
                red,green,blue=color(0,255)
            elif event.key==K_DOWN:
                imgy=imgy+10
                red,green,blue=color(0,255)
    pygame.display.update()
    fpsClock.tick(FPS)

