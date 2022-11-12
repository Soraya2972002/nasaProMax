import pygame 
#from veggie import screen1
def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NasaProMax")

def last_page():
    pass

def veggie():
    on = False
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

labo()