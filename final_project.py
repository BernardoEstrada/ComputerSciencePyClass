import pygame, sys, os, shelve
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,600))

#290 coins

world=1

red=(255,0,0)
brickRed=(241,82,14)
green=(0,128,0)
yellow=(255,255,0)
black=(0,0,0)
Grass=pygame.image.load('grass1.png')
blue=(50,100,255)
Barrier=pygame.image.load('barrier.png')
bush=pygame.image.load('bush.png')
sprite=pygame.image.load('front.png')
world_money=0
money=0
keys=pygame.image.load('key.png')
rupee=pygame.image.load('rupee_r.png')
wood_plank=pygame.image.load('wood.png')
rupee_color=[]
walkable_blocks=[0,3,4,5,7,8,9,-1,-2,-5,-6]
a=0
t=0
rad=0
inf=pygame.image.load('info.png')
sunk=False
x=[4,5,8,9,12]
y=[10,10,10,10,10]
up=[False,True,False,True,False]
seconds=0
delay=1.5
game=False
info=False
font=pygame.font.Font('freesansbold.ttf',24)

#---Title screen---------------------------------------
def title():
    global info, event, game
    start=False
    info=False
    while start==False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_RETURN and info==False:
                    start=True
                    game=True
                if event.key==K_i and info==False:
                    info=True
                elif event.key==K_i and info==True:
                    info=False
        if info==True:
            screen.blit(inf,(0,0))
            font=pygame.font.Font('freesansbold.ttf',18)
            grass(640,0)
            grass(600,0)
            screen.blit(font.render(('HS= '+str(highscore)),True,(255,255,255)),(600,5))
 
        else:
            screen.blit(pygame.image.load('start.png'),(0,0)) 
        pygame.display.update()

#---Loose screen---------------------------------------       
def loose():
    global event, game, d, money
    if money>highscore:
        d = shelve.open('score.txt')
        d['score'] = money
        d.close()
    home=False
    while home==False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_RETURN:
                    home=True
                    game=False
        else:
            screen.blit(pygame.image.load('end.png'),(0,0))
            font=pygame.font.Font('freesansbold.ttf',32)
            screen.blit(font.render((str(money)),True,(255,255,255)),(400,450))
        pygame.display.update()

def infor():
    global event, info, font
    if event.type == pygame.KEYDOWN:
        if event.key==K_i:
            info=True
    if event.type == pygame.KEYUP:
        if event.key==K_i:
            info=False
    if info==True:
        screen.blit(inf,(0,0))
        font=pygame.font.Font('freesansbold.ttf',24)
        grass(720,0)
        grass(680,0)
        coin(670,0,0,g=False)
        screen.blit(font.render(('x'+str(money+world_money)),True,(255,255,255)),(700,5))
        
        font=pygame.font.Font('freesansbold.ttf',18)
        grass(640,0)
        grass(600,0)
        screen.blit(font.render(('HS= '+str(highscore)),True,(255,255,255)),(600,5))

    
#--------Creating blocks--------------------------------------------
    #--creates random value (1, 2 or 3) for every space, this defines what color the rupee wull be 
def rupee_randomize():
    for i in range(299):
        rupee_color.append(random.choice([0,1,2]))
        
def coin(x,y,color,g=True):
     if g==True:
         grass(x,y)
     if rupee_color[color]==0:
        rupee=pygame.image.load('rupee_r.png')
     if rupee_color[color]==1:
        rupee=pygame.image.load('rupee_g.png')
     if rupee_color[color]==2:
        rupee=pygame.image.load('rupee_b.png')       
     screen.blit(rupee,(x,y))
def grass(x,y):
     screen.blit(Grass,(x,y))
def river(x,y):
     pygame.draw.rect(screen,blue,(x,y,40,40))    
def lava(x,y):  
     screen.blit(pygame.image.load('lava.png'),(x,y)) 
def barrier(x,y):
     screen.blit(Barrier,(x,y))
def finish(x,y):
     screen.blit(wood_plank,(x,y))
def wood(x,y):
     screen.blit(wood_plank,(x,y))
     if sunk==True:
         s = pygame.Surface((40,40))
         s.set_alpha(150)          
         s.fill((50,100,255))
         screen.blit(s,(x,y))    
def bricks(x,y):
     screen.blit(bush,(x,y))
def key(x,y):
     screen.blit(keys,(x,y))
def player(x,y):
     screen.blit(sprite,(x,y))
def snake(x,y):
     grass(x,y)
     screen.blit(pygame.image.load('enemy2.png'),(x,y))
def button(x,y):
     grass(x,y)
     if sunk==True:
         pygame.draw.rect(screen,(100,100,100),(x+15,y+15,10,10))
     if sunk==False:
         pygame.draw.rect(screen,(50,50,50),(x+15,y+15,10,10))
#--------/Creating blocks/------------------------------------------

#------Generating the world------------------------------------
    #--Lists that define what to draw on the screen---      
def createMaze(): #set up the world as numbers
                  #(-) Makes block treaspasable by user but not enemies (use for testing)
                  #0-grass
                  #1-wall
                  #2 - barrier that could be removed
                  #3-coins
                  #4- key
                  #5- wood
                  #6- river
                  #7- button
                  #8- fire/lava
                  #9- finish
                  #10-snake
     if world==1:
         row0= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#20 x 15 list
         row1= [1,0,0,0,0,0,3,3,3,1,0,1,0,0,0,1,0,1,3,1]
         row2= [1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,3,3,1]
         row3= [1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1]
         row4= [1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1]
         row5= [1,3,1,0,0,1,3,3,3,3,0,1,0,1,0,1,-1,1,0,1]
         row6= [1,3,1,0,0,1,1,1,1,1,-1,1,0,1,0,1,3,1,0,1]
         row7= [1,3,1,1,0,0,3,3,3,3,3,0,0,1,0,1,3,1,0,1]
         row8= [1,3,3,-1,0,3,3,3,3,3,3,3,0,-1,0,3,3,-1,4,1]
         row9= [1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1]
         row10=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
         row11=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
         row12=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
         row13=[1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
         row14=[1,1,9,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
         
     if world==2:
         row0= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
         row1= [1,0,0,0,0,0,0,0,0,0,6,0,0,3,3,3,3,3,3,1]
         row2= [1,0,0,0,3,0,3,0,3,0,6,6,0,3,3,3,3,3,3,1]
         row3= [1,0,0,0,0,3,3,0,3,3,3,6,6,6,0,3,3,3,3,1]
         row4= [1,0,0,0,3,3,0,3,3,0,0,0,0,5,0,3,3,3,3,1]
         row5= [1,0,0,0,0,0,3,0,0,0,3,0,0,6,6,0,3,3,3,1]
         row6= [1,0,0,0,3,3,0,3,0,3,0,0,0,0,-6,0,0,8,4,1]
         row7= [1,0,0,1,1,1,1,1,1,1,1,1,1,-1,-6,1,1,1,1,1]
         row8= [1,0,3,0,0,0,0,0,0,0,0,0,0,-2,-6,3,3,3,3,1]
         row9= [1,3,0,0,0,0,0,0,0,0,0,0,0,2,6,3,3,3,3,1]
         row10=[1,0,3,0,0,0,0,0,0,0,0,0,0,2,6,3,3,3,3,1]
         row11=[1,3,0,0,0,0,0,0,0,0,0,0,0,2,5,3,3,3,3,1]
         row12=[1,8,8,0,0,0,0,0,0,0,0,0,0,2,6,3,3,3,3,9]
         row13=[1,7,3,0,0,0,0,0,0,0,0,0,0,2,6,3,3,3,3,9]
         row14=[1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1]
         
     if world==3:
         row0= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#20 x 15 list
         row1= [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1]
         row2= [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,1]
         row3= [1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,3,1]
         row4= [1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,3,1]
         row5= [1,0,3,3,3,3,3,0,0,0,0,0,0,1,0,1,0,1,3,1]
         row6= [1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,3,1]
         row7= [1,3,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,3,1]
         row8= [1,3,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1]
         row9= [1,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,9]
         row10=[1,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,9]
         row11=[1,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,9]
         row12=[1,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,9]
         row13=[1,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,9]
         row14=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

     maze = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14]
     return maze
#-------draw the world changing the numbers to images----------
def drawMaze(maze): 
     for j in range(20):
          for i  in range(15):
               maze[i][j]=abs(maze[i][j]) #turns off testing treaspasable blocks (should be uncommented)
               x=j*40
               y=i*40
               if abs(maze[i][j]) == 1 :
                    bricks(x,y)
               elif abs(maze[i][j]) == 2:
                    barrier(x,y)
               elif maze[i][j] == 3:
                    coin(x,y,((i+1)*(j+1)))
               elif maze[i][j] == 4:
                    grass(x,y)
                    key(x,y)
               elif abs(maze[i][j]) == 5:
                    wood(x,y)
               elif abs(maze[i][j]) == 6:
                    river(x,y)
               elif maze[i][j] == 7:
                    button(x,y)
               elif maze[i][j] == 8:
                    lava(x,y)
               elif maze[i][j] == 9:
                    finish(x,y)
               elif maze[i][j] == 10:
                    snake(x,y)
               elif maze[i][j] == 0:
                    grass(x,y)
 
#-----------------player movement--------------------------------------                   
def move():
    global row, column, event, walkable_blocks, sprite

    #adds or removes sunken bridge from walkable blocks
    if 5 in walkable_blocks and sunk==True:
        walkable_blocks.remove(5) 
    if 5 not in walkable_blocks and sunk==False:
        walkable_blocks.append(5)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN and maze[row][column]!=9:
            if (event.key==K_UP or event.key==K_w) and (maze[row-1][column] in walkable_blocks):
                sprite=pygame.image.load('back.png')
                row=row-1
            if (event.key==K_DOWN or event.key==K_s) and (maze[row+1][column] in walkable_blocks):
                sprite=pygame.image.load('front.png')
                row=row+1
            if (event.key==K_LEFT or event.key==K_a) and (maze[row][column-1] in walkable_blocks):
                sprite=pygame.image.load('side.png')
                sprite=pygame.transform.flip(sprite,True,False)
                column=column-1
            if (event.key==K_RIGHT or event.key==K_d) and (maze[row][column+1] in walkable_blocks):
                sprite=pygame.image.load('side.png')
                column=column+1

#-------------------Enemy movement------------------------------------
def enemy():
    global x, y, up, row, column, event
    if world==2 and len(x)==len(y):
        for i in range(5):
            if abs(maze[y[i]-1][x[i]]) not in walkable_blocks:
                if up[i]==True:
                    x[i]+=1
                up[i]=False
            if abs(maze[y[i]+1][x[i]]) not in walkable_blocks:
                if up[i]==False:
                    x[i]-=1
                up[i]=True
            if seconds==0:
                if up[i]==False:
                    y[i]+=1
                elif up[i]==True:
                    y[i]-=1
            screen.blit(pygame.image.load('enemy3.png'),(x[i]*40,y[i]*40))
            if row==y[i] and column==x[i]:
                die()
    if world==3:
        for i in range(5):
            maze[y[i]][x[i]]=0
            if event.type==KEYDOWN:
                if column>x[i] and (maze[y[i]][x[i]+1] in walkable_blocks) and (maze[y[i]][x[i]+1]!=8):
                    x[i]+=1
                if column<x[i] and (maze[y[i]][x[i]-1] in walkable_blocks) and (maze[y[i]][x[i]-1]!=8):
                    x[i]-=1
                if row>y[i] and (maze[y[i]+1][x[i]] in walkable_blocks) and (maze[y[i]+1][x[i]]!=8):
                    y[i]+=1
                if row<y[i] and (maze[y[i]-1][x[i]] in walkable_blocks) and (maze[y[i]-1][x[i]]!=8):
                    y[i]-=1
            maze[y[i]][x[i]]=10      
        for i in range(5,13):
            if abs(maze[y[i]-1][x[i]]) not in walkable_blocks:
                up[i]=False
            if abs(maze[y[i]+1][x[i]]) not in walkable_blocks:
                up[i]=True
            if seconds==0 or seconds==15:
                if up[i]==False:
                    y[i]+=1
                elif up[i]==True:
                    y[i]-=1
            if seconds<15:
                if up[i]==True:
                    screen.blit(pygame.image.load('enemy1b.png'),(x[i]*40,(y[i]*40-int(seconds*40/15))))
                if up[i]==False:
                    screen.blit(pygame.image.load('enemy1b.png'),(x[i]*40,(y[i]*40+int(seconds*40/15))))
            if seconds>=15:
                if up[i]==True:
                    screen.blit(pygame.image.load('enemy1a.png'),(x[i]*40,(y[i]*40-int((seconds-15)*40/15))))
                if up[i]==False:
                    screen.blit(pygame.image.load('enemy1a.png'),(x[i]*40,(y[i]*40+int((seconds-15)*40/15))))
            if row==y[i] and column==x[i]:
                die()
                
    if maze[row][column]==5 and sunk==True:
        die()
    if maze[row][column]==8 or maze[row][column]==10:
        die()

#--------kills player, returns to start and takes away coins colected in the world + 5 -----
def die():
    global row, column, maze, world_money, money, sunk,rupee_color,x,y, up
    sunk=True
    rupee_color=[]
    rupee_randomize()
    row=1
    column=1
    if world==3: 
        column=8              
        x=[6,7,8,9,10,3,4,5,6,7,8,9,10]
        y=[7,7,7,7,7,13,7,12,8,11,9,10,10]
        up=[False,True,False,True,False,True,False,True,False,True,False,True,False]
    world_money=0
    money=money-5
    maze=createMaze()

#---picks coins and adds them to 'world money' so that if the player dies this can be set to 0--    
def pick_coins():
    global world_money
    grass(720,0)
    grass(680,0)
    coin(670,0,0,g=False)
    screen.blit(font.render(('x'+str(money+world_money)),True,(255,255,255)),(700,5))
    if maze[row][column] == 3:
        maze[row][column]=0
        world_money+=1
        print(money+world_money)
        
#--makes specific barriers disappear when keys are picked and bridges unsink when buttons pressed--        
def actuators():
    global sunk, maze, t
    if maze[row][column] == 4 and world==1:
          maze[row][column]=0
          maze[9][9]=0
          maze[9][10]=0
    if maze[row][column] == 4 and world==2:
          maze[row][column]=0
          maze[8][13]=0
          maze[9][13]=0
          maze[10][13]=0
          maze[11][13]=0
          maze[12][13]=0
          maze[13][13]=0
    if maze[row][column] == 7:
         sunk=False
    if sunk==False and world!=1:
         t+=1
         if t==delay*500:
             sunk=True
             t=0
#--Changes world when on ending block--
def world_transition():
     global Grass, game, x, y, maze, a, world, rupee_color, world_money, money, row, column, sunk, rad, up
     if world==4:
         game=False
     if maze[row][column] == 9:
          if a<=20:
              rad+=30
              pygame.draw.circle(screen, black, (400,300),rad)
              a+=1         
          else:   
              world+=1
              if world!=4:
                  Grass=pygame.image.load('grass2.png')
                  rupee_color=[]
                  rupee_randomize()
                  maze=createMaze()
              money=world_money+money
              world_money=0
              row=1 
              column=1
              sunk=True
              if world==3:
                 Grass=pygame.image.load('grass3.png') 
                 column=8              
                 x=[6,7,8,9,10,3,4,5,6,7,8,9,10]
                 y=[7,7,7,7,7,13,7,12,8,11,9,10,10]
                 up=[False,True,False,True,False,True,False,True,False,True,False,True,False]

     elif a<=40 and a>20:
          rad-=30
          pygame.draw.circle(screen, black, (400,300),rad)
          a+=1
          if a==40:
              a=0

def reset_variables():
    global world, money, world_money, grass, row, column, walkable_blocks, a, t, rad, sunk, x, y, up
    world=1
    row=1
    column=10
    money=0
    world_money=0
    walkable_blocks=[0,3,4,5,7,8,9,-1,-2,-5,-6]
    a=0
    t=0
    rad=0
    Grass=pygame.image.load('grass1.png') 
    sunk=False
    x=[4,5,8,9,12]
    y=[10,10,10,10,10]
    up=[False,True,False,True,False]
    
#=======/Functions/======================================================================


#=======Game Loop========================================================================
while True:
    d = shelve.open('score.txt')
    highscore= d['score']
    d.close()
    reset_variables()
    title()
    rupee_randomize()
    row=1  #starting location of the player in the maze
    column=10
    maze=createMaze()
    pygame.key.set_repeat(500,70)
    while game==True:
        #-Counter-
         if seconds <30:
             seconds+=1
         else:
             seconds=0 
         move()
         screen.fill(black)
         drawMaze(maze)
         enemy()
         player(column*40,row*40)
         pick_coins()
         actuators()
         world_transition()
         #print('you have ',world_money+money)
         infor()
         pygame.display.update()
    loose()

