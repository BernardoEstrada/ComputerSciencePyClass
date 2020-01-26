import pygame, sys
from pygame.locals import *
import random
pygame.init()

brown=(109,39,39)
black=(0,0,0)
sky=(0,104,104)
green=(0,50,0)
grass=(0,100,0)
white=(255,255,255)
blue=(100,100,255)
gray=(128,128,128)

screen=pygame.display.set_mode((600,500))#----screen size
screen.fill((sky))#----screen color
#----------Functions------------------------------------------------
#Tree
def tree(size,positionX,positionY):
    pygame.draw.polygon(screen,green,[[positionX,positionY+(17*size)],[positionX-(30*size),positionY+45*size],[positionX+(30*size),positionY+45*size]])#3rd triangle    
    pygame.draw.polygon(screen,black,[[positionX,positionY+(17*size)],[positionX-(30*size),positionY+45*size],[positionX+(30*size),positionY+45*size]],3)
    pygame.draw.polygon(screen,green,[[positionX,positionY+(7*size)],[positionX-(25*size),positionY+30*size],[positionX+(25*size),positionY+30*size]])#2nd triangle
    pygame.draw.polygon(screen,black,[[positionX,positionY+(7*size)],[positionX-(25*size),positionY+30*size],[positionX+(25*size),positionY+30*size]],3)
    pygame.draw.polygon(screen,green,[[positionX,positionY],[positionX-(20*size),positionY+(15*size)],[positionX+(20*size),positionY+(15*size)]])#1st triangle
    pygame.draw.polygon(screen,black,[[positionX,positionY],[positionX-(20*size),positionY+(15*size)],[positionX+(20*size),positionY+(15*size)]],3)
    pygame.draw.rect(screen,brown,[positionX-(10*size),(positionY+(45*size)),20*size,30*size])#trunk
    pygame.draw.rect(screen,black,[positionX-(10*size),(positionY+(45*size)),20*size,30*size],3)
#Star
def star(size,posx,posy):
    pygame.draw.circle(screen,white,(posx,posy),size)
#Moon
def moon(diffx,diffy,posx,posy,size):
    pygame.draw.circle(screen,white,(posx,posy),size)
    pygame.draw.circle(screen,sky,(posx-diffx,posy-diffy),size)
#Fish
def fish(posX,posY,r,g,b):
    pygame.draw.circle(screen,(r,g,b),(posX,posY),4)
    pygame.draw.polygon(screen,(r,g,b),[[posX-4,posY],[posX-6,posY+4],[posX-6,posY-4]])
#Mountains
def mountain():
    pygame.draw.polygon(screen,gray,[[300,20],[250,60],[350,60]])#mountain1
    pygame.draw.polygon(screen,white,[[300,20],[275,40],[325,40]])#snow
    pygame.draw.polygon(screen,gray,[[250,30],[200,60],[300,60]])#mountain2
    pygame.draw.polygon(screen,white,[[250,30],[225,45],[275,45]])#snow
    pygame.draw.polygon(screen,gray,[[350,40],[300,60],[400,60]])#mountain3
    pygame.draw.polygon(screen,white,[[350,40],[325,50],[375,50]])#snow
#----------------------------------------------------------------------------

pygame.draw.rect(screen,grass,[0,60,600,500])#Grass

for i in range (random.randint(0,200)):
    star(random.randint(2,2),random.randint(0,600),random.randint(0,50))
    
moon(random.randint(-40,40),random.randint(-40,40),random.randint(200,450),random.randint(0,40),random.randint(10,40))
mountain()
pygame.draw.rect(screen,grass,[0,60,600,500])#Grass

for i in range (10,30):#Tree generation 1
    green=(0,random.randint(50,150),0)
    tree(random.uniform(i/20,i/50),random.randint(10,590),random.randint((i*4),(i*5)))
    
for i in range (10,60):#Tree generation 2
    green=(0,random.randint(50,150),0)
    tree(random.uniform(i/20,i/50),random.randint(10,590),random.randint((i*4),(i*5)))
    
pygame.draw.ellipse(screen,blue,[-100,430,800,200])#pond
pygame.draw.ellipse(screen,gray,[-100,430,800,200],10)#shore

for i in range(30): #Fish 1
    fish(random.randint(50,550),random.randint(470,500),random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
for i in range(10): #Fish 2
    fish(random.randint(200,400),random.randint(445,470),random.randint(0,255),random.randint(0,255),random.randint(0,255))

pygame.display.update()
