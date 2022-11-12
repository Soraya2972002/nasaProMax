from math import sqrt
from operator import truth
from random import randint
import pygame
from pygame.locals import *
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
    def tempStatus(self,temp):
        if temp>27 and temp<-6:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("heat")
    def radiationStatus(self,rad):
        if rad>=0.021:
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
    def tempStatus(self,temp):
        if temp>=100:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("heat")
    def radiationStatus(self,rad):
        if rad>=1800000:
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
        self.gravityStatus(distance,planet)
    def tempStatus(self,temp):
        if 20<=temp<=26:
            if self.status=="sick":
                self.status="alive"
        elif 8<temp<20 and 26<temp<=32.2:
            if self.status=="alive":
                self.status="sick"
        else:
            if self.status != "dead":
                self.status = "dead"
                self.causes.append("heat")
    def radiationStatus(self,rad):
        if rad>=1500:
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
    def gravityStatus(self,distance,planet):
        g = calcGravity(planet,distance)
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
        self.gravityStatus(distance,planet)
    def tempStatus(self,temp):
        if not (26<=temp<=30):
            if self.status!="dead":
                self.status="dead"
                self.causes.append("temp")
    
    def radiationStatus(self,rad):
        if rad>=50:
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
    def gravityStatus(self,distance,planet):
        g = calcGravity(planet,distance)
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
        self.wearsSuit = True
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
        if not (20<=temp<=42.3) and not self.wearsSuit:
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
                        self.sicknesses.append(("Decompression sickness",Time,"84600"))
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
            if not self.sicknesses[i][2]:
                if Time >= self.sicknesses[i][0]+self.sicknesses[i][2]:
                    indexesToRemove.append(i)
        for l in indexesToRemove:
            del self.sicknesses[l]
PHYSICS_CONSTS = {"G":6.674e-11,"C":299792458}
planets = {"earth":{"mass":5.972e24,"radius":6371000,"heat":13.9,"radiation":300,"distance":408000},
"mars":{"mass":6.39e23,"radius":3389500,"heat":-63,"radiation":240,"distance":117.87e9},
"venus":{"mass":4.867e24,"radius":6051800,"heat":464,"radiation":0.03,"distance":255.64e9},
"mercury":{"mass":3.285e23 ,"radius":2439700,"heat":167,"radiation":2100,"distance":114.93e9},
"jupiter":{"mass":1.898e27 ,"radius":6991100,"heat":-145,"radiation":7777,"distance":592.120e9},
"moon":{"mass":7.348e22 ,"radius":1737.4,"heat":-77,"radiation":1369,"distance":3844e5},
"saturn":{"mass":5.683e26 ,"radius":58232,"heat":-176,"radiation":1369,"distance":1370600000}
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


#print(calcGravity("earth",6371000))