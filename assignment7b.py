import pygame, sys
from pygame.locals import *

black=(0,0,0)
white=(255,255,255)
gray=(50,50,50)
blue=(0,0,255)
sky=(0,204,204)
skin=(255,204,153)
red=(204,0,0)


pygame.init()
screen=pygame.display.set_mode((600,500))#----screen size
screen.fill((sky))#----screen color
pygame.draw.circle(screen,skin,(270,100),50,5)#----head
pygame.draw.line(screen,red,[270,150],[270,250],5)#----body
pygame.draw.line(screen,skin,[270,150],[270,160],5)#----neck
pygame.draw.line(screen,blue,[270,250],[320,350],5)#----right leg
pygame.draw.line(screen,blue,[270,250],[220,350],5)#----left leg
pygame.draw.line(screen,red,[270,170],[340,230],5)#----right arm
pygame.draw.line(screen,red,[270,170],[200,230],5)#----left arm

pygame.draw.rect(screen,gray,(0,350,600,150))#----road


pygame.display.update()
