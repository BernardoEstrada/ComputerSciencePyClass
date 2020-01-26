import pygame, sys, random, math
from pygame.locals import *

screen=pygame.display.set_mode((1152,720),0,32)
backimg=pygame.image.load('images/classroom/back.png')

hair=pygame.image.load('images/classroom/curl_black.png')
eyes=pygame.image.load('images/classroom/eye_blue.png')
skin=(243,203,173)
shirt=(255,0,0)
mouth=pygame.image.load('images/classroom/smile.png')

def kid(x,y):
    global skin, shirt
    pygame.draw.rect(screen,shirt,[x-20,y,40,100])
    pygame.draw.rect(screen,(0,0,100),[x-20,y+100,40,75])
    pygame.draw.circle(screen,skin,(x,y),44)
    screen.blit(hair,(x-49,y-49))
    screen.blit(eyes,(x-20,y-18))
    screen.blit(mouth,(x-22,y+10))
    
def randomize():
    global hair, eyes, skin, shirt, mouth
#-hair----------------------------------------------------------------------------------
    r=random.randint(0,11)
    if r==0:
        hair=pygame.image.load('images/classroom/curl_black.png')
    elif r==1:
        hair=pygame.image.load('images/classroom/curl_brown.png')
    elif r==2:
        hair=pygame.image.load('images/classroom/curl_red.png')
    elif r==3:
        hair=pygame.image.load('images/classroom/curl_yellow.png')    
    elif r==4:
        hair=pygame.image.load('images/classroom/long_black.png')
    elif r==5:
        hair=pygame.image.load('images/classroom/long_brown.png')
    elif r==6:
        hair=pygame.image.load('images/classroom/long_red.png')
    elif r==7:
        hair=pygame.image.load('images/classroom/long_yellow.png')
    elif r==8:
        hair=pygame.image.load('images/classroom/short_black.png')
    elif r==9:
        hair=pygame.image.load('images/classroom/short_brown.png')
    elif r==10:
        hair=pygame.image.load('images/classroom/short_red.png')
    elif r==11:
        hair=pygame.image.load('images/classroom/short_yellow.png')
#-eyes----------------------------------------------------------------------------------
    r=random.randint(0,3)
    if r==0:
        eyes=pygame.image.load('images/classroom/eye_blue.png')
    elif r==1:
        eyes=pygame.image.load('images/classroom/eye_brown.png')
    elif r==2:
        eyes=pygame.image.load('images/classroom/eye_gray.png')
    elif r==3:
        eyes=pygame.image.load('images/classroom/eye_green.png') 
#-skin----------------------------------------------------------------------------------
    r=random.randint(0,8)
    if r==0:
        skin=(255,223,196)
    elif r==1:
        skin=(225,184,153)
    elif r==2:
        skin=(231,158,109)
    elif r==3:
        skin=(165,114,87)    
    elif r==4:
        skin=(92,56,54)
    elif r==5:
        skin=(219,144,101)
    elif r==6:
        skin=(229,194,152)
    elif r==7:
        skin=(173,100,82)
    elif r==8:
        skin=(189,114,60)
#-shirt----------------------------------------------------------------------------------
    r=random.randint(0,8)
    if r==0:
        shirt=(255,102,102)
    elif r==1:
        shirt=(255,178,178)
    elif r==2:
        shirt=(51,255,51)
    elif r==3:
        shirt=(51,153,255)    
    elif r==4:
        shirt=(255,102,255)
    elif r==5:
        shirt=(160,160,160)
    elif r==6:
        shirt=(255,255,51)
    elif r==7:
        shirt=(153,204,255)
    elif r==8:
        shirt=(0,204,102)
#-mouth----------------------------------------------------------------------------------
    r=random.randint(0,9)
    if r==0:
        mouth=pygame.image.load('images/classroom/sad.png')
    elif r<=1:     
        mouth=pygame.image.load('images/classroom/smile.png')
        
def formula():
    r=random.randint(0,2)
    if r==0:
        equation=pygame.image.load('images/classroom/equation1.png')
    elif r==1:
        equation=pygame.image.load('images/classroom/equation2.png')
    elif r==2:
        equation=pygame.image.load('images/classroom/equation3.png')
    screen.blit(equation,(0,-50))

def plane():
    plane=pygame.image.load('images/classroom/plane.png')
    r=random.randint(0,1)
    if r==1:
        plane=pygame.transform.flip(plane, True, False)
    screen.blit(plane,(random.randint(50,1052),random.randint(0,200)))
def pencil():
    pencil=pygame.image.load('images/classroom/pencil.png')
    r=random.randint(0,5)
    if r==0:
        screen.blit(pencil,(600,405))
    elif r==1:
        screen.blit(pencil,(350,405))
    elif r==2:
        screen.blit(pencil,(750,405))
    elif r==3:
        screen.blit(pencil,(450,490))
    elif r==4:
        screen.blit(pencil,(250,490))
    elif r==5:
        screen.blit(pencil,(850,490))
def wall():
    calendar=pygame.image.load('images/classroom/calendar.png')
    #r=random.randint(0,5)
    r=0
    if r==0:
        screen.blit(calendar,(950,180))
    

screen.blit(backimg,(0,0))
wall()
formula()
plane()
a=400
b=300
c=150
for i in range (3):
    for j in range (3):
        randomize()
        kid(a,b)
        a+=c
    if i==0:
        screen.blit(pygame.image.load('images/classroom/back1.png'),(0,0))
        a=250
        b=400
        c=300
    if i==1:
        screen.blit(pygame.image.load('images/classroom/back2.png'),(0,0))
        r=random.randint(0,9)
        for i in range(r):
            pencil()
        a=200
        b=500
        c=400

#kid(400,150)

pygame.display.update()
