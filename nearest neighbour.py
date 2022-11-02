from __future__ import annotations
import random
import itertools as it
from turtle import color, width
import matplotlib.pyplot as plt
from Graph import Graph
from Knoten import Knoten

class Knoten(object):
    def __init__(self, name, xKoordinate, yKoordinate, besucht):
        self.name = name
        self.x = xKoordinate
        self.y = yKoordinate
        self.besucht = besucht
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

    def getDistance(self, startKnoten, zielKnoten):
        return ((startKnoten.x - zielKnoten.x) ** 2 + (startKnoten.y - zielKnoten.y) ** 2) ** 0.5
        
class Graph(object):
    def __init__(self):
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

def randomGraph(g:Graph, anzahlKnoten:int, besucht:bool):
    for i in range(anzahlKnoten):
        xKoordinate = int(random.randint(0,100))
        yKoordinate = int(random.randint(0,100))
        g.addKnoten(i, xKoordinate, yKoordinate, besucht)

    for knoten in g.KnotenMenge:
        for i in range(len(g.KnotenMenge)):
            if i+1 == anzahlKnoten:
                break
            elif knoten.name >= i+1:
                continue
            else:
                g.addKante(g.KnotenMenge[knoten.name], g.KnotenMenge[i+1], g.KnotenMenge[knoten.besucht])

def nearestNeighbour(g:Graph, startKnotenName:int):
    global besuchteKnoten 
    startKnoten = g.getKnoten(startKnotenName)
    startKnoten.besucht = True
    besuchteKnoten = [startKnoten]
    fremdeKnoten = []
    for knoten in g.getAlleKnoten():
        if not knoten.name == startKnoten.name:
            fremdeKnoten.append(knoten)
            
    erster = besuchteKnoten[0]
      
    for i in range(len(fremdeKnoten)-1):
        kuerzesterWeg = 2**0.5*100
        ausgangsKnoten = besuchteKnoten[0]
        nachbarn = g.getAlleNachbarn(ausgangsKnoten.name)
        for nachbar in nachbarn:     
            distance = g.getDistance(ausgangsKnoten, nachbar)
            
            if kuerzesterWeg > distance and nachbar.besucht == False:
                kuerzesterWeg = distance
                naehsterNachbar = nachbar

        naehsterNachbar.besucht = True
        besuchteKnoten.append(naehsterNachbar)   
                    
    besuchteKnoten.append(erster)
    for knoten in besuchteKnoten:
        print("besuchteKnoten: ",knoten.name)

#Visualisierung
def visualisierung(startKnoten):
    yWerte = []
    xWerte = []
    xAbstand = []
    yAbstand = []
    for knoten in besuchteKnoten:
        if startKnoten == knoten.name:
            plt.text(knoten.x +1, knoten.y +1, str(knoten.name)+ " startknoten", color="black")
        plt.text(knoten.x +1, knoten.y +1,knoten.name, color="black")
        yWerte.append(knoten.y)
        xWerte.append(knoten.x)
    

    print("y: ",yWerte)
    print("x: ",xWerte)

    plt.scatter(xWerte, yWerte,color='green', s=200)
    
    #abstände
    for knoten in besuchteKnoten:
        current = knoten
        for i in range(len(besuchteKnoten)):
            if i + 1 < len(besuchteKnoten) and i - 1 >= 0:
                next = besuchteKnoten[i]
                xLen = next.x - current.x
                yLen = next.y - current.y
                xAbstand.append(xLen)
                yAbstand.append(yLen)
                current = next

        #letzten Abstand hinzufügen
        xLen = knoten.x - current.x
        yLen = knoten.y - current.y
        xAbstand.append(xLen)
        yAbstand.append(yLen)
        break

    #arrows
    xWerte.pop()
    yWerte.pop()
    for a,b,c,d in it.zip_longest(xWerte, yWerte, xAbstand, yAbstand):
        plt.arrow(a,b,c,d, width=.2, facecolor = "red", edgecolor="black")
    
    plt.title("Nearest Neighbour")
    plt.xlabel("X-Werte")
    plt.ylabel("Y-Werte")
    plt.show()

#Initialisierung des Graphen
g = Graph()
randomGraph(g, 5, False)

startKnoten = 2
#Berechnung des kürzesten Weges
nearestNeighbour(g, startKnoten)

#Visualisiere Graph
visualisierung(startKnoten)




