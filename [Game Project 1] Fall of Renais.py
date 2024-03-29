import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

#Left, Right, Return
keys = [False, False,False]
sound = False

black = (0,0,0)
red = (200,0,0)
bright_red = (255,96,96)
green = (0,176,80)
bright_green = (96,255,96)
block_color = (247,49,41)

character_unselected_color = (252,251,171)
character_selected_color = (138,198,189)

backgroundMenuImg = pygame.image.load('data\graphic\BackgroundMenu.jpg')
backgroundImg = pygame.image.load('data\graphic\Background.png')
character_BackgroundImg = pygame.image.load('data\graphic\character_selection.png')
Scoreboard_Img = pygame.image.load('data\graphic\Scoreboard.png')

Select2_Sound = pygame.mixer.Sound("data\sound\Select 2.wav")
Select3_Sound = pygame.mixer.Sound("data\sound\Select 3.wav")

EirikaImg = pygame.image.load('data\graphic\eirika_masterlord_sword.png')
EirikaReverseImg = pygame.image.load('data\graphic\eirika_masterlord_sword_reverse.png')
Eirika_width = 41
Eirika_height = 66

EphraimImg = pygame.image.load('data\graphic\ephraim_masterlord_lance.png')
EphraimReverseImg = pygame.image.load('data\graphic\ephraim_masterlord_lance_reverse.png')
Ephraim_width = 47
Ephraim_height = 56

CYL_width = 320
CYL_height = 320

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fall of Renais")
clock = pygame.time.Clock()

def quit_game():
    pygame.quit()
    quit()

def MenuMusic():
    pygame.mixer.music.load("data\music\Combat_Preparations.mp3")
    pygame.mixer.music.play(-1)

def character_selection_Music():
    pygame.mixer.music.load("data\music\Distant_Roads.mp3")
    pygame.mixer.music.play(-1)

def Image(Img, x, y):
    if Img == "CYL_Eirika":
        Img = pygame.image.load('data\graphic\CYL_Eirika.png')
    elif Img == "CYL_Ephraim":
        Img = pygame.image.load('data\graphic\CYL_Ephraim.png')
    gameDisplay.blit(Img, (x-(CYL_width/2), y-(CYL_height/2)))

    
def Eirika(Eirikax,Eirikay, Eirikaz):
    if Eirikaz == 1:
        gameDisplay.blit(EirikaImg, (Eirikax, Eirikay))
    elif Eirikaz == 2:
        gameDisplay.blit(EirikaReverseImg, (Eirikax, Eirikay))
                
def EirikaMusic():
    pygame.mixer.music.load("data\music\Truth_Despair_and_Hope.mp3")
    pygame.mixer.music.play(-1)

def Ephraim(Ephraimx,Ephraimy,Ephraimz):
    if Ephraimz == 1:
        gameDisplay.blit(EphraimImg, (Ephraimx, Ephraimy))
    elif Ephraimz == 2:
        gameDisplay.blit(EphraimReverseImg, (Ephraimx, Ephraimy))

def EphraimMusic():
    pygame.mixer.music.load("data\music\Determination.mp3")
    pygame.mixer.music.play(-1)

def DeathMusic():
    pygame.mixer.music.load("data\music\In_Sorrows_Shadows.mp3")
    pygame.mixer.music.play(-1)
    
def Death(Death):
    Death_Sound = pygame.mixer.Sound("data\sound\Death.wav")
    pygame.mixer.Sound.play(Death_Sound)
    DeathMusic()
    
    message_display('You Died', display_width * 0.5, display_height * 0.5, text_death)
    time.sleep(5)
    if Death == "Eirika":
        game_eirika_loop()
    if Death == "Ephraim":
        game_ephraim_loop()

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def scoreboard(Character,Dodged,Level, x, y):
    count_color = (255,251,255)
    scoreboard_height = 54
    gameDisplay.blit(Scoreboard_Img, (x,y))

    font = pygame.font.SysFont(None, 36)
    text = font.render("Character: " +str(Character), True, count_color)
    gameDisplay.blit(text,(99, y + 17))
    
    text = font.render("Dodged: "+str(Dodged), True, count_color)
    gameDisplay.blit(text,(427, y + 17))
    
    text = font.render("Level: "+str(Level), True, count_color)
    gameDisplay.blit(text,(593, y + 17))


#Text
def message_display(text, x, y, z):
    largeText = pygame.font.SysFont("comicsansms",50)
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


def selection(KEY, msg,x,y,w,h,ic,ac,keys,action=None):
# Activations Conditions
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if keys [KEY] == True or (x+w > mouse[0] >x and y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if (keys[2] == True) or (click[0] ==1 and action !=None):
            pygame.mixer.Sound.play(Select3_Sound)
            keys[KEY] = False
            keys[2] = False
            action() 
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))

    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
       
def game_intro():
    MenuMusic()
    gameDisplay.blit(backgroundMenuImg, (0,0))
    message_display("Fall of Renais", (display_width/2),(display_height/4), text_title)
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if keys[0] == False:
                    if event.key == pygame.K_LEFT:
                        pygame.mixer.Sound.play(Select2_Sound)
                        keys[0] = True
                        keys[1] = False
                if keys[1] == False:
                    if event.key == pygame.K_RIGHT:
                        pygame.mixer.Sound.play(Select2_Sound)
                        keys[0] = False
                        keys[1] = True
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    keys[2] = True
                if event.key == pygame.K_ESCAPE:
                    quit_game()
            selection(0, "Play!", 150,450,100,50, green, bright_green, keys, game_character_loop)
            selection(1, "Quit...", 550,450,100,50, red, bright_red, keys, quit_game)
            


def game_character_loop():
    character_selection_Music()
    gameDisplay.blit(character_BackgroundImg, (0,0))
    message_display("Character Selection", display_width * 0.5, display_height * 0.25, text_character_selection)
    Image("CYL_Eirika", display_width*0.25, display_height*0.60)
    Image("CYL_Ephraim", display_width*0.75, display_height*0.60)
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if keys[0] == False:
                    if event.key == pygame.K_LEFT:
                        pygame.mixer.Sound.play(Select2_Sound)
                        keys[0] = True
                        keys[1] = False
                if keys[1] == False:
                    if event.key == pygame.K_RIGHT:
                        pygame.mixer.Sound.play(Select2_Sound)
                        keys[0] = False
                        keys[1] = True
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    keys[2] = True
                if event.key == pygame.K_ESCAPE:
                    quit_game()
            selection(0, "Eirika", 150, 525, 100, 50, character_unselected_color, character_selected_color, keys, game_eirika_loop)
            selection(1, "Ephraim", 550, 525, 100, 50, character_unselected_color, character_selected_color, keys, game_ephraim_loop)

def game_eirika_loop():
    EirikaMusic()

    Character = "Eirika"
    Level = "Tutorial"
    Dodged = 0

    Eirikax = (display_width * 0.8)
    Eirikay = (display_height * 0.8)
    Eirikaz = 1
    Eirikax_change = 0

    thing_speed = 11
    thing_width = 75
    thing_height = 75
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -350
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#Game Mechanics
    # Miscellaneous Keys
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    keys[2] = True
                if event.key == pygame.K_ESCAPE:
                    quit_game()

    # KEY DOWN/UP
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        keys[0] = True
                if event.key == pygame.K_RIGHT:
                        keys[1] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[0]=False
                elif event.key == pygame.K_RIGHT:
                    keys[1]=False
                    
    # Eirika Movements Mechanics
            if keys[0]==False and keys[1]==False:
                Eirikax_change = 0

            if keys[0]==True and keys[1]==False:
                Eirikaz = 1
                if thing_speed <= 35 :
                    Eirikax_change = -6 - (thing_speed/3)
                else:
                    Eirikax_change = -20
                    
            if keys[0]==False and keys[1]==True:
                Eirikaz = 2
                if thing_speed < 35 :
                    Eirikax_change = 6 + (thing_speed/3)
                else:
                    Eirikax_change = 20

            
            if keys[0]==True and keys[1]==True:
                Eirikaz = 2
                if thing_speed < 35 :
                    Eirikax_change = 6 + (thing_speed/3)
                else:
                    Eirikax_change = 20
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Eirikaz = 1
                        if thing_speed < 35 :
                            Eirikax_change = -6 - (thing_speed/3)
                        else:
                            Eirikax_change = -20

    # Things Movements Mechanics
        if thing_starty > display_height:
            thing_starty = -2 * thing_height
            thing_startx = random.randrange(0, display_width - thing_width)
            Dodged += 1
            if thing_speed < 15:
                Level = "Easy"
                thing_speed += 1
                thing_width += 3
                
            elif thing_speed < 20:
                Level = "Normal"
                thing_speed +=1
                thing_width +=2
                
            elif thing_speed < 25:
                Level = "Hard"
                thing_speed += 1
                thing_width += 1
                
            elif thing_speed < 30:
                Level = "Lunatic"
                thing_speed += 1
                
            elif thing_speed < 35:
                Level = "Infernal"
                thing_speed += 1
                
            else:
                Level = "Abyssal"
                thing_speed += 0.1
                
        if Eirikax > display_width - Eirika_width or Eirikax < 0:
            Death("Eirika")

        if Eirikay + Eirika_height > thing_starty and Eirikay < thing_starty + thing_height:
            #print('Y Crossover')
                
            if Eirikax + Eirika_width > thing_startx and Eirikax < thing_startx + thing_width:
                #print('X Crossover')
                Death("Eirika")
                        
        gameDisplay.blit(backgroundImg, (0,0))
        Eirika(Eirikax,Eirikay,Eirikaz)
        Eirikax += Eirikax_change
        
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        
        scoreboard(Character,Dodged,Level, 0, display_height*0.8 + Eirika_height)

        pygame.display.update()
        clock.tick(60)


def game_ephraim_loop():
    EphraimMusic()

    Character = "Ephraim"
    Level = "Easy"
    Dodged = 0

    Ephraimx = (display_width * 0.8)
    Ephraimy = (display_height * 0.8 + 10)
    Ephraimz = 1
    Ephraimx_change = 0

    thing_speed = 16
    thing_width = 75
    thing_height = 75
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -350
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#Game Mechanics
    # Miscellaneous Keys
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    keys[2] = True
                if event.key == pygame.K_ESCAPE:
                    quit_game()

    # KEY DOWN/UP
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        keys[0] = True
                if event.key == pygame.K_RIGHT:
                        keys[1] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[0]=False
                elif event.key == pygame.K_RIGHT:
                    keys[1]=False
                    
    # Ephraim Movements Mechanics
            if keys[0]==False and keys[1]==False:
                Ephraimx_change = 0

            if keys[0]==True and keys[1]==False:
                Ephraimz = 1
                Ephraimx_change = -5 - (thing_speed/2)
                if Level == "Abyssal":
                    Ephraimx_change = -20
                    
            if keys[0]==False and keys[1]==True:
                Ephraimz = 2
                Ephraimx_change = 5 + (thing_speed/2)
                if Level == "Abyssal":
                    Ephraimx_change = 25


            if keys[0]==True and keys[1]==True:
                Ephraimz = 2
                Ephraimx_change = 5 + (thing_speed/2)
                if Level == "Abyssal":
                    Ephraimx_change = -20
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Ephraimz = 1
                        Ephraimx_change = -5 - (thing_speed/2)
                        if Level == "Abyssal":
                            Ephraimx_change = -20


        if thing_starty > display_height:
            thing_starty = - 2 * thing_height
            thing_startx = random.randrange(0,display_width - thing_width)
            Dodged += 1
            if thing_speed < 20:
                Level = "Normal"
                thing_speed +=1
                thing_width +=3
                
            elif thing_speed < 25:
                Level = "Hard"
                thing_speed +=1
                thing_width +=2
                
            elif thing_speed < 30:
                Level = "Infernal"
                thing_speed +=1
                thing_width += 1
                
            elif thing_speed < 35:
                Level = "Lunatic"
                thing_speed += 1
                
            elif thing_speed < 40:
                Level = "Abyssal"
                thing_speed += 1
                
            else:
                Level = "Impossible"
                thing_speed += 0.1
                
        if Ephraimx > display_width - Ephraim_width or Ephraimx < 0:
            Death("Ephraim")

        if Ephraimy + Ephraim_height > thing_starty and Ephraimy < thing_starty + thing_height:
            #print('Y Crossover')
                
            if Ephraimx + Ephraim_width > thing_startx and Ephraimx < thing_startx + thing_width:
                #print('X Crossover')
                Death("Ephraim")
        
        
        gameDisplay.blit(backgroundImg, (0,0))
        Ephraim(Ephraimx,Ephraimy,Ephraimz)
        Ephraimx += Ephraimx_change
        
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        
        scoreboard(Character,Dodged,Level, 0, display_height*0.8 + Ephraim_height + 10)

        pygame.display.update()
        clock.tick(60)



game_intro()
game_character_loop()
game_eirika_loop()
game_ephraim_loop()
pygame.quit()
quit()
