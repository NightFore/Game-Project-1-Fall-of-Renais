import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
keys = [False, False, False, False]

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,96,96)
green = (0,176,80)
bright_green = (96,255,96)
block_color = (247,49,41)
groundcolor = (188,122,56)


EirikaImg = pygame.image.load('eirika_masterlord_sword.png')
Eirika_width = 41
Eirika_height = 66

EphraimImg = pygame.image.load('ephraim_masterlord_lance.png')
Ephraim_width = 47
Ephraim_height = 56



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Game Project 1")
clock = pygame.time.Clock()
    
def backgroundMenu(backgroundx,backgroundy):
    backgroundMenuImg = pygame.image.load('BackgroundMenu.jpg')
    gameDisplay.blit(backgroundMenuImg, (backgroundx,backgroundy))

def MenuMusic():
    pygame.mixer.music.load("Combat_Preparations.mp3")
    pygame.mixer.music.play(-1)
    
def character_selection_Background(backgroundx,backgroundy):
    char_sel_BackgroundImg = pygame.image.load('character_selection.png')
    gameDisplay.blit(char_sel_BackgroundImg, (backgroundx,backgroundy))

def character_selection_Music():
    pygame.mixer.music.load("Distant_Roads.mp3")
    pygame.mixer.music.play(-1)
    
def Eirika(x,y):
    gameDisplay.blit(EirikaImg, (x,y))

def EirikaMusic():
    pygame.mixer.music.load("Truth_Despair_and_Hope.mp3")
    pygame.mixer.music.play(-1)
    
def background(backgroundx,backgroundy):
    backgroundImg = pygame.image.load('Background.png')
    gameDisplay.blit(backgroundImg, (backgroundx,backgroundy))

def DeathMusic():
    pygame.mixer.music.load("In_Sorrows_Shadows.mp3")
    pygame.mixer.music.play(-1)
    
def DeathSound():
    Death_Sound = pygame.mixer.Sound("Death.wav")
    pygame.mixer.Sound.play(Death_Sound)
    DeathMusic()
    
    message_display('You Died')
    time.sleep(5)
    game_loop()
    
    
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def ground(groundx, groundy, groundw, groundh, color):
    pygame.draw.rect(gameDisplay, color, [groundx, groundy, groundw, groundh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_title(text, font):
    textSurface = font.render(text, True, (100,157,253))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

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

def game_intro():
    backgroundMenu(0,0)
    MenuMusic()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_title("Game Project 1", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play!", 150,450,100,50, green, bright_green,game_character_loop)
        button("Quit...", 550,450,100,50, red, bright_red,quit_game)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                game_loop()
            if event.key == pygame.K_ESCAPE:
                quit_game()
        pygame.display.update()
        clock.tick(30)

def game_character_loop():
    character_selection_Background(0,0)
    character_selection_Music()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message_display("Character Selection")

def game_loop():
    EirikaMusic()

    dodged = 0

    x = (display_width * 0.8)
    y = (display_height * 0.8)
    x_change = 0
    
    backgroundx = 0
    backgroundy = 0

    thing_startx = random.randrange(0, display_width - Eirika_width)
    thing_starty = -350
    thing_speed = 6
    thing_width = 75
    thing_height = 75
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keys[0]=True
                if event.key == pygame.K_RIGHT:
                    keys[1]= True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[0]=False
                elif event.key == pygame.K_RIGHT:
                    keys[1]=False


            if keys[0]==False and keys[1]==False:
                x_change = 0

            if keys[0]==True and keys[1]==False:
                if thing_speed < 10:
                    x_change = -6 - ((thing_speed - 6)/2)
                elif thing_speed < 14:
                    x_change = -8 - ((thing_speed -10)/2)
                elif thing_speed < 16:
                    x_change = -10 - ((thing_speed -14)/2)
                elif thing_speed < 18:
                    x_change = -12
                else:
                    x_change = -13
            if keys[0]==False and keys[1]==True:
                if thing_speed < 10:
                    x_change = 6 + ((thing_speed - 6)/2)
                elif thing_speed < 14:
                    x_change = 8 + ((thing_speed -10)/2)
                elif thing_speed < 16:
                    x_change = 10 + ((thing_speed -14)/2)
                elif thing_speed < 18:
                    x_change = 12
                else:
                    x_change = 13
            
            if keys[0]==True and keys[1]==True:
                if thing_speed < 10:
                    x_change = 6 + ((thing_speed - 6)/2)
                elif thing_speed < 14:
                    x_change = 8 + ((thing_speed -10)/2)
                elif thing_speed < 16:
                    x_change = 10 + ((thing_speed -14)/2)
                elif thing_speed < 18:
                    x_change = 12
                else:
                    x_change = 13
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if thing_speed < 10:
                            x_change = -6 - ((thing_speed - 6)/2)
                        elif thing_speed < 14:
                            x_change = -8 - ((thing_speed -10)/2)
                        elif thing_speed < 16:
                            x_change = -10 - ((thing_speed -14)/2)
                        elif thing_speed < 18:
                            x_change = -12
                        else:
                            x_change = -13
                        
        #print(keys)
        x += x_change

        #background Img
        background(0,0)

        #Character
        Eirika(x,y)
        
        #thing(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        things_dodged(dodged)

        #ground(groundx, groundy, groundw, groundh, color)
        ground(0, display_height*0.8 + Eirika_height, display_width, display_height, groundcolor)

        if x > display_width - Eirika_width or x < 0:
            DeathSound()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width - thing_width)
            dodged += 1
            if thing_speed < 10:
                thing_speed +=2
                thing_width +=3
            elif thing_speed < 14:
                thing_speed +=1
                thing_width +=2
            elif thing_speed < 16:
                thing_speed +=1
                thing_width +=1
            elif thing_speed < 18:
                thing_speed +=1
            else:
                thing_speed +=0.1
                

        if y + Eirika_height > thing_starty and y < thing_starty + thing_height:
            #print('Y Crossover')
                
            if x + Eirika_width > thing_startx and x < thing_startx + thing_width:
                #print('X Crossover')
                DeathSound()

        pygame.display.update()
        clock.tick(60)



game_intro()
game_loop()
pygame.quit()
quit()
