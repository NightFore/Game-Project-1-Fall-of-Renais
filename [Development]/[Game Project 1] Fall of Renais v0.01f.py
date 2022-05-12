import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Glass_Break-stephan_schutze-958181291.wav")
pygame.mixer.music.load("Truth_Despair_and_Hope.mp3")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,176,80)
groundcolor = (188,122,56)

bright_red = (255,96,96)
bright_green = (96,255,96)

block_color = (247,49,41)

Eirika_width = 50
Eirika_height = 70

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Game Project 1")
clock = pygame.time.Clock()


EirikaImg = pygame.image.load('eirika_masterlord_sword (1).png')



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def ground(groundx, groundy, groundw, groundh, color):
    pygame.draw.rect(gameDisplay, color, [groundx, groundy, groundw, groundh])

def Eirika(x,y):
    gameDisplay.blit(EirikaImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()

    
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    message_display('You Died')

def button(msg,x,y,w,h,ic,ac,action=None):
    #ic = Inactive Color
    #ac = Active Color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] >x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] ==1 and action !=None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
        
    gameDisplay.blit(textSurf, textRect)

def quit_game():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Game Project 1", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start!", 150,450,100,50, green, bright_green,game_loop)
        button("Quit...", 550,450,100,50, red, bright_red,quit_game)
        
        pygame.display.update()
        clock.tick(15)



def game_loop():

    pygame.mixer.music.play(-1)

    x = (display_width * 0.8)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -500
    thing_speed = 7.5
    thing_width = 75
    thing_height = 75

    dodged = 0
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if thing_speed < 10:
                        x_change = -5
                    elif thing_speed < 15:
                        x_change = -6.5
                    elif thing_speed < 20:
                        x_change = -8
                    else:
                        x_change = -10

                elif event.key == pygame.K_RIGHT:
                    if thing_speed < 10:
                        x_change = 5
                    elif thing_speed < 15:
                        x_change = 6.5
                    elif thing_speed < 20:
                        x_change = 8
                    else:
                        x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            if thing_speed < 10:
                                x_change = 5
                            elif thing_speed < 15:
                                x_change = 6.5
                            elif thing_speed < 20:
                                x_change = 8
                            else:
                                x_change = 10
                elif event.key == pygame.K_RIGHT:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if thing_speed < 10:
                                x_change = -5
                            elif thing_speed < 15:
                                x_change = -6.5
                            elif thing_speed < 20:
                                x_change = -8
                            else:
                                x_change = -10

        x += x_change

        gameDisplay.fill(white)

        
        #thing(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        Eirika(x,y)
        things_dodged(dodged)

        if x > display_width - Eirika_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            if thing_speed < 10:
                thing_speed +=1.1
                thing_width +=5
            elif thing_speed < 15:
                thing_speed +=0.5
                thing_width +=2.0
            elif thing_speed < 20:
                thing_speed +=0.2
                thing_width +=0.5
            else:
                thing_speed +=0.1

        if y + Eirika_height > thing_starty and y < thing_starty + thing_height:
            #print('Y Crossover')
                
            if x + Eirika_width > thing_startx and x < thing_startx + thing_width:
                #print('X Crossover')
                crash()

        #ground(groundx, groundy, groundw, groundh, color)
        ground(0, display_height*0.8 + Eirika_height, display_width, display_height, groundcolor)

        pygame.display.update()
        clock.tick(60)



game_intro()
game_loop()
pygame.quit()
quit()
