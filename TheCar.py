import pygame
import time
import random
pygame.init()
#width and height of the window
display_width=800
display_height=600
car_width=44
car_height=93
img=pygame.image.load('9.png')#Used to load the car image
img2=pygame.image.load('stone.png')#Used to load the obstacle image
disp=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race')
clock=pygame.time.Clock()
white=(255,255,255)
bg=(55,55,55)
color1=(6,174,238)
flag=1
def things_dodged(count):
    font=pygame.font.SysFont(None, 40)
    text=font.render("Dodged: "+str(count), True, color1)
    disp.blit(text,(0,0))
def things(thingx, thingy, thingw, thingh, color):
    #pygame.draw.rect(disp,color,[thingx,thingy,thingw,thingh]) -- To create your own block with dimensions thingw and thingh
    disp.blit(img2,(thingx,thingy))
def text_object(text, font):
    textSurface=font.render(text, True, color1)
    return  textSurface, textSurface.get_rect()
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect=text_object(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    disp.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
def crashing(d):
    message_display('You Crashed SCORE : '+str(d))
def car(x,y):
    disp.blit(img,(x,y))
def game_loop():
    x=(display_width*0.40)
    y=(display_height*0.84 )
    crash= False
    xchange=0
    thing_startx= random.randrange(0, display_width)
    thing_starty=-600
    thing_speed=3
    # use thing_width and thing_height to specify dimensions of the dropping blocks
    thing_width=100
    thing_height=100
    dodged=0
    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    xchange=-5
                elif event.key==pygame.K_RIGHT:
                    xchange=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    xchange=0
        x+=xchange
        disp.fill(bg)
        things(thing_startx, thing_starty, thing_width, thing_height, color1)
        if (thing_starty>display_height):
            thing_starty=0-thing_height
            thing_startx = random.randrange(0, display_width)
            dodged+=1
            if dodged%5==0:
                thing_speed+=1
        car(x,y)
        things_dodged(dodged)
        if x>display_width-car_width or x<0:
            crashing(dodged)
            crash=True

        pygame.display.update()
        if (((x<thing_startx+thing_width and x>thing_startx) or (x+car_width<thing_startx+thing_width and x+car_width>thing_startx)) and y<=thing_starty+thing_height ):
            crashing(dodged)
            crash=True
        thing_starty += thing_speed
        clock.tick(250)
while (flag==1):
    game_loop()
pygame.quit()
quit()
