import pygame, sys, random, time
from pygame.locals import *
pygame.init()

speed=1

loop=0
loopB=0
imgx=50
imgy=220
carx=273
cary=215 
position=1
move=0
brown=(109,39,39)
black=(0,0,0)
sky=(0,104,104)
green=(0,50,0)
frame=1
car_width=39
car_height=25

screen=pygame.display.set_mode((800,542),0,32)
img=pygame.image.load('images/animation/1.png')
img2=pygame.transform.rotate(img, 90)
ampelmann=pygame.image.load('images/ampelmann-green.png')
car=pygame.image.load('images/car.png')
car=pygame.transform.smoothscale(car, (car_width,car_height))
pygame.display.set_caption('Animation')
backimg=pygame.image.load('images/sign-yellow.png')
font=pygame.font.Font('freesansbold.ttf',24)
text=font.render('a',True,black)
button=pygame.image.load('images/button.png')

def walk(distance, text_move=0, speed=1, car_move=0, button=0):
    global frame, img, img2, imgx, imgy, backimg
    if distance > 0:
        for i in range(distance):
            imgx=imgx+(1*speed)
            img2=pygame.transform.flip(img, False, False)
            if frame >= 1 and frame < 2:
                img=pygame.image.load('images/animation/9.png')
                frame=frame+0.2*speed
            elif frame >= 2 and frame < 3:
                img=pygame.image.load('images/animation/8.png')
                frame=frame+0.2*speed
            elif frame >= 3 and frame < 4:
                img=pygame.image.load('images/animation/7.png')
                frame=frame+0.2*speed
            elif frame >= 4 and frame < 5:
                img=pygame.image.load('images/animation/6.png')
                frame=frame+0.2*speed
            elif frame >= 5 and frame < 6:
                img=pygame.image.load('images/animation/5.png')
                frame=frame+0.2*speed
            elif frame >= 6 and frame < 7:
                img=pygame.image.load('images/animation/4.png')
                frame=frame+0.2*speed
            elif frame >= 7 and frame < 8:
                img=pygame.image.load('images/animation/3.png')
                frame=frame+0.2*speed
            elif frame >= 8 and frame < 9:
                img=pygame.image.load('images/animation/2.png')
                frame=frame+0.2*speed
            elif frame >= 9 and frame < 10:
                img=pygame.image.load('images/animation/1.png')
                frame=frame+0.2*speed
            else:
                frame=1
            if text_move==1:
                refresh()
            elif car_move==1:
                refresh(a=2)
            elif button==1:
                refresh(a=3)
            else:
                refresh(a=99)
    if distance < 0:
        for i in range(abs(distance)):
            imgx=imgx-(1*speed)
            img2=pygame.transform.flip(img, True, False)
            if frame >= 1 and frame < 2:
                img=pygame.image.load('images/animation/9.png')
                frame=frame+0.2*speed
            elif frame >= 2 and frame < 3:
                img=pygame.image.load('images/animation/8.png')
                frame=frame+0.2*speed
            elif frame >= 3 and frame < 4:
                img=pygame.image.load('images/animation/7.png')
                frame=frame+0.2*speed
            elif frame >= 4 and frame < 5:
                img=pygame.image.load('images/animation/6.png')
                frame=frame+0.2*speed
            elif frame >= 5 and frame < 6:
                img=pygame.image.load('images/animation/5.png')
                frame=frame+0.2*speed
            elif frame >= 6 and frame < 7:
                img=pygame.image.load('images/animation/4.png')
                frame=frame+0.2*speed
            elif frame >= 7 and frame < 8:
                img=pygame.image.load('images/animation/3.png')
                frame=frame+0.2*speed
            elif frame >= 8 and frame < 9:
                img=pygame.image.load('images/animation/2.png')
                frame=frame+0.2*speed
            elif frame >= 9 and frame < 10:
                img=pygame.image.load('images/animation/1.png')
                frame=frame+0.2*speed
            else:
                frame=1
            if text_move==1:
                refresh()
            elif car_move==1:
                refresh(a=2)
            elif button==1:
                refresh(a=3)
            else:
                refresh(a=99)
def jump(height, *extra):
    
    global frame, img, img2, imgx, imgy, backimg
    img=pygame.image.load('images/animation/6.png')
    img2=pygame.transform.rotate(img, 0)
    for i in range(height):
        imgy=imgy-2
        refresh()
    
    for i in range(int(height/2)):
        imgy=imgy+4
        refresh()
    img=pygame.image.load('images/animation/4.png')
    img2=pygame.transform.rotate(img, 0)
    refresh()

def jump_walk(height,background):
    global frame, img, img2, imgx, imgy, backimg, ampelmann
    img=pygame.image.load('images/animation/6.png')
    img2=pygame.transform.rotate(img, 0)
    for i in range(height):
        imgy=imgy-2
        imgx=imgx+10
        refresh()
        
    ampelmann=pygame.image.load('images/invisible.png')
    backimg=pygame.image.load(background)
    imgx=0
    refresh(a=99)
    
    for i in range(int(height/2)):
        imgy=imgy+4
        imgx=imgx+7
        refresh()
    img=pygame.image.load('images/animation/4.png')
    img2=pygame.transform.rotate(img, 0)
    refresh()
    
def talk(phrase,x,y,offsetx=0,offsety=0):
    global text, frame, img, img2, backimg
    img=pygame.image.load('images/animation/9.png')
    text=font.render(phrase,True,black)
    screen.blit(text,(x+90,y-10))
    pygame.display.update()

def refresh(a = 0):
    global frame, img, img2, imgx, imgy, backimg, ampelmann, car, carx, cary, button
    screen.fill((100,100,100))
    screen.blit(backimg,(0,0))
    if a==2:
        screen.blit(car,(carx,cary))
    if a==3:
        screen.blit(button,(50,300))
        screen.blit(text,(imgx+90,imgy-10))
    if a==4:
        screen.blit(button,(50,300))
    screen.blit(ampelmann,(580,300))
    screen.blit(img2,(imgx,imgy))
    if a!=99 and a!=3 and a!=4:
        screen.blit(text,(imgx+90,imgy-10))
    pygame.display.update()

def ampelmann_switch(color='r'):
    global ampelmann
    if color=='r':
        ampelmann=pygame.image.load('images/ampelmann-red.png')
        refresh(a=99)
    elif color=='g':
        ampelmann=pygame.image.load('images/ampelmann-green.png')
        refresh(a=4)

def car_drive():
    global carx, cary, car, car_height, car_width
    for i in range(11):
        car=pygame.image.load('images/car.png')
        car_width=int(car_width*(5/4))
        car_height=int(car_height*(5/4))
        car=pygame.transform.smoothscale(car,(car_width,car_height))
        carx=400-(car.get_width()/2)
        time.sleep(0.1)
        walk(20, car_move=1)
def runover():
    global img, img2, imgx, imgy, backimg, ampelmann
    for i in range(200):
        img2=pygame.transform.rotate(img, i*10)
        imgx=imgx-3
        imgy=imgy-2
        refresh(a=2)
    time.sleep(1)
    imgx=800
    backimg=pygame.image.load('images/sign-yellow.png')
    ampelmann=pygame.image.load('images/ampelmann-red.png')
    refresh(a=3)
    for i in range(200):
        img2=pygame.transform.rotate(img, i*10)
        imgx=imgx-3
        imgy=imgy+3
        refresh(a=3)
    img2=pygame.transform.rotate(img, 270)
    refresh(a=3)
    time.sleep(1)
    for i in range(90):
        imgy=imgy-2.2
        img2=pygame.transform.rotate(img,270+i)
        refresh(a=3)
        
    
#-----\FUNCTIONS/---------------------------------------------------------

refresh()
walk(300)
ampelmann_switch()
talk('''You can't pass!''',480,280)
time.sleep(speed*1)
talk('Why?',imgx,imgy)
jump(25, text)
time.sleep(speed*0.1)
jump(25, text)
time.sleep(speed*0.5)
refresh(a=99)
time.sleep(speed*0.5)
talk('''Because I'm red!''',470,280)
time.sleep(speed*1)
refresh(a=99)
talk('''You have to''',520,280)
time.sleep(speed*0.8)
refresh(a=99)
talk('''change me''',520,280)
time.sleep(speed*0.8)
refresh(a=99)
talk('''to green!''',520,280)
time.sleep(speed*0.8)
refresh(a=99)
talk('How do I do that?',imgx,imgy)
refresh()
time.sleep(speed*1)
talk('''Just press the button''',520,280)
time.sleep(speed*0.8)
refresh(a=99)
talk('''And wait''',380,280)
time.sleep(speed*1.5)
refresh(a=99)
font=pygame.font.Font('freesansbold.ttf',18)
talk('Fine! I will wait!',(imgx),(imgy))
refresh()
time.sleep(speed*1)
font=pygame.font.Font('freesansbold.ttf',24)
refresh(a=99)
talk('I hate this stop signs!',(imgx),(imgy))
walk(-50)
walk(-150,text_move=1)
walk(-100)
walk(1)
    
talk('',(imgx),(imgy))
time.sleep(1)
walk(50,speed=10)
jump_walk(25,'images/road.jpg')
car_drive()
runover()
time.sleep(0.5)
talk('Wow, what was that?',imgx,imgy)
refresh(a=3)
time.sleep(1)
talk('What happened?',imgx,imgy)
refresh(a=3)
walk(150, button=1)
talk('',imgx,imgy)
img=pygame.image.load('images/animation/9.png')
refresh(a=3)
font=pygame.font.Font('freesansbold.ttf',18)
talk('''You shouldn't have done that!''',370,290)
time.sleep(1)
refresh(a=4)
talk('''You could have died''',400,290)
time.sleep(1)
talk('I just wanted to get to the other side',imgx,imgy)
refresh(a=3)
time.sleep(1)
talk('''The only thing you had to do''',370,290)
time.sleep(1)
refresh(a=4)
talk('''was press the button and wait''',370,290)
time.sleep(1)
talk('But I am on a hurry',imgx,imgy)
refresh(a=3)
time.sleep(1)
walk(-250, button=1)
refresh(a=4)
talk('''*Beep*''',-30,300)
time.sleep(1)
talk('',(imgx),(imgy))
refresh(a=4)
walk(250, button=1)
talk('Now what?',imgx,imgy)
refresh(a=3)
time.sleep(1)
talk('''Wait for it...''',470,290)
time.sleep(1)
refresh(a=4)
time.sleep(1)
talk('''Wait for it...''',470,290)
time.sleep(1)
refresh(a=4)
time.sleep(1)
talk('''I can feel it!''',470,290)
time.sleep(1)
refresh(a=4)
time.sleep(1)
ampelmann_switch(color='g')
talk('''See?''',470,290)
time.sleep(1)
refresh(a=4)
talk('''Now you can cross safely''',450,290)
time.sleep(1)
refresh(a=4)
talk('''It wasn't that hard''',470,290)
time.sleep(1)
refresh(a=4)

for i in range(255):
    rect=pygame.Surface((800,542))
    rect.set_alpha(i)
    rect.fill((0,0,0))
    screen.blit(rect,(0,0))
    pygame.display.update()
    time.sleep(0.05)
