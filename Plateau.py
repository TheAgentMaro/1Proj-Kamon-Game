import math
from math import *
import random
from PIL import Image, ImageTk

class Plateau: 
     
    #------------------------------------ # Constructeur #------------------------------------#  
    
    def __init__(self, rayon, PlateauSize, centerX, centerY, listLogo, listColor):
        
        # Hexagone
        self.__rayon = rayon
        self.__height = math.sqrt(3)*rayon
        
        # Plateau
        self.__PlateauSize = PlateauSize
        self.__centerX = centerX
        self.__centerY = centerY
        self.__ring = self.ring()
        
        # Case
        self.__dic = self.createDic(listLogo, listColor)
    
    #------------------------------------# Get functions       #------------------------------------#
    
    def getDic(self):
        return self.__dic
    
    def getHeight(self):
        return self.__height
    
    def getRayon(self):
        return self.__rayon
    
    def getRing(self):
        return self.__ring
    
    #------------------------------------
    # Anneaux
    #------------------------------------
    
    def ring(self):
        if self.__PlateauSize == 37:
            return 3
        if self.__PlateauSize == 61:
            return 4
        if self.__PlateauSize == 91:
            return 5
    
    #------------------------------------
    # Dictionnaire de cases
    #------------------------------------
    
    # Création des clés et des coordonnées
    def generateCoord(self):
        dic = {}
        position = (self.__centerX, self.__centerY)
        coordKey = [0, 0, 0]
        self.addDic(dic, coordKey, position)
        for i in range(self.__ring+1):
            for _ in range(i):
                coordKey[1] -= 1
                coordKey[2] += 1
                position = self.axeDeplacement("r", -1.1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[2] -= 1
                coordKey[0] += 1
                position = self.axeDeplacement("s", -1.1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[2] -= 1
                coordKey[1] += 1
                position = self.axeDeplacement("r", 1.1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[0] -= 1
                coordKey[1] += 1
                position = self.axeDeplacement("q", -1.1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[0] -= 1
                coordKey[2] += 1
                position = self.axeDeplacement("s", 1.1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            for _ in range(i):
                coordKey[1] -= 1
                coordKey[2] += 1
                position = self.axeDeplacement("r", -1.1, position[0], position[1])
                self.addDic(dic, coordKey, position)
            if i > 1:
                for _ in range(i-1):
                    coordKey[1] -= 1
                    coordKey[0] += 1
                    position = self.axeDeplacement("q", 1.1, position[0], position[1])
                    self.addDic(dic, coordKey, position)
            position = (self.__centerX, self.__centerY)
            coordKey = [0, 0, 0]
        return dic
    
    # Ajouts des clés et des coordonnées
    def addDic(self, dic, coordKey, position):
        coordKey = tuple(coordKey)
        dic[coordKey] = [position]
        coordKey = list(coordKey)
    
    # Creer une liste aleatoire de 7 png
    def randomPng(self, listPng):
        random.shuffle(listPng)
        sixPng = [""]
        for i in range(6):
            sixPng.append(self.image(listPng[i], round((self.__centerX+0.60*self.__rayon)-(self.__centerX-0.60*self.__rayon)), round((self.__centerY+0.60*self.__rayon)-(self.__centerY-0.60*self.__rayon))))
        return sixPng
    
    # Création des couleurs et des logos
    def colorLogo(self, listLogo, listColor):
        case = []
        Logo = self.randomPng(listLogo)
        for i in range(1, 7):
            for j in range((self.__PlateauSize-1)//6):
                case += [(Logo[i], listColor[j+1])]
        case += [(Logo[0], listColor[0])]
        return case
    
    # Ajouts des couleurs et des logos   
    def addColorLogo(self, listLogo, dic, listColor):
        case = self.colorLogo(listLogo, listColor)
        listKey = []
        for key in dic:
            listKey.append(key)
        random.shuffle(listKey)
        x = 0
        for i in range(len(listKey)):
            dic[listKey[i]] += [case[x]]
            x += 1
    
    # Ajouts de l'état des cases
    def addState(self, dic):
        for value in dic.values():
            value += ["vide"]
            
    # Création du dictionnaire
    def createDic(self, listLogo, listColor):
        dic = self.generateCoord()
        self.addColorLogo(listLogo, dic, listColor)
        self.addState(dic)
        return dic
            
    #------------------------------------
    # Coordonnées des coins d'un hexagone
    #------------------------------------
    
    def generateCoordCorner(self, x, y, rayon):
        return [(x+rayon, y), 
                (rayon*math.cos(pi/3)+x, rayon*math.sin(pi/3)+y), 
                (-(rayon*math.cos(pi/3))+x, rayon*math.sin(pi/3)+y), 
                (x-rayon, y), 
                (-(rayon*math.cos(pi/3))+x, -(rayon*math.sin(pi/3))+y), 
                (rayon*math.cos(pi/3)+x, -(rayon*math.sin(pi/3))+y)]
        
    #------------------------------------
    # Coordonnées d'un cercle
    #------------------------------------
        
    def generateCoordCircle(self, x, y, rayon):
        return [(x-0.60*rayon, y-0.60*rayon), (x+0.60*rayon, y+0.60*rayon)]
    
    #------------------------------------
    # Deplacement de case en case
    #------------------------------------
    
    def axeDeplacement(self, axe, deplacement, x, y):
        if axe == "q":
            return (self.__rayon*1.5*deplacement+x, -(self.__height/2)*deplacement+y)
        if axe == "r":
            return (x, self.__height*deplacement+y)
        if axe == "s":
            return (-(self.__rayon*1.5)*deplacement+x, -(self.__height/2)*deplacement+y)
        
    #------------------------------------   
    # Changer la taille d'une image
    #------------------------------------  

    def image(self, image, width, height):
        file = Image.open(image)
        file = file.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(file)
    
    