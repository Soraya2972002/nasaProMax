import pygame 
import math
bars={'physical':30,'mental':100}#porcentage ....... 

def whichcolour(stg):
        if bars[stg]>=50 :
            return "#FF0000"
        else:
            return "#00FF00"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


clock = pygame.time.Clock()
FPS = 300

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#background = pygame.color.Color("#3B2042")
pygame.display.set_caption("NasaProMax")

#load image
bg = pygame.image.load("./images/stars2.png").convert()
grp3 = pygame.image.load("./images/Group 3.png").convert_alpha()
chC = pygame.image.load("./images/Choose Character.png").convert_alpha()
logo = pygame.image.load("./images/Logo.png").convert_alpha()
title = pygame.image.load("./images/Titkle.png").convert_alpha()
polygone1 = pygame.image.load("./images/Polygon 1.png").convert_alpha()
polygone2 = pygame.image.load("./images/Polygon 2.png").convert_alpha()
#astronaut = pygame.image.load("./images/astronaut.png").convert_alpha()
bar_bg = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
bar_bg2 = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
bar_bg3 = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
bar_bg4 = pygame.image.load("./images/Rectangle 3.png").convert_alpha()


bg_height = bg.get_height()
bg_rect = bg.get_rect()


#define game variables
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1

run = True
def chooseB():
 screen.blit(bg,(0,0))
 while run:
    
    screen.blit(bg, (0, 0))
    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (0, i * bg_height + scroll))
        bg_rect.y = i * bg_height + scroll
        pygame.draw.rect(screen, "#412161", bg_rect, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

      #scroll background
    scroll -= 0.3

  #reset scroll
    if abs(scroll) > bg_height:
        scroll = 0
    


    
    
    screen.blit(bar_bg, (660, 237))
    pygame.draw.rect( screen, whichcolour("physical"), (660, 237, bars["physical"]*3.08, 22),0,0,0,5,0,5)
    screen.blit(bar_bg2, (660, 321))
    pygame.draw.rect( screen, "#EB5858", (660, 321, 109, 22),0,0,0,5,0,5)
    screen.blit(bar_bg3, (660, 405))
    pygame.draw.rect( screen, "#EB5858", (660, 405, 169, 22),0,0,0,5,0,5)
    screen.blit(bar_bg4, (660, 489))
    pygame.draw.rect( screen, "#EB5858", (660, 489, 259, 22),0,0,0,5,0,5)
    screen.blit(polygone1, (550, 290))
    screen.blit(polygone2, (118, 290))
    screen.blit(title, (670, 125))
    screen.blit(logo, (1018, 33))
    screen.blit(grp3, (178, 94))
    #screen.blit(astronaut, (237, 150))
    screen.blit(chC, (457, 37))



   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)

    

  
    pygame.display.flip()
    



  
    
    pygame.display.update()

pygame.quit()