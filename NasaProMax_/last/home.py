from os import stat
import pygame 
import math,time
import bo3

def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)
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
logo1 = pygame.image.load("./images/group 1.png").convert_alpha()
explore = pygame.image.load("./images/group 2.png").convert_alpha()
grp3 = pygame.image.load("./images/Group 3.png").convert_alpha()
chC = pygame.image.load("./images/Choose Character.png").convert_alpha()
logo = pygame.image.load("./images/Logo.png").convert_alpha()
title = pygame.image.load("./images/Title.png").convert_alpha()
polygone1 = pygame.image.load("./images/Polygon 1.png").convert_alpha()
polygone2 = pygame.image.load("./images/Polygon 2.png").convert_alpha()
astronaut = pygame.image.load("./images/astronaut.png").convert_alpha()
bar_bg = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
bar_bg2 = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
bar_bg3 = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
bar_bg4 = pygame.image.load("./images/Rectangle 3.png").convert_alpha()
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


def home():
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
        button=pygame.draw.rect(screen, "#412161", bg_rect, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
            
                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    planetMenu()
          #scroll background
    scroll -= 0.3

  #reset scroll
    if abs(scroll) > bg_height:
        scroll = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)

    


    screen.blit(logo1, (452, 111))
    screen.blit(explore, (460, 429))

  
    pygame.display.flip()
    



  
    
    pygame.display.update()
def chooseH():
 #define game variables
 scroll = 0
 tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1
 run = True
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
    pygame.draw.rect( screen, "#EB5858", (660, 237, 219, 22),0,0,0,5,0,5)
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
    screen.blit(astronaut, (237, 150))
    screen.blit(chC, (457, 37))



   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)

    

  
    pygame.display.flip()
    



  
    
    pygame.display.update()
def chooseB():

 scroll = 0
 tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1
 run = True
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
def planetMenu():

 scroll = 0
 tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1
 run = True
 screen.blit(bg,(0,0))
 while run:
    
    screen.blit(bg, (0, 0))
    screen.blit(logo, (1060, 15))

    screen.blit(shape, (110, 114))
    #screen.blit(earth, (151, 141))
    earth = Buttonify("images/earth.png",(286, 141), screen)
    screen.blit(earthW, (185, 290))
    
    screen.blit(shape, (363, 114))
    #screen.blit(mars, (390, 121))
    mars = Buttonify("images/mars.png",(555, 121), screen)
    screen.blit(marsW, (438, 290))
    screen.blit(shape, (616, 114))
    #screen.blit(iss, (616, 168))
    iss=Buttonify("images/iss.png",(816, 168), screen)
    screen.blit(issW, (703, 290))
    screen.blit(shape, (869, 114))
    #screen.blit(saturn, (883, 107))
    saturn=Buttonify("images/saturn.png",(1071, 107), screen)
    screen.blit(saturnW, (945, 290))
    screen.blit(shape, (110, 352))
    #screen.blit(rocket, (160, 380))
    rocket=Buttonify("images/rocket.png",(275, 380), screen)
    screen.blit(shape, (363, 352))
    #screen.blit(moon, (384, 360))
    moon=Buttonify("images/moon.png",(550, 360), screen)
    screen.blit(moonW, (434, 525))
    screen.blit(shape, (616, 352))
    #screen.blit(jupiter, (647, 362))
    jupiter=Buttonify("images/jupiter.png",(802, 362), screen)
    screen.blit(jupiterW, (686, 525))
    screen.blit(shape, (869, 352))
    #screen.blit(mercury, (926, 392))
    mercury=Buttonify("images/mercury.png",(1026, 392), screen)
    screen.blit(mercuryW, (931, 525))
  
    pygame.display.flip()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse = pygame.mouse.get_pos()
            if earth[1].collidepoint(mouse):
                bo3.inspace("earth")
            if mars[1].collidepoint(mouse):
                bo3.inspace("mars")
            if moon[1].collidepoint(mouse):
                bo3.inspace("moon")
            if mercury[1].collidepoint(mouse):
                bo3.inspace("mercury")
            if jupiter[1].collidepoint(mouse):
                bo3.inspace("jupiter")
            if iss[1].collidepoint(mouse):
                labo()
            if rocket[1].collidepoint(mouse):
                bo3.inspace("earth")
            if saturn[1].collidepoint(mouse):
                bo3.inspace("saturn")          
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
    


    clock.tick(FPS)

    

'''def lab():
    pygame.display.set_caption("NasaProMax")
    bg = pygame.image.load("images/window.png").convert()
    screen.blit(bg,(0,0))
    planet = pygame.image.load("images/mars.png").convert_alpha()
    desk =  pygame.image.load("images/desk.png").convert_alpha()
    tools = pygame.image.load("images/tools.png").convert_alpha()
    microscope = pygame.image.load("images/microscope.png").convert_alpha()
    tube = pygame.image.load("images/tube.png").convert_alpha()


    run = True
    while run:
            
            screen.blit(bg, (0, 0))
            screen.blit(planet, (880, 68))
            screen.blit(desk , (-302,-76))
            screen.blit(tools, (450,210))
            #screen.blit(microscope, (170,200))
            microscope=Buttonify("images/microscope.png",(370, 200), screen)
            screen.blit(tube, (870,235))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if microscope[1].collidepoint(mouse):
                        bo3.inspace("earth")
            pygame.display.flip()                    
            pygame.display.update()

    pygame.quit()

def last_page():
    pass

def veggie():
    on = False
    bg = pygame.image.load("images/window_2.png").convert()
    desk =  pygame.image.load("images/desk.png").convert_alpha()
    junction = pygame.image.load("images/junction.png").convert_alpha()
    pillow = pygame.image.load("images/pillow.png").convert_alpha()
    lamp = pygame.image.load("images/lampOf.png").convert_alpha()
    polygon3 = pygame.image.load("images/polygon_3.png").convert_alpha() 
    polygon4 = pygame.image.load("images/polygon_4.png").convert_alpha()
    shutter = pygame.image.load("images/switch.png").convert_alpha()
    shutter = pygame.transform.scale(shutter,(70, 70))
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
                            lamp = pygame.image.load("images/lamp.png").convert_alpha()
                            screen.blit(lamp, (200,0))
                            on = True
                            pygame.display.flip()
                        else :
                            lamp = pygame.image.load("images/lampOf.png").convert_alpha()
                            screen.blit(lamp, (200,0))
                            on = False
                            pygame.display.flip()
        

    pygame.quit()

def labo():


    bg = pygame.image.load("images/window.png").convert()
    planet = pygame.image.load("images/mars.png").convert_alpha()
    desk =  pygame.image.load("images/desk.png").convert_alpha()
    tools = pygame.image.load("images/tools.png").convert_alpha()
    microscope = pygame.image.load("images/microscope.png").convert_alpha()
    tube = pygame.image.load("images/tube.png").convert_alpha()
    polygon4 = pygame.image.load("images/polygon_4.png").convert_alpha()
    polygon3 = pygame.image.load("images/polygon_3.png").convert_alpha() 

    screen.blit(bg, (0, 0))
    screen.blit(planet, (880, 68))
    screen.blit(desk , (-302,-76))
    screen.blit(tools, (450,210))
    screen.blit(microscope, (170,200))
    screen.blit(tube, (870,235))
    screen.blit(polygon4, (10,300))
    x = 1150 # x coordnate of image
    y = 300
    screen.blit(polygon3, (x,y))

    pygame.display.flip()


    run = True
    while run:
        x1,y1 = polygon3.get_size()
        x2,y2 = polygon4.get_size()
        x4 = pygame.draw.rect(screen, (255,255,255),pygame.Rect(x, y, x1,y1))
        x6 = pygame.draw.rect(screen, (255,255,255),pygame.Rect(10, 300, x2,y2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()               
                if x4.collidepoint(mouse_pos):
            # Set the x, y postions of the mouse click
                    print('here')
                    animals()
                if x6.collidepoint(mouse_pos):
            # Set the x, y postions of the mouse click
                    print('here1')
                    veggie()
    pygame.quit()

def animals():
    bg = pygame.image.load("images/animals.png").convert()
    desk =  pygame.image.load("images/desk.png").convert_alpha()
    fishes = pygame.image.load("images/fishes.png").convert_alpha()
    fishes = pygame.transform.scale(fishes,(340,200))
    rats = pygame.image.load("images/rats.png").convert_alpha()
    mars = pygame.image.load("images/mars.png").convert_alpha()
    mars = pygame.transform.scale(mars,(120,100))
    polygon3 = pygame.image.load("images/polygon_3.png").convert_alpha() 
    polygon4 = pygame.image.load("images/polygon_4.png").convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(desk , (-302,-76))
    screen.blit(fishes, (160,170))
    screen.blit(rats, (720,170))
    screen.blit(mars, (220,50))
    screen.blit(polygon3, (1150,300))
    screen.blit(polygon4, (10,300))
    pygame.display.flip()



    run = True

    while run:
            x1,y1 = polygon3.get_size()
            x2,y2 = polygon4.get_size()
            x4 = pygame.draw.rect(screen, (255,255,255),pygame.Rect(1150, 300, x1,y1))
            x6 = pygame.draw.rect(screen, (255,255,255),pygame.Rect(10, 300, x2,y2))
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()               
                    if x4.collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        pass
                    if x6.collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        print('here1')
                        labo()

    pygame.quit()'''
def last_page():
    pass

def veggie():
    on = False
    stats = pygame.image.load("images/stats.png").convert_alpha()
    stats = pygame.transform.scale(stats,(150,150))
    bg = pygame.image.load("./images/window_2.png").convert()
    desk =  pygame.image.load("./images/desk.png").convert_alpha()
    junction = pygame.image.load("./images/junction.png").convert_alpha()
    pillow = pygame.image.load("./images/pillow.png").convert_alpha()
    lamp = pygame.image.load("./images/lampOf.png").convert_alpha()
    polygon3 = pygame.image.load("./images/polygon_3.png").convert_alpha() 
    polygon4 = pygame.image.load("./images/polygon_4.png").convert_alpha()
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
    screen.blit(stats, (40,430))
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
                        polygon3 = pygame.image.load("./images/polygon_3.png").convert_alpha() 
                        polygon4 = pygame.image.load("./images/polygon_4.png").convert_alpha()
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

def labo():


    bg = pygame.image.load("./images/window.png").convert()
    stats = pygame.image.load("./images/stats.png").convert_alpha()
    stats = pygame.transform.scale(stats,(150, 150))
    planet = pygame.image.load("./images/mars.png").convert_alpha()
    desk =  pygame.image.load("./images/desk.png").convert_alpha()
    tools = pygame.image.load("./images/tools.png").convert_alpha()
    microscope = pygame.image.load("./images/microscope.png").convert_alpha()
    tube = pygame.image.load("./images/tube.png").convert_alpha()
    polygon4 = pygame.image.load("./images/polygon_4.png").convert_alpha()
    polygon3 = pygame.image.load("./images/polygon_3.png").convert_alpha() 
    xx = pygame.image.load("./images/x.png").convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(planet, (880, 68))
    screen.blit(desk , (-302,-76))
    screen.blit(tools, (450,210))
    screen.blit(tube, (870,235))
    screen.blit(stats, (40,430))
    microscope=Buttonify("./images/microscope.png",(370, 200), screen)
    polygon3 = Buttonify("./images/polygon_3.png",(1150, 300), screen)
    polygon4 = Buttonify("./images/polygon_4.png",(75, 300), screen)
    pygame.display.flip()


    run = True
    xx = [None,None]
    xx1 = [None,None]
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
                    xx = Buttonify("x.png",(500, 100), screen)
                print(xx)
                try :
                    if xx[1].collidepoint(mouse_pos):
                        bg = pygame.image.load("./images/window.png").convert()
                        planet = pygame.image.load("./images/mars.png").convert_alpha()
                        desk =  pygame.image.load("./images/desk.png").convert_alpha()
                        tools = pygame.image.load("./images/tools.png").convert_alpha()
                        microscope = pygame.image.load("./images/microscope.png").convert_alpha()
                        tube = pygame.image.load("./images/tube.png").convert_alpha()
                        polygon4 = pygame.image.load("./images/polygon_4.png").convert_alpha()
                        polygon3 = pygame.image.load("./images/polygon_3.png").convert_alpha() 
                        xx = pygame.image.load("./images/x.png").convert_alpha()
                        screen.blit(bg, (0, 0))
                        screen.blit(planet, (880, 68))
                        screen.blit(desk , (-302,-76))
                        screen.blit(tools, (450,210))
                        screen.blit(tube, (870,235))
                        microscope=Buttonify("./images/microscope.png",(370, 200), screen)
                        polygon3 = Buttonify("./images/polygon_3.png",(1150, 300), screen)
                        polygon4 = Buttonify("./images/polygon_4.png",(75, 300), screen)
                        pygame.display.flip()
                except :
                    pass
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()

def animals():
    xx = [None,None]
    screen.fill((0,0,0))
    bg = pygame.image.load("./images/animals.png").convert()
    stats = pygame.image.load("./images/stats.png").convert_alpha()
    stats = pygame.transform.scale(stats,(150, 150))
    desk =  pygame.image.load("./images/desk.png").convert_alpha()
    fishes = pygame.image.load("./images/fishes.png").convert_alpha()
    fishes = pygame.transform.scale(fishes,(150,10))
    rats = pygame.image.load("./images/rats.png").convert_alpha()
    mars = pygame.image.load("./images/mars.png").convert_alpha()
    mars = pygame.transform.scale(mars,(120,100))
    polygon3 = pygame.image.load("./images/polygon_3.png").convert_alpha() 
    polygon4 = pygame.image.load("./images/polygon_4.png").convert_alpha()
    screen.blit(bg, (0, 0))
    screen.blit(desk , (-302,-76))
    screen.blit(mars, (220,50))
    screen.blit(stats, (40,430))
    polygon3 = Buttonify("./images/polygon_3.png",(1150, 300), screen)
    polygon4 = Buttonify("./images/polygon_4.png",(75, 300), screen)
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
                    if rats[1].collidepoint(mouse_pos) or fishes[1].collidepoint(mouse_pos):
                # Set the x, y postions of the mouse click
                        p = pygame.image.load("./images/Group_vide.png").convert_alpha()
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
                            polygon3 = pygame.image.load("./images/polygon_3.png").convert_alpha() 
                            polygon4 = pygame.image.load("./images/polygon_4.png").convert_alpha()
                            screen.blit(bg, (0, 0))
                            screen.blit(desk , (-302,-76))
                            screen.blit(mars, (220,50))
                            polygon3 = Buttonify("./images/polygon_3.png",(1150, 300), screen)
                            polygon4 = Buttonify("./images/polygon_4.png",(75, 300), screen)
                            fishes = Buttonify("./images/fishes.png",(500,70), screen)
                            rats = Buttonify("./images/rats.png",(990,170), screen)
                            pygame.display.flip()
                            pygame.display.update()
                    except :
                        pass

    pygame.quit()


home()

pygame.quit()
