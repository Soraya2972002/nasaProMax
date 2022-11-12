
import pygame 
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


clock = pygame.time.Clock()
FPS = 300

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#background = pygame.color.Color("#3B2042")
pygame.display.set_caption("NasaProMax")

#load image
bg = pygame.image.load("images/stars2.png").convert()
logo = pygame.image.load("images/logoshape.png").convert_alpha()
shape = pygame.image.load("images/shape.png").convert_alpha()
earth = pygame.image.load("images/earth.png").convert_alpha()
mars = pygame.image.load("images/mars.png").convert_alpha()
iss = pygame.image.load("images/iss.png").convert_alpha()
saturn = pygame.image.load("images/saturn.png").convert_alpha()
moon = pygame.image.load("images/moon.png").convert_alpha()
jupiter = pygame.image.load("images/jupiter.png").convert_alpha()
mercury = pygame.image.load("images/mercury.png").convert_alpha()
rocket = pygame.image.load("images/rocket.png").convert_alpha()
earthW = pygame.image.load("images/earthW.png").convert_alpha()
marsW = pygame.image.load("images/marsW.png").convert_alpha()
issW = pygame.image.load("images/issW.png").convert_alpha()
saturnW = pygame.image.load("images/saturnW.png").convert_alpha()
moonW = pygame.image.load("images/moonW.png").convert_alpha()
jupiterW = pygame.image.load("images/jupiterW.png").convert_alpha()
mercuryW = pygame.image.load("images/mercuryW.png").convert_alpha()




bg_height = bg.get_height()
bg_rect = bg.get_rect()


#define game variables
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1

run = True


def planetMenu():
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

    scroll -= 0.3

  #reset scroll
    if abs(scroll) > bg_height:
        scroll = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)

    


    screen.blit(logo, (1060, 15))

    screen.blit(shape, (110, 114))
    #screen.blit(earth, (151, 141))
    Image = Buttonify("images/earth.png",(151, 141), screen)
    screen.blit(earthW, (185, 290))

    screen.blit(shape, (363, 114))
    screen.blit(mars, (390, 121))
    screen.blit(marsW, (438, 290))
    screen.blit(shape, (616, 114))
    screen.blit(iss, (616, 168))
    screen.blit(issW, (703, 290))
    screen.blit(shape, (869, 114))
    screen.blit(saturn, (883, 107))
    screen.blit(saturnW, (945, 290))
    screen.blit(shape, (110, 352))
    screen.blit(rocket, (160, 380))
    screen.blit(shape, (363, 352))
    screen.blit(moon, (384, 360))
    screen.blit(moonW, (434, 525))
    screen.blit(shape, (616, 352))
    screen.blit(jupiter, (647, 362))
    screen.blit(jupiterW, (686, 525))
    screen.blit(shape, (869, 352))
    screen.blit(mercury, (926, 392))
    screen.blit(mercuryW, (931, 525))
  
    pygame.display.flip()
    



  
    
    pygame.display.update()

pygame.quit()
