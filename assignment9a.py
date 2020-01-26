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
img2=pygame.transform.rotate(img, 0)
pygame.display.set_caption('Animation')

backimg=pygame.image.load('images/sky.png').convert()


imgx=50
imgy=605
pygame.key.set_repeat(10,100)

while True:#game loop
    screen.fill((255,255,255))    
    screen.blit(backimg,(0,0))
    screen.blit(img2,(imgx,imgy))
    #---------------------------------------
    #--------------------------------------
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                imgx=imgx-10
                img2=pygame.transform.rotate(img, 0)
            elif event.key==K_RIGHT:
                imgx=imgx+10
                img2=pygame.transform.rotate(img, 0)
            elif event.key==K_UP:
                imgy=imgy-10
                img2=pygame.transform.rotate(img, 15)
            elif event.key==K_DOWN:
                imgy=imgy+10
                img2=pygame.transform.rotate(img, 345)
    pygame.display.update()
    fpsClock.tick(FPS)
