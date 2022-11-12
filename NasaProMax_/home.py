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
bg = pygame.image.load("./images/stars2.png").convert()
logo = pygame.image.load("./images/group 1.png").convert_alpha()
explore = pygame.image.load("./images/group 2.png").convert_alpha()



bg_height = bg.get_height()
bg_rect = bg.get_rect()


#define game variables
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1

run = True
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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)

    


    screen.blit(logo, (452, 111))
    screen.blit(explore, (460, 429))

  
    pygame.display.flip()
    



  
    
    pygame.display.update()

pygame.quit()
