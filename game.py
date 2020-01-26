import pygame, sys, random, math, os, shelve
from pygame.locals import *

d = shelve.open('images/game/score.txt')
highscore= 0
d.close()

pygame.init()
FPS=60#frames per second
fpsClock=pygame.time.Clock()

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen=pygame.display.set_mode((1152,720),0,32)

font=pygame.font.Font('freesansbold.ttf',30)
text=font.render('x15',True,(255,255,255))
tank=pygame.image.load('images/game/tank_b.png')
car=pygame.image.load('images/game/car.png')
bullet=pygame.image.load('images/game/bullet.png')
bomb=pygame.image.load('images/game/bomb.png')
explosion1=pygame.image.load('images/game/transparent.png')
explosion2=pygame.image.load('images/game/transparent.png')
explosion3=pygame.image.load('images/game/transparent.png')
bullet1=pygame.transform.rotate(bullet,0)
bullet2=pygame.transform.rotate(bullet,0)
bullet3=pygame.transform.rotate(bullet,0)
tank2=pygame.image.load('images/game/tank_t.png')
tank3=pygame.transform.rotate(tank2,0)
pygame.display.set_caption('Game')
heart=pygame.image.load('images/lives/4.png')
backimg=pygame.image.load('images/game/titlescreen.png').convert()

pygame.key.set_repeat(1,50)
carx=1152
cary=random.randint(40,700)
car1x=1152
car1y=random.randint(40,700)
car2x=1152
car2y=random.randint(40,700)
angle=0
angle_b=0
angle_b2=0
angle_b3=0
lives=4
tankx=100
tanky=100
bulletx=500
bullety=450
objx=0
objy=0
bullet2x=520
bullet2y=450
obj2x=0
obj2y=0
bullet3x=540
bullet3y=450
obj3x=0
obj3y=0
shooting=False
shooting2=False
shooting3=False
exploding1=False
exploding2=False
exploding3=False
bombx=2000
bomby=0
bomb2x=2000
bomb2y=0
bomb3x=2000
bomb3y=0
a=0
b=0
c=0
f=0
cars_destroyed=0


#----\\\\\\\\\\\\\\\\\\\\------------------------------------>
#----Functions start here------------------------------------->
#----////////////////////------------------------------------>

#---Title screen---------------------------------------
def title():
    global event, backimg, game, highscore, d
    d = shelve.open('images/game/score.txt')
    highscore= d['score']
    d.close()
    start=False
    info=False
    while start==False:
        for event in pygame.event.get():
            mx,my=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and mx>=412 and mx<=740 and my>400 and my<570 and info==False:
                start=True
                game=True
            if event.type == pygame.MOUSEBUTTONDOWN and mx>=995 and mx<=1115 and my>540 and my<680 and info==False:
                info=True
            elif event.type == pygame.MOUSEBUTTONDOWN and mx>=995 and mx<=1115 and my>540 and my<680 and info==True:
                info=False
            elif event.type == pygame.MOUSEBUTTONDOWN and mx>=1028 and mx<=1110 and my>62 and my<160 and info==True:   
                d = shelve.open('images/game/score.txt')
                d['score'] = 0
                highscore= d['score']
                d.close()
        if info==True:
            backimg=pygame.image.load('images/game/info.png').convert()
        else:
            backimg=pygame.image.load('images/game/titlescreen.png').convert()
        screen.blit(backimg,(0,0)) 
        text=font.render(("Highscore: " + str(highscore)),True,(0,0,0))
        screen.blit(text,(900,5))
        pygame.display.update()
    backimg=pygame.image.load('images/game/background.png').convert()

#---Reads inputs (mouse click, keyboard press, etc.)-------------------------------
def inputs():
    global tankx, tanky, angle, event
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot()
        if event.type==KEYDOWN:
            move()

#---Speeds up the whole game by one frame every second---------------------------------------
def speed_up():
    global FPS, f
    f+=1
    if f==(FPS):
        FPS+=1
        f=0

#---Changes "lives" image to show the lives left-----------------------------------
def live():
    global lives, heart, cars_destroyed, game
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
        game=False

#---Makes tank rotate while staying centered---------------------------------------
def rot_center(image, angle):
    if angle>=-80:
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    else:
        return image
        
#---Tracks mouse movement and changes tank and bullet angle------------------------
def mouse_track():
    global tankx, tanky, angle, angle_b, tank2, tank3, bullet, bullet1, bullet2, bullet3, shooting, shooting2,shooting3,bulletx,bullety,bullet2x,bullet2y,bullet3x,bullet3y
    mousex,mousey=pygame.mouse.get_pos()
    if mousex-tankx+50>50:
        angle= math.degrees(math.atan((tanky+50-mousey)/(mousex+50-tankx)))
        angle_b= math.degrees(math.atan((tanky+50-mousey)/(mousex+50-tankx)))
    tank3=rot_center(tank2,angle)
    if shooting==False:
        bullet1=rot_center(bullet,angle_b)
        bulletx=tankx+50-6
        bullety=tanky+50-6
    if shooting2==False:
        bullet2=rot_center(bullet,angle_b)
        bullet2x=tankx+50-6
        bullet2y=tanky+50-6
    if shooting3==False:
        bullet3=rot_center(bullet,angle_b)
        bullet3x=tankx+50-6
        bullet3y=tanky+50-6

#---Makes tank go up and down------------------------------------------------------
def move():
    global tankx, tanky, angle
    if event.key==K_UP or event.key==K_w:
        if tanky>=15:
            tanky=tanky-10
    elif event.key==K_DOWN or event.key==K_s:
        if tanky<=605:
            tanky=tanky+10
    if event.key==K_SPACE:
        pygame.key.set_repeat(0,0)
        shoot()
        pygame.key.set_repeat(1,50)

#---Makes bullet go to the tank when user clicks mouse and triggers bullet_move----
def shoot():
    global tankx,tanky,angle,bullet,bulletx,bullety,bullet2x,bullet2y,bullet3x,bullet3y,objx,objy,obj2x,obj2y,obj3x,obj3y,shooting,shooting2,shooting3
    mousex,mousey=pygame.mouse.get_pos()
    if shooting==False:
        bulletx=tankx+50-6
        bullety=tanky+50-6
        objx=mousex+50-tankx
        objy=tanky+50-mousey
        shooting=True
    elif shooting2==False:
        bullet2x=tankx+50-6
        bullet2y=tanky+50-6
        obj2x=mousex+50-tankx
        obj2y=tanky+50-mousey
        shooting2=True
    elif shooting3==False:
        bullet3x=tankx+50-6
        bullet3y=tanky+50-6
        obj3x=mousex+50-tankx
        obj3y=tanky+50-mousey
        shooting3=True

#---Makes bullet move to where mouse was clicked-----------------------------------
def bullet_move():
    global tankx,tanky,angle,bullet,bulletx,bullety,bullet2x,bullet2y,bullet3x,bullet3y,objx,objy,obj2x,obj2y,obj3x,obj3y,shooting,shooting2,shooting3
    if shooting==True:
        bulletx=bulletx+(objx/100)
        bullety=bullety-(objy/100)
    if shooting2==True:
        bullet2x=bullet2x+(obj2x/100)
        bullet2y=bullet2y-(obj2y/100)
    if shooting3==True:
        bullet3x=bullet3x+(obj3x/100)
        bullet3y=bullet3y-(obj3y/100)
    if bulletx>1152 or bullety>720 or bullety<-20:
        shooting=False
    if bullet2x>1152 or bullet2y>720 or bullet2y<-20:
        shooting2=False
    if bullet3x>1152 or bullet3y>720 or bullet3y<-20:
        shooting3=False

#---Moves car and destroy when touching bullet---------------------------------------
def car_move():
    global f, FPS, cars_destroyed, car, carx, cary, car1x, car1y, car2x, car2y, tanky, tankx, lives, bulletx, bullety, bullet2x, bullet2y, bullet3x, bullet3y, shooting, shooting2, shooting3
    if lives>0:
    #Detect collisions of car 0
        if carx>-36:
            carx-=2
        else:
            carx=random.randint(1152,1500)
            cary=random.randint(40,700)
        if math.hypot(((tankx+50)-(carx+37)),((tanky+50)-(cary+21)))<30:
            carx=random.randint(1152,1500)
            cary=random.randint(40,700)
            lives-=1
        if math.hypot(((bulletx+6)-(carx+37)),((bullety+5)-(cary+21)))<30:
            carx=random.randint(1152,1500)
            cary=random.randint(40,700)
            cars_destroyed+=1
            shooting=False
        if math.hypot(((bullet2x+6)-(carx+37)),((bullet2y+5)-(cary+21)))<30:
            carx=random.randint(1152,1500)
            cary=random.randint(40,700)
            cars_destroyed+=1
            shooting2=False
        if math.hypot(((bullet3x+6)-(carx+37)),((bullet3y+5)-(cary+21)))<30:
            carx=random.randint(1152,1500)
            cary=random.randint(40,700)
            cars_destroyed+=1
            shooting3=False
    #Detect collisions of car 1
        if car1x>-36:
            car1x-=2
        else:
            car1x=random.randint(1152,1500)
            car1y=random.randint(40,700)
        if math.hypot(((tankx+50)-(car1x+37)),((tanky+50)-(car1y+21)))<30:
            car1x=random.randint(1152,1500)
            car1y=random.randint(40,700)
            lives-=1
        if math.hypot(((bulletx+6)-(car1x+37)),((bullety+5)-(car1y+21)))<30:
            car1x=random.randint(1152,1500)
            car1y=random.randint(40,700)
            cars_destroyed+=1
            shooting=False
        if math.hypot(((bullet2x+6)-(car1x+37)),((bullet2y+5)-(car1y+21)))<30:
            car1x=random.randint(1152,1500)
            car1y=random.randint(40,700)
            cars_destroyed+=1
            shooting2=False
        if math.hypot(((bullet3x+6)-(car1x+37)),((bullet3y+5)-(car1y+21)))<30:
            car1x=random.randint(1152,1500)
            car1y=random.randint(40,700)
            cars_destroyed+=1
            shooting3=False
    #Detect collisions of car 2
        if car2x>-36:
            car2x-=2
        else:
            car2x=random.randint(1152,1500)
            car2y=random.randint(40,700)
        if math.hypot(((tankx+50)-(car2x+37)),((tanky+50)-(car2y+21)))<30:
            car2x=random.randint(1152,1500)
            car2y=random.randint(40,700)
            lives-=1
        if math.hypot(((bulletx+6)-(car2x+37)),((bullety+5)-(car2y+21)))<30:
            car2x=random.randint(1152,1500)
            car2y=random.randint(40,700)
            cars_destroyed+=1
            shooting=False
        if math.hypot(((bullet2x+6)-(car2x+37)),((bullet2y+5)-(car2y+21)))<30:
            car2x=random.randint(1152,1500)
            car2y=random.randint(40,700)
            cars_destroyed+=1
            shooting2=False
        if math.hypot(((bullet3x+6)-(car2x+37)),((bullet3y+5)-(car2y+21)))<30:
            car2x=random.randint(1152,1500)
            car2y=random.randint(40,700)
            cars_destroyed+=1
            shooting3=False
    #---Drops Bomb after Reaching tank---------------
        if carx+75<=tankx+50:
            bomb_drop(0)
            FPS=60
            f=0
        if car1x+75<=tankx+50:
            bomb_drop(1)
            FPS=60
            f=0
        if car2x+75<=tankx+50:
            bomb_drop(2)
            FPS=60 
            f=0
    #---Returns car after exiting the screen----------
        if carx+75<tankx:
            carx=random.randint(1152,1500)
            cary=random.randint(40,700)
        if car1x+75<tankx:
            car1x=random.randint(1152,1500)
            car1y=random.randint(40,700)
        if car2x+75<tankx:
            car2x=random.randint(1152,1500)
            car2y=random.randint(40,700)
            
#---Triggers dropping bomb when car reaches tank---------------------------------------
def bomb_drop(car):
    global bombx, bomby, bomb2x, bomb2y, bomb3x, bomb3y, exploding1, exploding2, exploding3, a, b, c, explosion1
    if car==0:
        bombx=carx+75-22
        bomby=cary+21-12
        a=0
        exploding1=True
        explosion1=pygame.image.load('images/game/transparent.png')
    if car==1:
        bomb2x=car1x+75-12
        bomb2y=car1y+21-22
        b=0
        exploding2=True
        explosion2=pygame.image.load('images/game/transparent.png')
    if car==2:
        bomb3x=car2x+75-12
        bomb3y=car2y+21-22
        c=0
        exploding3=True
        explosion3=pygame.image.load('images/game/transparent.png')
        
#---Animates the explosion and removes a life---------------------------------------
def explosion():
    global a, b, c, bombx, bomb2x, bomb3x, explosion1, explosion2, explosion3, exploding1, exploding2, exploding3, lives
    if exploding1==True:
        a+=1
        if a==60:
            explosion1=pygame.image.load('images/game/explosion1.png')
        if a==75:
            explosion1=pygame.image.load('images/game/explosion2.png')
        if a==90:
            explosion1=pygame.image.load('images/game/explosion3.png')
        if a==110:
            lives-=1   
            explosion1=pygame.image.load('images/game/transparent.png')
            bombx=2000
            exploding1=False
            a=0
    if exploding2==True:
        b+=1
        if b==60:
            explosion2=pygame.image.load('images/game/explosion1.png')
        if b==75:
            explosion2=pygame.image.load('images/game/explosion2.png')
        if b==90:
            explosion2=pygame.image.load('images/game/explosion3.png')
        if b==110:
            lives-=1   
            explosion2=pygame.image.load('images/game/transparent.png')
            bomb2x=2000
            exploding2=False
            b=0
    if exploding3==True:
        c+=1
        if c==60:
            explosion3=pygame.image.load('images/game/explosion1.png')
        if c==75:
            explosion3=pygame.image.load('images/game/explosion2.png')
        if c==90:
            explosion3=pygame.image.load('images/game/explosion3.png')
        if c==110:
            lives-=1                
            explosion3=pygame.image.load('images/game/transparent.png')
            bomb3x=2000
            exploding3=False
            c=0
 
#---Loose screen---------------------------------------       
def loose():
    global event, backimg, game
    home=False
    refresh()
    while home==False:
        for event in pygame.event.get():
            mx,my=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and mx>=412 and mx<=740 and my>400 and my<570:
                home=True
                game=False
        else:
            backimg=pygame.image.load('images/game/you_lost.png').convert()
        screen.blit(backimg,(288,180))
        pygame.display.update()

#---Refresh the screen-------------------------------------------------------------
def refresh():
    screen.fill((100,100,100))    
    screen.blit(backimg,(0,0))
    screen.blit(bomb,(bombx,bomby))
    screen.blit(bomb,(bomb2x,bomb2y))
    screen.blit(bomb,(bomb3x,bomb3y))
    screen.blit(tank,(tankx,tanky))
    screen.blit(car,(carx,cary))
    screen.blit(car,(car1x,car1y))
    screen.blit(car,(car2x,car2y))
    screen.blit(bullet1,(bulletx,bullety))
    screen.blit(bullet2,(bullet2x,bullet2y))
    screen.blit(bullet3,(bullet3x,bullet3y))
    screen.blit(tank3,(tankx,tanky))
    screen.blit(explosion1,(bombx-49,bomby-49))
    screen.blit(explosion2,(bomb2x-49,bomb2y-49))
    screen.blit(explosion3,(bomb3x-49,bomb3y-49))
    screen.blit(heart,(485,5))
    screen.blit(car,(1000,0))
    text=font.render(("x " + str(cars_destroyed)),True,(255,255,0))
    screen.blit(text,(1080,5))
    text=font.render(("Highscore: " + str(highscore)),True,(255,255,0))
    screen.blit(text,(750,5))
    pygame.display.update()
    fpsClock.tick(FPS)

#----\\\\\\\\\\\\\\\\\\-------------------------------------->
#----Functions end here--------------------------------------->
#----//////////////////-------------------------------------->

game=True

while True:
    title()
    #--Reset variables and locations--
    lives=4
    carx=random.randint(1152,1500)
    car1x=random.randint(1152,1500)
    car2x=random.randint(1152,1500) 
    cars_destroyed=0
    f=0 
    FPS=60
    d = shelve.open('images/game/score.txt')
    highscore= d['score']
    d.close()
    while game==True: #---game loop---
        live()
        mouse_track()
        inputs()
        bullet_move()
        car_move()
        explosion()
        speed_up()
        refresh()
    d = shelve.open('images/game/score.txt')
    if d['score'] < cars_destroyed:
        d['score'] = cars_destroyed  
        highscore= d['score']
    d.close()
    loose()
