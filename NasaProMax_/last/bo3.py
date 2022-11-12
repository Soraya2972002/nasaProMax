import imp
import pygame 
import math,time
# official file
from main import *
human = Human(0,20)
l = ["mercury.png",'earth.png','moon.png','mars.png','saturn.png','jupiter.png']

day = human.day

def rotation(astronaut, planet, stars, ellipse , other_planet, rocket,last_planet,day):
    pygame.init()
    
    clock = pygame.time.Clock()
    FPS = 300

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    #create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("NasaProMax")

    #load astronaut
    bg = pygame.image.load(stars).convert()
    bg_height = bg.get_height()
    bg_rect = bg.get_rect()
    """astronaut = pygame.image.load(astronaut).convert_alpha()
    astronaut = pygame.transform.scale(astronaut,(200, 200))"""
    earth = pygame.image.load(f"images/{planet}").convert_alpha()
    earth = pygame.transform.scale(earth,(200, 200))
    if other_planet is not False:
        mars = pygame.image.load(f"images/{other_planet}").convert_alpha()
        mars = pygame.transform.scale(mars,(100, 100))
        

    if last_planet is not False:
        jupiter = pygame.image.load(f"images/{last_planet}").convert_alpha()
        jupiter = pygame.transform.scale(jupiter,(100, 100))
    ellipse = pygame.image.load(f"images/{ellipse}").convert_alpha()
    ellipse = pygame.transform.scale(ellipse,(250, 250))
    rocket = pygame.image.load(f"images/{rocket}").convert_alpha()
    rocket = pygame. transform. scale(rocket, (50, 50))
    w3,h3 = ellipse.get_size()
    w4,h4 = rocket.get_size()
    x = SCREEN_WIDTH/2-((w3/2)+(w4/2))
    y = SCREEN_HEIGHT/2-((h3/2)-(h4/2))
    w,h = rocket.get_size()


    #define game variables
    scroll = 0
    tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1

    #game loop
    run = True
    angle = 0
    degree = 0
    b = False
    b1 = False
    b2 = False
    
    while run:
        clock.tick(FPS)
        human.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
        #print(human.status,human.causes)
        #draw scrolling background
        for i in range(0, tiles):
            screen.blit(bg, (0, i * bg_height + scroll))
            stats = pygame.image.load("./images/stats2.png")
            stats = pygame.transform.scale(stats,(150,150))   
            screen.blit(stats,(10,10)) 
            bg_rect.y = i * bg_height + scroll
            pygame.draw.rect(screen, ("#3E2053"), bg_rect, 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pressed = pygame.key.get_pressed()

            if other_planet is not False:

                if (pressed[pygame.K_RIGHT] or b1) and not b2:
                    b1 = True
                    j1 = str(x).split('.')
                    j2 = str(y).split('.')
                    if (int(j1[0]) in [670] and int(j2[0]) in [336]):
                        print("daaaaaaaaaaaaaay1")
                        day += 1
                        print(day)

                    if (int(j1[0]) in [648,649] and int(j2[0]) in [144,145]) or b:
                        b = True
                        x += 1
                        #print('ghjkk')
                        y -= 0.37
                        rocket = pygame. transform. scale(rocket, (50, 50))
                        rotated = pygame.transform.rotate(rocket, -80)
                        screen.blit(rotated, (x,y))
                        if other_planet is not False:
                            screen.blit(mars, (SCREEN_WIDTH-(w1/2), -(h1/5)))
                        if last_planet is not False:
                            screen.blit(jupiter, ((h5), (SCREEN_HEIGHT-(1.75*h5))))
                        screen.blit(ellipse, (SCREEN_WIDTH/2-(w3/2), SCREEN_HEIGHT/2-(h3/2)))
                        screen.blit(earth, (SCREEN_WIDTH/2-(w2/2), SCREEN_HEIGHT/2-(h2/2)))
                        #screen.blit(astronaut, (0,0))
                        j1 = str(x).split('.')
                        if int(j1[0]) in [1100,1101]:
                            screen.fill((0,0,0))
                            pygame.display.flip()
                            time.sleep(0.01)
                            index = l.index(planet) + 1
                            if index == len(l):
                                planet = False
                            else :
                                planet  = l[index]

                            if last_planet == False:
                                #print('yes')
                                last_planet = l[0]
                            else:
                            
                                index = l.index(last_planet) + 1
                                if index == len(l):
                                    last_planet = False
                                else :
                                    last_planet  = l[index]
                            
                            index = l.index(other_planet) + 1
                            if index == len(l):
                                other_planet = False
                            else :
                                other_planet  = l[index]

                            rotation("Astronaut suit-pana 1.svg",planet,"stars2.png","Ellipse 1.png",other_planet,"rocket.png",last_planet,day)

            if last_planet is not False:

                if (pressed[pygame.K_LEFT] or b2) and not b1 :
                    b2 = True
                    j1 = str(x).split('.')
                    j2 = str(y).split('.')
                    if (int(j1[0]) in [670] and int(j2[0]) in [336]):
                        print("daaaaaaaaaaaaaay3")
                        day += 1
                        print(day)
                    if (int(j1[0]) in [495,496] and int(j2[0]) in [342,343]) or b:
                        b = True
                        #print('gjvb,jh')
                        x -= 1
                        y += 0.3
                        rocket = pygame. transform. scale(rocket, (50, 50))
                        rotated = pygame.transform.rotate(rocket, 100)
                        if other_planet is not False:
                            screen.blit(mars, (SCREEN_WIDTH-(w1/2), -(h1/5)))
                        if last_planet is not False:
                            screen.blit(jupiter, ((h5), (SCREEN_HEIGHT-(1.75*h5))))
                        
                        screen.blit(ellipse, (SCREEN_WIDTH/2-(w3/2), SCREEN_HEIGHT/2-(h3/2)))
                        screen.blit(earth, (SCREEN_WIDTH/2-(w2/2), SCREEN_HEIGHT/2-(h2/2)))
                        #screen.blit(astronaut, (0,0))
                        screen.blit(rotated, (x,y))
                        j1 = str(x).split('.')
                        if int(j1[0]) in [200,201]:
                            screen.fill((0,0,0))
                            pygame.display.flip()
                            time.sleep(1)
                            index = l.index(planet) - 1
                            if index == -1:
                                planet = False
                            else :
                                planet  = l[index]
                            
                            index = l.index(last_planet) - 1
                            if index == -1:
                                last_planet = False
                            else :
                                last_planet  = l[index]

                            if other_planet == False:
                                other_planet = l[-1]
                            else:
                            
                                index = l.index(other_planet) - 1
                                if index == -1:
                                    other_planet = False
                                else :
                                    other_planet  = l[index]

                            rotation("Astronaut suit-pana 1.svg",planet,"stars2.png","Ellipse 1.png",other_planet,"rocket.png",last_planet,day)

            if not b :
                j1 = str(x).split('.')
                j2 = str(y).split('.')
                if (int(j1[0]) in [670] and int(j2[0]) in [336]):
                    print("daaaaaaaaaaaaaay2")
                    day += 1
                    print(day)
                #print('here')
                #print(b,b1,b2)
                radius = w3/2
                rotated = pygame.transform.rotate(rocket, -degree)
                degree +=0.4
                center = (600-w4+30,300-h4)
                x,y = [center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)]
                #print(x,y)
                angle += 0.01
                w2,h2 = earth.get_size()
                screen.blit(earth, (SCREEN_WIDTH/2-(w2/2), SCREEN_HEIGHT/2-(h2/2)))
                if other_planet is not False:
                    w1,h1 = mars.get_size()
                    screen.blit(mars, (SCREEN_WIDTH-(w1/2), -(h1/5)))
                if last_planet is not False:
                    w5,h5 = jupiter.get_size()
                    screen.blit(jupiter, ((h5), (SCREEN_HEIGHT-(1.75*h5))))
                screen.blit(ellipse, (SCREEN_WIDTH/2-(w3/2), SCREEN_HEIGHT/2-(h3/2)))
                #screen.blit(astronaut, (0,0))
                screen.blit(rotated, (x,y))
                pygame.display.flip()


        #scroll background
        scroll -= 0.3
    #reset scroll
        if abs(scroll) > bg_height:
            scroll = 0

        pygame.display.flip()

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
  
    pygame.quit()


def inspace(planet):
    after = lambda x : False if (x.index(f"{planet}.png")==len(x)-1) else x[x.index(f"{planet}.png")+1]
    before = lambda x : False if (x.index(f"{planet}.png")==0) else x[x.index(f"{planet}.png")-1]
    rotation("Astronaut suit-pana 1.svg",f"{planet}.png","stars2.png","Ellipse 1.png",after(l),"rocket.png",before(l),day)