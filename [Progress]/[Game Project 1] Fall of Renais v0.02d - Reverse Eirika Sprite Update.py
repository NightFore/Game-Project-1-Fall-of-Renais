import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
keys = [False, False]

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,96,96)
green = (0,176,80)
bright_green = (96,255,96)
block_color = (247,49,41)
groundcolor = (188,122,56)
count_color = (74,255,65)

character_unselected_color = (252,251,171)
character_selected_color = (138,198,189)

EirikaImg = pygame.image.load('eirika_masterlord_sword.png')
EirikaReverseImg = pygame.image.load('eirika_masterlord_sword_reverse.png')
Eirika_width = 41
Eirika_height = 66

EphraimImg = pygame.image.load('ephraim_masterlord_lance.png')
Ephraim_width = 47
Ephraim_height = 56

CYL_width = 320
CYL_height = 320

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

def image(x, y, z):
    if z == 1:
        z = pygame.image.load('CYL_Eirika.png')
    elif z == 2:
        z = pygame.image.load('CYL_Ephraim.png')
    gameDisplay.blit(z, (x-(CYL_width/2), y-(CYL_height/2)))

    
    
def Eirika(Eirikax,Eirikay, Eirikaz):
    if Eirikaz == 1:
        gameDisplay.blit(EirikaImg, (Eirikax, Eirikay))
    elif Eirikaz == 2:
        gameDisplay.blit(EirikaReverseImg, (Eirikax, Eirikay))
                
def EirikaMusic():
    pygame.mixer.music.load("Truth_Despair_and_Hope.mp3")
    pygame.mixer.music.play(-1)

def Ephraim(Ephraimx,Ephraimy):
    gameDisplay.blit(EphraimImg, (Ephraimx, Ephraimy))

def EphraimMusic():
    pygame.mixer.music.load("Determination.mp3")
    pygame.mixer.music.play(-1)
    
    
def background(backgroundx,backgroundy):
    backgroundImg = pygame.image.load('Background.png')
    gameDisplay.blit(backgroundImg, (backgroundx,backgroundy))

def DeathMusic():
    pygame.mixer.music.load("In_Sorrows_Shadows.mp3")
    pygame.mixer.music.play(-1)
    
def Death(z):
    Death_Sound = pygame.mixer.Sound("Death.wav")
    pygame.mixer.Sound.play(Death_Sound)
    DeathMusic()
    
    message_display('You Died', display_width * 0.5, display_height * 0.5, text_death)
    time.sleep(5)
    if z == 1:
        game_eirika_loop()
    if z == 2:
        game_ephraim_loop()

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def character(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Character: "+str(count), True, count_color)
    gameDisplay.blit(text,(0,0))
    
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, count_color)
    gameDisplay.blit(text,(0,20))

def level(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Level: "+str(count), True, count_color)
    gameDisplay.blit(text,(100,20))

def ground(groundx, groundy, groundw, groundh, color):
    pygame.draw.rect(gameDisplay, color, [groundx, groundy, groundw, groundh])


#Text
def message_display(text, x, y, z):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = z(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def text_title(text, font):
    textSurface = font.render(text, True, (224,64,0))
    return textSurface, textSurface.get_rect()
def text_character_selection(text,font):
    textSurface = font.render(text, True, (152,232,248))
    return textSurface, textSurface.get_rect()
def text_death(text,font):
    textSurface = font.render(text, True, bright_red)
    return textSurface, textSurface.get_rect()
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def button(msg,x,y,w,h,ic,ac,action=None):
    Select3_Sound = pygame.mixer.Sound("Select 3.wav")
    #ic = Inactive Color
    #ac = Active Color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse[0])
    
    if x+w > mouse[0] >x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] ==1 and action !=None:
            pygame.mixer.Sound.play(Select3_Sound)
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

        message_display("Game Project 1", (display_width/2),(display_height/4), text_title)
        
        button("Play!", 150,450,100,50, green, bright_green,game_character_loop)
        button("Quit...", 550,450,100,50, red, bright_red,quit_game)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                game_character_loop()
            if event.key == pygame.K_ESCAPE:
                quit_game()
        pygame.display.update()
        clock.tick(30)

def game_character_loop():
    character_selection_Background(0,0)
    character_selection_Music()
    image(display_width*0.25, display_height*0.60, 1)
    image(display_width*0.75, display_height*0.60, 2)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message_display("Character Selection", display_width * 0.5, display_height * 0.25, text_character_selection)
        button("Eirika", 150, 525, 100, 50, character_unselected_color, character_selected_color, game_eirika_loop)
        button("Ephraim", 550, 525, 100, 50, character_unselected_color, character_selected_color, game_ephraim_loop)
        pygame.display.update()
        clock.tick(30)



def game_eirika_loop():
    EirikaMusic()
    backgroundx = 0
    backgroundy = 0

    Character = "Eirika"
    dodged = 0
    Level = "Tutorial"

    Eirikax = (display_width * 0.8)
    Eirikay = (display_height * 0.8)
    Eirikaz = 1
    Eirikax_change = 0

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

#Game Mechanics
    #KEY DOWN/UP
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keys[0]=True
                    Eirikaz = 1
                if event.key == pygame.K_RIGHT:
                    keys[1]= True
                    Eirikaz = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[0]=False
                elif event.key == pygame.K_RIGHT:
                    keys[1]=False

    #Eirika Movements
            if keys[0]==False and keys[1]==False:
                Eirikax_change = 0


            if keys[0]==True and keys[1]==False:
                if thing_speed < 18 :
                    Eirikax_change = -6 - (thing_speed/3)
                else:
                    Eirikax_change = -14
                    
            if keys[0]==False and keys[1]==True:
                if thing_speed < 18 :
                    Eirikax_change = 6 + (thing_speed/3)
                else:
                    Eirikax_change = 14

            
            if keys[0]==True and keys[1]==True:
                if thing_speed < 18 :
                    Eirikax_change = 6 + (thing_speed/3)
                else:
                    Eirikax_change = 14
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if thing_speed < 18 :
                            Eirikax_change = -6 - (thing_speed/3)
                        else:
                            Eirikax_change = -14
                        
        background(0,0)
        
        Eirika(Eirikax,Eirikay,Eirikaz)
        Eirikax += Eirikax_change
        
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        character(Character)
        things_dodged(dodged)
        level(Level)
        
        ground(0, display_height*0.8 + Eirika_height, display_width, display_height, groundcolor)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width - thing_width)
            dodged += 1
            if thing_speed < 10:
                Level = 1
                thing_speed +=2
                thing_width +=3
            elif thing_speed < 16:
                Level = 2
                thing_speed +=1
                thing_width +=2
            elif thing_speed < 18:
                Level = 3
                thing_speed +=1
                thing_width +=1
            elif thing_speed < 25:
                Level = 4
                thing_speed +=1
            else:
                Level = 5
                thing_speed +=0.1
                
        if Eirikax > display_width - Eirika_width or Eirikax < 0:
            Death(1)

        if Eirikay + Eirika_height > thing_starty and Eirikay < thing_starty + thing_height:
            #print('Y Crossover')
                
            if Eirikax + Eirika_width > thing_startx and Eirikax < thing_startx + thing_width:
                #print('X Crossover')
                Death(1)

        pygame.display.update()
        clock.tick(60)



def game_ephraim_loop():
    EphraimMusic()
    backgroundx = 0
    backgroundy = 0

    Character = "Ephraim"
    dodged = 0
    Level = "Easy"

    Ephraimx = (display_width * 0.8)
    Ephraimy = (display_height * 0.8)
    Ephraimx_change = 0

    thing_startx = random.randrange(0, display_width - Eirika_width)
    thing_starty = -350
    thing_speed = 15
    thing_width = 75
    thing_height = 75
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#Game Mechanics
    #KEY DOWN/UP
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

    #Ephraim Movements
            if keys[0]==False and keys[1]==False:
                Ephraimx_change = 0


            if keys[0]==True and keys[1]==False:
                Ephraimx_change = -15
                if thing_speed > 20:
                    Ephraimx_change = -20
                if thing_speed > 35:
                    Ephraimx_change = -25
                    
            if keys[0]==False and keys[1]==True:
                Ephraimx_change = 15
                if thing_speed > 20:
                    Ephraimx_change = 20
                if thing_speed > 35:
                    Ephraimx_change = 25

            if keys[0]==True and keys[1]==True:
                Ephraimx_change = 15
                if thing_speed > 20:
                    Ephraimx_change = 20
                if thing_speed > 35:
                    Ephraimx_change = -25
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Ephraimx_change = -15
                        if thing_speed > 20:
                            Ephraimx_change = -20
                        if thing_speed > 35:
                            Ephraimx_change = -25
                        
        background(0,0)

        Ephraim(Ephraimx,Ephraimy)
        Ephraimx += Ephraimx_change
        
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        character(Character)
        things_dodged(dodged)
        level(Level)
        
        ground(0, display_height*0.8 + Ephraim_height, display_width, display_height, groundcolor)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width - thing_width)
            dodged += 1
            if thing_speed < 20:
                Level = "Normal"
                thing_speed +=1
                thing_width +=5
            elif thing_speed < 25:
                Level = "Hard"
                thing_speed +=1
                thing_width +=3
            elif thing_speed < 35:
                Level = "Abyssal"
                thing_speed +=1
                
        if Ephraimx > display_width - Ephraim_width or Ephraimx < 0:
            Death(2)

        if Ephraimy + Ephraim_height > thing_starty and Ephraimy < thing_starty + thing_height:
            #print('Y Crossover')
                
            if Ephraimx + Ephraim_width > thing_startx and Ephraimx < thing_startx + thing_width:
                #print('X Crossover')
                Death(2)

        pygame.display.update()
        clock.tick(60)



game_intro()
game_character_loop()
game_eirika_loop()
game_ephraim_loop()
pygame.quit()
quit()
