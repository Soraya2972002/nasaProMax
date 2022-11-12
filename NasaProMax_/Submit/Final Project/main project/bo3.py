import imp
import pygame 
import math,time
# official file
from main import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NasaProMax")

def labo():


    bg = pygame.image.load("./images/window.png").convert()
    planet = pygame.image.load("./images/mars.png").convert_alpha()
    desk =  pygame.image.load("./images/desk.png").convert_alpha()
    tools = pygame.image.load("./images/tools.png").convert_alpha()
    microscope = pygame.image.load("./images/microscope.png").convert_alpha()
    polygon4 = pygame.image.load("./images/Polygon_4.png").convert_alpha()
    polygon3 = pygame.image.load("./images/Polygon_3.png").convert_alpha() 
    xx = pygame.image.load("./images/x.png").convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(desk , (-302,-76))
    screen.blit(tools, (450,210))
    microscope=Buttonify("./images/microscope.png",(370, 200), screen)
    polygon3 = Buttonify("./images/Polygon_3.png",(1150, 300), screen)
    polygon4 = Buttonify("./images/Polygon_4.png",(75, 210), screen)
    tube=Buttonify("./images/tube.png",(1000, 210), screen)
    planet = Buttonify("./images/mars.png",(880, 68), screen)
    pygame.display.flip()


    run = True
    xx = [None,None]
    while run:
        """x2,y2 = microscope.get_size()
        x8 = pygame.draw.rect(screen, (255,255,255),pygame.Rect(170, 200, x2,y2))"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()               
                if polygon3[1].collidepoint(mouse_pos):
            # Set the x, y postions of the mouse click
                    print('here')
                    animals()
                if polygon4[1].collidepoint(mouse_pos):
            # Set the x,  postions of the mouse click
                    print('here1')
                    veggie()
                if microscope[1].collidepoint(mouse_pos): # for the microscope
                # here its for the bactery
                    p = pygame.image.load("./images/Group_bacterie.png").convert_alpha()
                    p = pygame.transform.scale(p,(600,400))
                    x2,y2 = p.get_size()
                    screen.blit(p, (((SCREEN_WIDTH//2) -x2//2) , ((SCREEN_HEIGHT//2) -y2//2)))
                    xx = Buttonify("images/x.png",(500, 100), screen)
                    pygame.display.flip()
                if tube[1].collidepoint(mouse_pos): # for the microscope
                # here its for the bactery
                    p = pygame.image.load("./images/Group_human.png").convert_alpha()
                    p = pygame.transform.scale(p,(600,400))
                    x2,y2 = p.get_size()
                    screen.blit(p, (((SCREEN_WIDTH//2) -x2//2) , ((SCREEN_HEIGHT//2) -y2//2)))
                    xx = Buttonify("images/x.png",(500, 100), screen)
                    pygame.display.flip()
                if planet[1].collidepoint(mouse_pos): # for the microscope
                # here its for the bactery
                    inspace("earth")
                    
                try :
                    if xx[1].collidepoint(mouse_pos):
                        bg = pygame.image.load("./images/window.png").convert()
                        planet = pygame.image.load("./images/mars.png").convert_alpha()
                        desk =  pygame.image.load("./images/desk.png").convert_alpha()
                        tools = pygame.image.load("./images/tools.png").convert_alpha()
                        microscope = pygame.image.load("./images/microscope.png").convert_alpha()
                        polygon4 = pygame.image.load("./images/Polygon_4.png").convert_alpha()
                        polygon3 = pygame.image.load("./images/Polygon_3.png").convert_alpha() 
                        xx = pygame.image.load("./images/x.png").convert_alpha()
                        screen.blit(bg, (0, 0))
                        screen.blit(desk , (-302,-76))
                        screen.blit(tools, (450,210))
                        microscope=Buttonify("./images/microscope.png",(370, 200), screen)
                        polygon3 = Buttonify("./images/Polygon_3.png",(1150, 300), screen)
                        polygon4 = Buttonify("./images/Polygon_4.png",(75, 300), screen)
                        tube=Buttonify("./images/tube.png",(1000, 210), screen)
                        planet = Buttonify("./images/mars.png",(880, 68), screen)
                        pygame.display.flip()
                except :
                    pass
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()

def last_page():
    pass

def veggie():
    on = False
    bg = pygame.image.load("./images/window_2.png").convert()
    desk =  pygame.image.load("./images/desk.png").convert_alpha()
    junction = pygame.image.load("./images/junction.png").convert_alpha()
    pillow = pygame.image.load("./images/pillow.png").convert_alpha()
    lamp = pygame.image.load("./images/lampOf.png").convert_alpha()
    polygon3 = pygame.image.load("./images/Polygon_3.png").convert_alpha() 
    polygon4 = pygame.image.load("./images/Polygon_4.png").convert_alpha()
    shutter = pygame.image.load("./images/switch.png").convert_alpha()
    shutter = pygame.transform.scale(shutter,(70, 70))
    xx = pygame.image.load("./images/x.png").convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(shutter, (50, 50))
    screen.blit(desk , (-302,-76))
    screen.blit(junction, (600,180))
    screen.blit(pillow, (150,320))
    screen.blit(lamp, (200,0))
    screen.blit(polygon3, (1150,300))
    screen.blit(polygon4, (10,300))
    pygame.display.flip()

    run = True
    
    while run:
            x1,y1 = polygon3.get_size()
            x2,y2 = polygon4.get_size()
            x4 = pygame.draw.rect(screen, "#B8D3F2",pygame.Rect(1150, 300, x1,y1),1)
            x6 = pygame.draw.rect(screen, "#B8D3F2",pygame.Rect(10, 300, x2,y2),1)
            x2,y2 = shutter.get_size()
            x8 = pygame.draw.rect(screen, "#B8D3F2",pygame.Rect(50, 50, x2,y2),1)
            x2,y2 = pillow.get_size()
            x9 = pygame.draw.rect(screen, "#B8D3F2",pygame.Rect(150, 320, x2,y2),1)
            x10 = None
            try :
                x2,y2 = xx.get_size()
                x10 = pygame.draw.rect(screen, "#B8D3F2",pygame.Rect(400, 100, x2,y2),1)
            except:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()               
                    if x4.collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        print('here')
                        labo()
                    if x6.collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        print('here1')
                        pass
                    if x8.collidepoint(mouse_pos):
                        if not on :
                            lamp = pygame.image.load("./images/lamp.png").convert_alpha()
                            screen.blit(lamp, (200,0))
                            on = True
                            pygame.display.flip()
                        else :
                            lamp = pygame.image.load("./images/lampOf.png").convert_alpha()
                            screen.blit(lamp, (200,0))
                            on = False
                            pygame.display.flip()
                    if x9.collidepoint(mouse_pos):
                        p = pygame.image.load("./images/Group_plante.png").convert_alpha()
                        p = pygame.transform.scale(p,(600,400))
                        x2,y2 = p.get_size()
                        screen.blit(p, (((SCREEN_WIDTH//2) -x2//2) , ((SCREEN_HEIGHT//2) -y2//2)))
                        screen.blit(xx, (400,100))
                        x2,y2 = xx.get_size()
                        x10 = pygame.draw.rect(screen, "#B8D3F2",pygame.Rect(400, 100, x2,y2),1)
                        pygame.display.flip()
                    print(x10)
                    print(mouse_pos)
                    if x10.collidepoint(mouse_pos):
                        bg = pygame.image.load("./images/window_2.png").convert()
                        desk =  pygame.image.load("./images/desk.png").convert_alpha()
                        junction = pygame.image.load("./images/junction.png").convert_alpha()
                        pillow = pygame.image.load("./images/pillow.png").convert_alpha()
                        lamp = pygame.image.load("./images/lampOf.png").convert_alpha()
                        polygon3 = pygame.image.load("./images/Polygon_3.png").convert_alpha() 
                        polygon4 = pygame.image.load("./images/Polygon_4.png").convert_alpha()
                        shutter = pygame.image.load("./images/switch.png").convert_alpha()
                        shutter = pygame.transform.scale(shutter,(70, 70))
                        xx = pygame.image.load("./images/x.png").convert_alpha()
                        screen.fill((0,0,0))
                        screen.blit(bg, (0, 0))
                        screen.blit(shutter, (50, 50))
                        screen.blit(desk , (-302,-76))
                        screen.blit(junction, (600,180))
                        screen.blit(pillow, (150,320))
                        screen.blit(lamp, (200,0))
                        screen.blit(polygon3, (1150,300))
                        screen.blit(polygon4, (10,300))
                        pygame.display.flip()
                        pygame.display.update()
        

    pygame.quit()

def animals():
    xx = [None,None]
    screen.fill((0,0,0))
    bg = pygame.image.load("./images/animals.png").convert()
    desk =  pygame.image.load("./images/desk.png").convert_alpha()
    fishes = pygame.image.load("./images/fishes.png").convert_alpha()
    fishes = pygame.transform.scale(fishes,(150,10))
    rats = pygame.image.load("./images/rats.png").convert_alpha()
    mars = pygame.image.load("./images/mars.png").convert_alpha()
    mars = pygame.transform.scale(mars,(120,100))
    polygon3 = pygame.image.load("./images/Polygon_3.png").convert_alpha() 
    polygon4 = pygame.image.load("./images/Polygon_4.png").convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(desk , (-302,-76))
    screen.blit(mars, (220,50))
    polygon3 = Buttonify("./images/Polygon_3.png",(1150, 300), screen)
    polygon4 = Buttonify("./images/Polygon_4.png",(75, 300), screen)
    fishes = Buttonify("./images/fishes.png",(500,70), screen)
    rats = Buttonify("./images/rats.png",(990,170), screen)
    pygame.display.flip()



    run = True

    while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()                
                    if polygon3[1].collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        pass
                    if polygon4[1].collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        print('here1')
                        labo()
                    if rats[1].collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        p = pygame.image.load("./images/Group_animal.png").convert_alpha()
                        p = pygame.transform.scale(p,(600,400))
                        x2,y2 = p.get_size()
                        screen.blit(p, (((SCREEN_WIDTH//2) -x2//2) , ((SCREEN_HEIGHT//2) -y2//2)))
                        xx = Buttonify("./images/x.png",(500, 100), screen)
                        pygame.display.flip()
                    if fishes[1].collidepoint(mouse_pos):
                        p = pygame.image.load("./images/Group_fish.png").convert_alpha()
                        p = pygame.transform.scale(p,(600,400))
                        x2,y2 = p.get_size()
                        screen.blit(p, (((SCREEN_WIDTH//2) -x2//2) , ((SCREEN_HEIGHT//2) -y2//2)))
                        xx = Buttonify("./images/x.png",(500, 100), screen)
                        pygame.display.flip()
                    try :
                        if xx[1].collidepoint(mouse_pos):
                            screen.fill((0,0,0))
                            bg = pygame.image.load("./images/animals.png").convert()
                            desk =  pygame.image.load("./images/desk.png").convert_alpha()
                            fishes = pygame.image.load("./images/fishes.png").convert_alpha()
                            fishes = pygame.transform.scale(fishes,(150,10))
                            rats = pygame.image.load("./images/rats.png").convert_alpha()
                            mars = pygame.image.load("./images/mars.png").convert_alpha()
                            mars = pygame.transform.scale(mars,(120,100))
                            polygon3 = pygame.image.load("./images/Polygon_3.png").convert_alpha() 
                            polygon4 = pygame.image.load("./images/Polygon_4.png").convert_alpha()
                            screen.blit(bg, (0, 0))
                            screen.blit(desk , (-302,-76))
                            screen.blit(mars, (220,50))
                            polygon3 = Buttonify("./images/Polygon_3.png",(1150, 300), screen)
                            polygon4 = Buttonify("./images/Polygon_4.png",(75, 300), screen)
                            fishes = Buttonify("./images/fishes.png",(500,70), screen)
                            rats = Buttonify("./images/rats.png",(990,170), screen)
                            pygame.display.flip()
                            pygame.display.update()
                    except :
                        pass

    pygame.quit()


def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)
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

    """button1 = pygame.image.load("images/saturn.png").convert_alpha()
    button1 = pygame.transform.scale(button1,(50, 50))"""

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
    button1=Buttonify("images/saturn.png",(800, 800), screen)
    pygame.display.flip()
    while run:
        clock.tick(FPS)
        human.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
        #print(human.status,human.causes)
        #draw scrolling background
        stats = pygame.image.load("./images/stats2.png")
        for i in range(0, tiles):
            screen.blit(bg, (0, i * bg_height + scroll))
            stats = pygame.transform.scale(stats,(150,150))   
            screen.blit(stats,(10,10)) 
            bg_rect.y = i * bg_height + scroll
            pygame.draw.rect(screen, ("#3E2053"), bg_rect, 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Set the x, y postions of the mouse click
                        labo()
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
                        screen.blit(button1,(0,400))
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

                            rotation("Astronaut suit-pana 1.svg",planet,"images/stars2.png","Ellipse 1.png",other_planet,"rocket.png",last_planet,day)

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

                            rotation("Astronaut suit-pana 1.svg",planet,"images/stars2.png","Ellipse 1.png",other_planet,"rocket.png",last_planet,day)

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
        pygame.display.update()


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
    rotation("Astronaut suit-pana 1.svg",f"{planet}.png","images/stars2.png","Ellipse 1.png",after(l),"rocket.png",before(l),day)
