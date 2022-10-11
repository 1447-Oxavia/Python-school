import random
#import matplotlib as npl
#import matplotlib.pyplot as plt 
#import numpy as np


class Knoten(object):
    def __init__(self, name, xKoordinate, yKoordinate, besucht):
        self.name = name
        #self.laenge = ((nameStartKnoten.x - nameZielKnoten.x) ** 2 + (nameStartKnoten.y - nameZielKnoten.y) ** 2) ** (0.5)
        self.x = xKoordinate
        self.y = yKoordinate
        self.besucht = False
        self.vorgaenger = []

    def getX(self):
        return self.x

    def setX(self, neuesX:int):
        self.x = neuesX
        return self.x

    def getY(self):
        return self.y
    
    def setY(self, neuesY:int):
        self.y = neuesY
        return self.y

    def addVorgaenger(self, vorgaengerName:int):
        self.vorgaenger.append(vorgaengerName)
        
    def getVorgaenger(self):
        return self.vorgaenger
    
    def setName(self, randomName:int):
        self.name = randomName
        return self.name

    def getName(self):
        return self.name
            
class Graph(object):
    def __init__(self, ):
        self.KnotenMenge = []
        self.KantenMenge = []

    def getAlleKnoten(self):
        return self.KnotenMenge

    def existiertKnoten(self, nameKnoten:int):
        for knoten in self.KnotenMenge:
            if knoten == nameKnoten:
                return True
            else:
                return False

    def addKnoten(self, nameKnoten:int, xKoordinate:int, yKoordinate:int, besucht:bool):
        k = Knoten(nameKnoten, xKoordinate, yKoordinate, besucht)
        self.KnotenMenge.append(k)
       

    def getKnoten(self, nameKnoten:int):
        for knoten in self.KnotenMenge:
            if knoten.name == nameKnoten:
                return knoten

    def delKnoten(self, nameKnoten:int):
        for knoten in self.KnotenMenge:
            if knoten.name == nameKnoten:
                self.KnotenMenge.remove(nameKnoten)
            else:
                print("Kein Knoten mit diesem Namen")
    

    def existiertKante(self, nameStartKnoten:int, nameZielKnoten:int):
        for kante in self.KantenMenge:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                return True
            else:
                return False

    def addKante(self, nameStartKnoten:Knoten, nameZielKnoten:Knoten, besucht:Knoten):
        laenge = ((nameStartKnoten.x - nameZielKnoten.x) ** 2 + (nameStartKnoten.y - nameZielKnoten.y) ** 2) ** (0.5)
        self.KantenMenge.append([nameStartKnoten.name , nameZielKnoten.name, laenge, besucht.besucht])

    def getDistance(self, startKnoten, zielKnoten):
        return ((startKnoten.x - zielKnoten.x) ** 2 + (startKnoten.y - zielKnoten.y) ** 2) ** 0.5

    def delKante(self, nameStartKnoten:int, nameZielKnoten:int):
        for kante in self.KantenMenge:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                self.KantenMenge.remove(kante)


    def getAlleNachbarn(self, nameKnoten:int):
        nachbarn = []
        for kante in self.KantenMenge:
            if kante[0] == nameKnoten:
                nachbarn.append(self.getKnoten(kante[1]))
            elif kante[1] == nameKnoten:
                nachbarn.append(self.getKnoten(kante[0]))
        return nachbarn

        print(nachbarn)
        print('Maul')
    
g = Graph()

def getVerbindung():
    for knoten in g.getAlleKnoten():
        print(knoten.name, ":", g.getAlleNachbarn(knoten.name))

def randomGraph(anzahlKnoten:int):

    for i in range(anzahlKnoten):
        xKoordinate = int(random.randint(0,100))
        yKoordinate = int(random.randint(0,100))
        besucht = False
        g.addKnoten(i, xKoordinate, yKoordinate, besucht)

    for knoten in g.KnotenMenge:
        for i in range(len(g.KnotenMenge)):
            if i+1 == anzahlKnoten:
                break
            elif knoten.name >= i+1:
                continue
            else:
                g.addKante(g.KnotenMenge[knoten.name], g.KnotenMenge[i+1], g.KnotenMenge[knoten.besucht])
    
randomGraph(10)

xKoordinate = int(random.randint(0,100))
yKoordinate = int(random.randint(0,100))

def nearestNeighbour(g:Graph, startKnoten:int, xKoordinate:int, yKoordinate:int, besucht:bool):

    besuchteKnoten = [Knoten(startKnoten, xKoordinate, yKoordinate, besucht)]
    fremdeKnoten = g.getAlleKnoten()
    erster = besuchteKnoten[0]
    naesterNachbar = 0
    
    for i in range(len(fremdeKnoten)-1):
        kuerzesterWeg = 100
        ausgangsKnoten = besuchteKnoten[0]
        nachbarn = g.getAlleNachbarn(ausgangsKnoten.name)
              
        for nachbar in nachbarn:     
            y = nachbar.name
            distance = g.getDistance(ausgangsKnoten, nachbar)
            
            if kuerzesterWeg > distance and nachbar.besucht == False:
                kuerzesterWeg = distance
                naehsterNachbar = nachbar
            nachbar.besucht = True
        besuchteKnoten.append(nachbar)   
                    
        startKnoten = naehsterNachbar
    print("besuchteKnoten: ",besuchteKnoten)
    
nearestNeighbour(g,0,xKoordinate,yKoordinate, True)









