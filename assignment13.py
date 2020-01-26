import pygame, sys
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,600))

red=(255,0,0)
brickRed=(241,82,14)
green=(0,128,0)
yellow=(255,255,0)
black=(0,0,0)
Grass=(30,155,30)
Barrier=pygame.image.load('barrier.png')
bush=pygame.image.load('bush.png')
sprite=pygame.image.load('link.gif')
money=0
keys=pygame.image.load('key.png')

def coin(x,y):
     pygame.draw.rect(screen,Grass,(x,y,40,40))
     pygame.draw.circle(screen,yellow,(x+20,y+20),5)
     pygame.draw.rect(screen,Grass,(x,y,40,40),2)

def grass(x,y):
     pygame.draw.rect(screen,Grass,(x,y,40,40))
     pygame.draw.rect(screen,Grass,(x,y,40,40),2)
     
def barrier(x,y):
     screen.blit(Barrier,(x,y))
     
def bricks(x,y):
     screen.blit(bush,(x,y))

def key(x,y):
     screen.blit(keys,(x,y))

def player(x,y):
     screen.blit(sprite,(x,y))
     
def createMaze(): #set up the world as numbers
                  #0-grass
                  #1-wall
                  #2 - barrier that could be removed
                  #3-coins
                  #4- key

     row0= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#20 x 15 list
     row1= [1,0,0,0,0,0,3,3,3,1,0,1,0,0,0,1,0,1,3,1]
     row2= [1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,3,3,1]
     row3= [1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1]
     row4= [1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1]
     row5= [1,3,1,0,0,1,3,3,3,3,0,1,0,1,0,1,1,1,0,1]
     row6= [1,3,1,0,0,1,1,1,1,1,1,1,0,1,0,1,3,1,0,1]
     row7= [1,3,1,1,0,0,3,3,3,3,3,0,0,1,0,1,3,1,0,1]
     row8= [1,3,3,1,0,3,3,3,3,3,3,3,0,1,0,3,3,1,4,1]
     row9= [1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1]
     row10=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
     row11=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
     row12=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
     row13=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
     row14=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

     maze = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14]
     return maze
def drawMaze(maze): # draw the maze changing the numbers to images
     for j in range(20):
          for i  in range(15):
               x=j*40
               y=i*40
               if maze[i][j] == 1 :
                    bricks(x,y)
               elif maze[i][j] == 2:
                    barrier(x,y)
               elif maze[i][j] == 3:
                    coin(x,y)
               elif maze[i][j] == 4:
                    grass(x,y)
                    key(x,y)
               elif maze[i][j] == 0:
                    grass(x,y)
                 
row=1  #starting location of the player in the maze
column=10
maze=createMaze()
#===============================================================================
pygame.key.set_repeat(500,70)
while True:
     for event in pygame.event.get():
          if event.type==QUIT:
               pygame.quit()
               sys.exit()
#=============== player movement   =======================================
          if event.type==KEYDOWN:
               if (event.key==K_UP or event.key==K_w) and (maze[row-1][column] in [0,3,4]):
                    row=row-1
               if (event.key==K_DOWN or event.key==K_s) and (maze[row+1][column] in [0,3,4]):
                    row=row+1
               if (event.key==K_LEFT or event.key==K_a) and (maze[row][column-1] in [0,3,4]):
                    column=column-1
               if (event.key==K_RIGHT or event.key==K_d) and (maze[row][column+1] in [0,3,4]):
                    column=column+1
#===============end of player
     if maze[row][column] == 3:
          maze[row][column]=0
          money+=1
          print(money)
          
     if maze[row][column] == 4:
          maze[row][column]=0
          maze[9][9]=0
          maze[9][10]=0
     
     screen.fill(black)
     drawMaze(maze)
     player(column*40,row*40)
     pygame.display.update()
