import imp
import pygame 
import math,time
from random import randint,uniform,uniform
# official file
#from main import *
#import home
DISTANCE_MAX = 4.3287e9
previousPressures = []
Time = 0
class Plant():
    def __init__(self):
        self.name = "Chinnese Cabbage"
        self.status = "alive"
        self.causes = []
        self.age = 0
    def checkEnv(self,temp,rad,pr):
        self.tempStatus(temp)
        self.radiationStatus(rad)
        self.pressureStatus(pr)
        print(self.status)
    def tempStatus(self,temp):
        if temp>Htemp and temp<LTemp:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("heat")
    def radiationStatus(self,rad):
        if rad>=Hrad:
            if self.status !="dead":
                self.status="dead"
                self.causes.append("radiation")
    def pressureStatus(self,pr):
        if pr>=1: 
            if self.status !="dead":
                self.status="dead"
                self.causes.append("pressure")
            
class Bacteria():
    def __init__(self):
        self.status = "alive"
        self.causes = []
        self.name = "radiodurans"
        self.age = 0
        
    def checkEnv(self,temp,rad,pr):
        self.tempStatus(temp)
        self.radiationStatus(rad)
        self.pressureStatus(pr)
        print(self.status)
    def tempStatus(self,temp):
        if temp>=Htemp:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("heat")
    def radiationStatus(self,rad):
        if rad>=Hrad:
            if self.status !="dead":
                self.status="dead"
                self.causes.append("radiation")
    def pressureStatus(self,pr):
        if pr>=8165.51567: 
            if self.status !="dead":
                self.status="dead"
                self.causes.append("pressure")
class Rat():
    def __init__(self,gender):
        self.status = "alive"
        self.gender = gender
        self.causes = []
        self.stress = 0
        self.hasFood = False
    def checkEnv(self,temp,rad,distance,pr,planet):
        self.tempStatus(temp)
        self.radiationStatus(rad)
        self.stressStatus(distance)
        self.pressureStatus(pr)
        self.gravityStatus(planet)
        print(self.status)
    def tempStatus(self,temp):
        if 20<=temp<=26:
            if self.status=="sick":
                self.status="alive"
        elif temp>Htemp and temp<LTemp:
            if self.status=="alive":
                self.status="sick"
        else:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("heat")
    def radiationStatus(self,rad):
        if rad>=Hrad:
            if self.status !="dead":
                self.status="dead"
                self.causes.append("radiation")

        elif rad>=1200:
            if self.status=="alive":
                self.status="sick"
    def pressureStatus(self,pr):
        if pr>=600: #change 
            if self.status !="dead":
                self.status="dead"
                self.causes.append("pressure")
    def stressStatus(self,distanceInKm):
        self.stress = distanceInKm/DISTANCE_MAX
        if self.hasFood:
            self.stress-=0.4
            if self.stress<0:
                self.stress = 0
            self.hasFood = False
    def gravityStatus(self,planet):
        g = calcGravity(planet,408000+planets[planet]["radius"])
        if g > 100: #modify
            if self.status != "dead":
                self.status = "dead"
class Fish():
    def __init__(self,gender):
        self.status = "alive"
        self.gender = gender
        self.causes = []
        self.hasNewWater = False
    def checkEnv(self,temp,rad,distance,planet,pr):
        self.tempStatus(temp)
        self.radiationStatus(rad)
        self.stressStatus(distance)
        self.pressureStatus(pr)
        self.gravityStatus(planet)
        print(self.status)
    def tempStatus(self,temp):
        if temp>Htemp and temp<LTemp:
            if self.status!="dead":
                self.status="dead"
                self.causes.append("temp")
    
    def radiationStatus(self,rad):
        if rad>=Hrad:
            if self.status !="dead":
                self.status="dead"
                self.causes.append("radiation")

        elif rad>=35:
            if self.status=="alive":
                self.status="sick"
    def pressureStatus(self,pr):
        if pr>=600:
            if self.status !="dead":
                self.status="dead"
                self.causes.append("pressure")
    def stressStatus(self,distanceInKm):
        self.stress = distanceInKm/DISTANCE_MAX
        if self.hasNewWater:
            self.stress-=0.4
            if self.stress<0:
                self.stress = 0
            self.hasNewWater = False
    def gravityStatus(self,planet):
        g = calcGravity(planet,408000+planets[planet]["radius"])
        if g > 100: #modify
            if self.status != "dead":
                self.status = "dead"
class Human():
    def __init__(self,gender,age):
        self.status = "alive"       # expresses the current state of our human
        self.gender = gender        # human gender
        self.age = age              # human age
        self.causes = []            # causes of death
        self.mentalHealth = 0.6     # mental health indicator between 0 to 1, expressing well being when high
        self.bones = 1              # state of bones, between 0 to 1, higher is better
        self.muscles = 1            # state of muscles, between 0 to 1, higher is better
        self.cells = 1              # state of cells, between 0 to 1, higher is better
        self.sicknesses = []        # list of sicknesses currently infecting the human
        self.earthAge = age
        self.radiation = self.age * 3 #amount of radiation effected, initialized to earth life time radiation in mSv
        self.exposedToDeath = False # determines if human has exposed himself to death by carrying deadly diseases
        self.sportToday = False
        self.inPlanet = False
        self.petDied = False
        self.wearsSuit = False
        self.deathAge = randint(80,102)
        self.day = 0
    def checkEnv(self,temp,distance,planet,pr):
        """Checks teh environment stats & updates the state of the human according (refresh)"""
        self.tempStatus(temp)
        self.radiationStatus()
        self.mentalStatus(distance)
        self.pressureStatus(pr)
        self.gravityStatus(planet)
        self.bonesMusclesStatus()
        self.mentalStatus(distance)
    def tempStatus(self,temp):
        '''Update the human state, according to the temperture'''
        if temp>Htemp and temp<LTemp :
            if self.status!="dead":
                self.status="dead"
                self.causes.append("temp")
    
    def radiationStatus(self):
        '''Update the human state, according to the radiation level & time spent exposed'''
        self.radiation = self.earthAge * 3 + Time/3.156e+7*300
        if self.radiation > 600 and not self.exposedToDeath:
            self.deathAge = randint(5,10) + self.age
            self.exposedToDeath = True
            self.sicknesses.append(("Cancer",Time,False))
            self.status = "sick"
    def pressureStatus(self,pr):
        '''Update the human state, according to the pressure level'''
        if pr>=500: #atm
            if self.status !="dead":
                self.status="dead"
                self.causes.append("pressure")
        else:
            if len(previousPressures)<4:
                previousPressures.append(pr)
            else:
                for prr in previousPressures:
                    if abs(pr-prr)>150:
                        self.sicknesses.append(("Decompression sickness",Time,"86400"))
                        self.status = "sick"
                previousPressures.remove(previousPressures[0])
                previousPressures.append(pr)
    def bonesMusclesStatus(self):
        if not self.sportToday:
            self.bones -= 0.01
            self.muscles -=0.01
            if self.bones < 0:
                self.bones = self.muscles =  0
                self.status = 'dead'
                self.causes.append("Bones losses & Atrophy")
            elif self.bones<0.5:
                self.sicknesses.append(("Bones losses & Atrophy",Time,False))
    def mentalStatus(self,distanceInKm):
        self.mentalHealth = - distanceInKm/DISTANCE_MAX*0.05 - self.petDied*0.2 + self.sportToday*0.3+randint(-1,1)*0.1
        
    def gravityStatus(self,planet):
        '''Update the human state, according to g force level'''
        g = calcGravity(planet,408000+planets[planet]["radius"])
        #print("g",g)
        if g > 80:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("G force")
    def updateTime(self):
        self.age = self.earthAge + Time/3.156e+7
        if self.age>=self.deathAge:
            self.status = "dead"
            self.causes.append("Death time arrived")
        indexesToRemove = []
        for i in range(len(self.sicknesses)):
            if self.sicknesses[i][2]:
                if Time >= self.sicknesses[i][0]+self.sicknesses[i][2]:
                    indexesToRemove.append(i)
        for l in indexesToRemove:
            del self.sicknesses[l]
PHYSICS_CONSTS = {"G":6.674e-11,"C":299792458}
planets = {"earth":{"mass":5.972e24,"radius":6371000,"heat":13.9,"radiation":300,"distance":408000,"cycle":86400,"pressure":1},
"mars":{"mass":6.39e23,"radius":3389500,"heat":-63,"radiation":240,"distance":117.87e9,"cycle":88619.616,"pressure":0.00602023},
"venus":{"mass":4.867e24,"radius":6051800,"heat":464,"radiation":0.03,"distance":255.64e9,"cycle":10.0872,"pressure":75},
"mercury":{"mass":3.285e23 ,"radius":2439700,"heat":167,"radiation":2100,"distance":114.93e9,"cycle":5.0670144e6,"pressure":10e-12},
"jupiter":{"mass":1.898e27 ,"radius":6991100,"heat":-145,"radiation":7777,"distance":592.120e9,"cycle":35733.312,"pressure":5.92154},
"moon":{"mass":7.348e22 ,"radius":1737.4,"heat":-77,"radiation":136.9,"distance":3844e5,"cycle":2551443.84,"pressure":3e-15},
"saturn":{"mass":5.683e26 ,"radius":58232,"heat":-176,"radiation":690,"distance":1370600000,"cycle":38016,"pressure":1.38169}
}

winSize = (1200,600)
stars = [((randint(150, 200), randint(150, 200), randint(150, 200)), (randint(1, winSize[0]), randint(1, winSize[1])), randint(1, 2)) for _ in range(250)]
display = pygame.display.set_mode(winSize)

def calcGravity(planet,distanceInKM=False):
    '''Calculates G force, between a plant & an object with a distance between, if no distance is given, it calculates the g force on the planet surface'''
    if not distanceInKM:
        distanceInKM=planets[planet]["radius"]
    return (PHYSICS_CONSTS["G"]*planets[planet]["mass"])/((distanceInKM)**2)
def getHeat(planet):
    '''returns the surface heat of a planet'''
    return planets[planet]["heat"]


l = ["mercury.png",'earth.png','moon.png','mars.png','saturn.png','jupiter.png']



def rotation(astronaut, planet, stars, ellipse , other_planet, rocket,last_planet):
    Time=0
    pygame.init()
    
    clock = pygame.time.Clock()
    FPS = 2000

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    #create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Endless Scroll")

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
    ellipse = pygame.transform.scale(ellipse,(5, 5))
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
    isd = 0
    while run:
        isd+=1
        if isd==100:
            run=False
            pygame.quit()
            return 100
        
        clock.tick(FPS)
        #print(human.status,human.causes)
        #draw scrolling background
        
        for i in range(0, tiles):
            screen.blit(bg, (0, i * bg_height + scroll))
            bg_rect.y = i * bg_height + scroll
            pygame.draw.rect(screen, ("#3E2053"), bg_rect, 1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pressed = pygame.key.get_pressed()
            Time+=86400
            print(1+Time//86400)
            if isinstance(user,Human):
                user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                user.updateTime()
            elif isinstance(user,Plant):
                user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
            elif isinstance(user,Bacteria):
                user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
            elif isinstance(user,Rat):
                user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],1.000276,planet[:-4])
            elif isinstance(user,Fish):
                user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
            if user.status=="dead":
                run=False
                pygame.quit()
                return 1+Time//86400
            if other_planet is not False:

                if (pressed[pygame.K_RIGHT] or b1) and not b2:
                    b1 = True
                    j1 = str(x).split('.')
                    j2 = str(y).split('.')
                    '''if (int(j1[0]) in [670] and int(j2[0]) in [336]):
                        Time+=planets[planet[:-4]]["cycle"]
                        print(1+Time//86400)
                        if isinstance(user,Human):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                            user.updateTime()
                        elif isinstance(user,Plant):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
                        elif isinstance(user,Bacteria):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
                        elif isinstance(user,Rat):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],1.000276,planet[:-4])
                        elif isinstance(user,Fish):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                        if user.status=="dead":
                            pygame.quit()
                            user.status="alive"
                            break'''
                            
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
                            #time.sleep(0.01)
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

                            rotation("Astronaut suit-pana 1.svg",planet,"images/stars2.png","Ellipse 1.png",other_planet,"rocket.png",last_planet)

            if last_planet is not False:

                if (pressed[pygame.K_LEFT] or b2) and not b1 :
                    b2 = True
                    j1 = str(x).split('.')
                    j2 = str(y).split('.')
                    '''if (int(j1[0]) in [577] and int(j2[0]) in [250]):
                        Time+=86400
                        print(1+Time//86400)
                        if isinstance(user,Human):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                            user.updateTime()
                        elif isinstance(user,Plant):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
                        elif isinstance(user,Bacteria):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
                        elif isinstance(user,Rat):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],1.000276,planet[:-4])
                        elif isinstance(user,Fish):
                            user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                        if user.status=="dead":
                            run=False
                            pygame.quit()
                            return 1+Time//86400'''
                    if (int(j1[0]) in [577] and int(j2[0]) in [250]) or b:
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

                            rotation("Astronaut suit-pana 1.svg",planet,"images/stars2.png","Ellipse 1.png",other_planet,"rocket.png",last_planet)

            if not b :
                print(x,y)
                j1 = str(x).split('.')
                j2 = str(y).split('.')
                '''if (int(j1[0]) in [670] and int(j2[0]) in [336]):
                    Time+=86400
                    print(1+Time//86400)
                    if isinstance(user,Human):
                        user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                        user.updateTime()
                    elif isinstance(user,Plant):
                        user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
                    elif isinstance(user,Bacteria):
                        user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],1.000276)
                    elif isinstance(user,Rat):
                        user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],1.000276,planet[:-4])
                    elif isinstance(user,Fish):
                        user.checkEnv(planets[planet[:-4]]["heat"],planets[planet[:-4]]["radiation"],planets[planet[:-4]]["distance"],planet[:-4],1.000276)
                    if user.status=="dead":
                            run=False
                            pygame.quit()
                            return 1+Time//86400'''

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
    after = lambda x : False if (x.index(f"{planet}")==len(x)-1) else x[x.index(f"{planet}")+1]
    before = lambda x : False if (x.index(f"{planet}")==0) else x[x.index(f"{planet}")-1]
    return rotation("Astronaut suit-pana 1.svg",f"{planet}","images/stars2.png","Ellipse 1.png",after(l),"rocket.png",before(l))
import pandas as pd
df=pd.DataFrame(columns=["type","htemp","ltemp","radth","pressure","maxdays"])
import random
maxdays=0
for i in range(4000):
    times=[]
    for j in l:
        getType=random.randint(1,4)
        if getType==1:
            user = Bacteria()
        elif getType==2:
            user = Human(0,20)
        elif getType==3:
            user = Fish(1)
        elif getType==4:
            user = Rat(0)
        while True:
            Hrad=uniform(0.001,8000) 
            Htemp=uniform(15,99)
            LTemp=uniform(-99,13)
            Hpre=uniform(0,13)
            print(df)
            test=(df[df['htemp']==Htemp])&(df[df['ltemp']==LTemp])&(df[df['radth']==Hrad])&(df[df['pressure']==Hpre])
            if len(test)==0:
                break
        times.append(inspace(j))

    list=[type(user).__name__,Htemp,LTemp,Hrad,Hpre,sum(times)/len(times)]
    df.loc[len(df.index)]=list

    #df.loc[len(df.index)] = []
df.to_csv('data.csv', index=False)
