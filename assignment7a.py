import pygame, sys
from pygame.locals import *

background=(0,0,0)
color1=(255,0,0)
color2=(255,0,255)
color3=(0,255,0)
color4=(0,255,255)
color5=(255,255,0)
color6=(255,255,255)

pygame.init()
screen=pygame.display.set_mode((600,500))
screen.fill(background)
pygame.draw.rect(screen,color1,(10,10,200,100))
pygame.draw.polygon(screen,color2,[[10,120],[10,320],[150,320],[150,120]])
pygame.draw.polygon(screen,color3,[[10,120],[10,320],[210,320]])
pygame.draw.rect(screen,color4,(220,10,100,100))
pygame.draw.circle(screen,color5,(270,170),50)
pygame.draw.polygon(screen,color6,[[110,330],[10,380],[110,430],[210,380]])


pygame.display.update()

