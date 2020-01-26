import pygame, sys, random, math
from pygame.locals import *

def color(min,max):
    r=random.randint(min,max)
    g=random.randint(min,max)
    b=random.randint(min,max)
    return r,g,b

pygame.init()
FPS=120#frames per second
fpsClock=pygame.time.Clock()
red=255
green=0
blue=0

screen=pygame.display.set_mode((1152,720),0,32)
img=pygame.image.load('images/plane.png')
bullet=pygame.image.load('images/bullet.png')
img2=pygame.transform.rotate(img, 0)
pygame.display.set_caption('Animation')
heart=pygame.image.load('images/lives/4.png')

backimg=pygame.image.load('images/sky.png').convert()

lives=4
imgx=50
imgy=100
bulletx=1152
bullety=450
pygame.key.set_repeat(1,50)

def live():
    global lives, heart
    if lives==4:
        heart=pygame.image.load('images/lives/4.png')  
    if lives==3:
        heart=pygame.image.load('images/lives/3.png')  
    if lives==2:
        heart=pygame.image.load('images/lives/2.png')  
    if lives==1:
        heart=pygame.image.load('images/lives/1.png')  
    if lives==0:
        heart=pygame.image.load('images/lives/0.png')     

while True:#game loop
    screen.fill((255,255,255))    
    screen.blit(backimg,(0,0))
    screen.blit(img2,(imgx,imgy))
    screen.blit(bullet,(bulletx,bullety))
    screen.blit(heart,(485,5))
    live()
    if lives>0:
        #---------------------------------------
        if bulletx>-36:
            bulletx-=2
        else:
            bulletx=1152
            bullety=random.randint(40,450)
        #--------------------------------------
        if math.hypot(((imgx+59)-(bulletx+18)),((imgy+35)-(bullety+16)))<60:
            bulletx=1152
            bullety=random.randint(40,450)
            lives-=1
        #--------------------------------------
    else:
        bulletx=1116
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_UP or event.key==K_w:
                if imgy>=15:
                    imgy=imgy-10
                img2=pygame.transform.rotate(img, 15)
            elif event.key==K_DOWN or event.key==K_s:
                if imgy<=400:
                    imgy=imgy+10
                img2=pygame.transform.rotate(img, 345)
        if event.type==KEYUP:
            img2=pygame.transform.rotate(img, 0)
    pygame.display.update()
    fpsClock.tick(FPS)
