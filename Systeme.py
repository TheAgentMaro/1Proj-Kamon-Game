from Plateau import Plateau
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import math
from math import *
from random import *

class Game:
    
    #------------------------------------ # Constructeur #------------------------------------# 
    
    def __init__(self, canvas, canvasConfig, PlateauSize, rayon, listlogos, listColor, colorPlateau, colorPlayer1, colorPlayer2, bgCase):
        
        # Le canvas
        self.__canvasPlateau = canvas
        self.__canvasPlateau.bind('<Button-1>', self.Game)
        
        # Objet Plateau
        self.__bgCase = bgCase
        self.__rayon = rayon
        self.__borderdWidth = 10
        self.__Plateau = Plateau(rayon, PlateauSize, canvasConfig[0], canvasConfig[1], listlogos, listColor)
        self.__dic = self.__Plateau.getDic()
        self.__ring = self.__Plateau.getRing()  #retourne la valeur de la clé donnée si elle est présente dans le dictionnaire
        self.__colorPlateau = colorPlateau
        #self.__PlateauSize = 37

        # Dernier coups joué
        self.__lastHit = ()
        
        # Joueur actuel
        self.__player1 = 1
        self.__player2 = 2
        self.__colorPlayer1 = colorPlayer1
        self.__colorPlayer2 = colorPlayer2
        self.__player = self.__player1
        self.__colorPlayer = self.__colorPlayer1
        
        #Compteur des pions
        self.player1total = 0
        self.player2total = 0

        #bords
        self.__up_orange1 = [(1,-3,2)]
        self.__up_orange2 = [(2,-3,1)]
        
        self.__down_orange1 = [(-1,3,-2)]
        self.__down_orange2 = [(-2,3,-1)]
        
        self.__up_blue1 = [(-1,-2,3)]
        self.__up_blue2 = [(-2,-1,3)]
        
        self.__down_blue1 = [(1,2,-3)]
        self.__down_blue2 = [(2,1,-3)]
        
        self.__gauche_vert1 = [(3,-2,-1)]
        self.__gauche_vert2 = [(3,-1,-2)]
        
        self.__droite_vert1 = [(-3,1,2)]
        self.__droite_vert2 = [(-3,2,1)]
        
        #Liste des hexagones passé par
        self._player1detect =[]
        self._player2detect =[]
        

    
    def Game(self, event):
        """
        Role : Game de je un par un 

        :param event: position du souris 
        """ 
        key = self.where(event.x, event.y)
        if key != "no":
            value = self.__dic[key]
            if self.premierCoup(key, self.__ring):
                self.put(value) #value = [(951.5, 249.9481317257946), (<PIL.ImageTk.PhotoImage object at 0x00000189675F12D0>, 'red'), 'black']
                self.changePlayer()
                if value[2] == 'white':
                    self.player1total = self.player1total + 1
                    self._player1detect.append(key)
                    print('WHITE Player list :' , self._player1detect)
                if value[2] == 'black':
                    self.player2total = self.player2total + 1
                    self._player2detect.append(key)
                    print('BLACK Player list :' , self._player2detect)
                print('Joueur White Totale Pion Posé :', self.player1total,'Joueur Black Totale Pion Posé :', self.player2total)
                self.checkbord()

    
    def premierCoup(self, key, ring):
        """
        Role : Verifier le premier coup ou elle est possible (position)

        
        :param key: dict
        :param ring: prendre la valeur de la dict key
        
        return 1 : assigner les coordonnées dans le varibale ring
        return 2 : vérifier si c possible ou non 
        """ 
        if self.__lastHit == ():
            return ((key[0] == ring or key[0] == -ring) and (key[1] != ring or key[1] != -ring) and (key[2] != ring or key[2] != -ring)) ^ ((key[1] == ring or key[1] == -ring) and (key[2] != ring or key[2] != -ring) and (key[0] != ring or key[0] != -ring)) ^ ((key[2] == ring or key[2] == -ring) and (key[1] != ring or key[1] != -ring) and (key[0] != ring or key[0] != -ring))
        if self.__lastHit != ():
            return self.possible(key)
             

    
    def possible(self, key):
        """
        Role : cette fonction vérifie si c'est possible de plaçer un pion ou non sinon retourner le joueur qui a gangé

        :param key: dic [coords]

        :return: True or False
        """ 
        value = self.__dic[key]
        if value[1][0] != "":
            if value[2] == "vide":
                if self.__lastHit == () or self.__lastHit[0] == value[1][0] or self.__lastHit[1] == value[1][1]:
                    return True
                elif self.__lastHit != () and self.__lastHit[0] != value[1][0] or self.__lastHit[1] != value[1][1]:
                    #return self.winner()
                    pass
        return False

                
    def where(self, x, y):
        """
        Quel hexagone ?
        Role : détecter ou on peut plaçer un pion sur l'hexagone dans le plateau
        
        Value : [(489.5, 650.0518682742054), (<PIL.ImageTk.PhotoImage object at 0x000002ADEF7D1300>, 'orange'), 'vide']
                [(374.0, 583.3679121828036), (<PIL.ImageTk.PhotoImage object at 0x000002ADEF7D1090>, 'orange'), 'vide']

        :param x: int
        :param y: int
        
        
        :return None si on peut pas plaçer un pion dans une position donner dans le plateau
        """ 
        for value in self.__dic.values():
            if math.sqrt((value[0][0] - x)*(value[0][0] - x) + (value[0][1] - y)*(value[0][1] - y)) < self.__Plateau.getHeight()/2:
                key = self.getKey(value)
                return key
        return "no"
    
    
    def getKey(self, val):
        """
        Role : Trouve la clé de l'hexagone avec sa valeur

        :param val: describe about parameter p1
    
        :return: retournce le clé de l'hexagone courant forme (q , r , s)
        """ 
        
        for key, value in self.__dic.items():
            if val == value:
                print(key)
                return key #(q , r , s)
     
           
    def put(self, value):
        """
        Role : mettre le pion du joueur correspond à son couleur et enregistre le coup

        :param Value : describe about parameter p1

        :return: describe what it returns
        """ 
        value[2] = self.__colorPlayer

        
        self.__lastHit = (value[1][0], value[1][1]) #logo , coleur
        
        listCoordCorner = self.__Plateau.generateCoordCorner(value[0][0], value[0][1], self.__rayon*0.9)
        
        listCoordCircle = self.__Plateau.generateCoordCircle(value[0][0], value[0][1], self.__rayon*1.2)
        #polygon
        self.__canvasPlateau.create_polygon(listCoordCorner, fill="", outline=self.__colorPlayer, width=0.2*self.__rayon)
        
        #cercle
        self.__canvasPlateau.create_oval(listCoordCircle, fill="", outline=self.__colorPlayer, width=0.3*self.__rayon)
        
        
    def changePlayer(self):
        """
        Role : Changement de joueur
        """ 
        if self.__player == self.__player1:
            self.__player = self.__player2
            self.__colorPlayer = self.__colorPlayer2
        else:
            self.__player = self.__player1
            self.__colorPlayer = self.__colorPlayer1
    
    def winner(self):
            if self.player2total == 18 and self.player2total == 18:
                    showinfo('Match Nul !!', 'Félicitations à vous deux !')
            elif self.player1total > self.player2total :
                    showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
            elif self.player1total == self.player2total :
                    showinfo('Match Nul !!', 'Félicitations à vous deux !')
            elif self.player1total < self.player2total :
                    showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')

                
    def checkbord(self):
        """
        Role : Fin de partie par réalisation d'une chaîne entre deux bords opposés 
        """
        for vert in self.__droite_vert1:
            for vert2 in self.__droite_vert2:
                    for vert3 in self.__gauche_vert1:
                        for vert4 in self.__gauche_vert2:
                            if vert in self._player1detect and vert3 in self._player1detect and len(self._player1detect) >= 7 :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                                
                            elif vert in self._player2detect and vert3 in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif vert2 in self._player1detect and vert3  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif vert2 in self._player2detect and vert3  in self._player2detect and len(self._player2detect) >= 7   :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif  vert in self._player1detect and vert4 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif vert in self._player2detect and vert4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif vert2 in self._player1detect and vert4  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif vert2 in self._player2detect and vert4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Vert Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
        for oran in self.__up_orange1:
            for oran2 in self.__up_orange2:
                    for oran3 in self.__down_orange1:
                        for oran4 in self.__down_orange2:
                            if oran in self._player1detect and oran3 in self._player1detect  and len(self._player1detect) >= 7 :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                                
                            elif oran in self._player2detect and oran3 in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif oran2 in self._player1detect and oran3  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif oran2 in self._player2detect and oran3  in self._player2detect and len(self._player2detect) >= 7   :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif  oran in self._player1detect and oran4 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif oran in self._player2detect and oran4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif oran2 in self._player1detect and oran4  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif oran2 in self._player2detect and oran4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Orange Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
        for blue in self.__up_blue1:
                for blue2 in self.__up_blue2:
                    for blue3 in self.__down_blue1:
                        for blue4 in self.__down_blue2:
                            if blue in self._player1detect and blue3 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                                
                            elif blue in self._player2detect and blue3 in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif blue2 in self._player1detect and blue3  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif blue2 in self._player2detect and blue3  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif  blue in self._player1detect and blue4 in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif blue in self._player2detect and blue4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')
                                
                            elif blue2 in self._player1detect and blue4  in self._player1detect and len(self._player1detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : White")
                                showinfo('Victoire','Félicitations au joueur WHITE, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois Black ! ')
                            
                            elif blue2 in self._player2detect and blue4  in self._player2detect and len(self._player2detect) >= 7  :
                                print("Jonction entre deux bord Blue Player : Black")
                                showinfo('Victoire','Félicitations au joueur BLACK, vous êtes maintenant un KamonSamurai, bonne chance la prochaine fois WHITE !')



#------------------------------------  Affichage du plateau ------------------------------------ #
    
    def AffichagePlateau(self):
        self.__canvasPlateau.delete(ALL)
        for value in self.__dic.values():
            listCoordCorner = self.__Plateau.generateCoordCorner(value[0][0], value[0][1], self.__rayon)
            listCoordCircle = self.__Plateau.generateCoordCircle(value[0][0], value[0][1], self.__rayon)
            self.__canvasPlateau.create_polygon(listCoordCorner, fill=self.__bgCase, outline=self.__colorPlateau, width=self.__borderdWidth)
            self.__canvasPlateau.create_oval(listCoordCircle, fill=value[1][1], width=0)
            self.__canvasPlateau.create_image(value[0][0], value[0][1], image=value[1][0])
            self.__canvasPlateau.create_polygon(listCoordCorner, fill="", outline=self.__colorPlateau, width=self.__borderdWidth, activeoutline="yellow")
            self.__canvasPlateau.create_line(1250, 300, 650, 0,width=10, fill="#fc870c") #haut2 orange
            self.__canvasPlateau.create_line(180,0,180,1200,width=10, fill="#619456") #Verticale1 #green
            self.__canvasPlateau.create_line(1030,0,1030,1200,width=10, fill="#619456") #Verticale2
            self.__canvasPlateau.create_line(0,645,1200,1200,width=10, fill="#fc870c")#bas1 orange
            self.__canvasPlateau.create_line(0,300,560,0,width=10, fill="#616CA3") #haut1 blue
            self.__canvasPlateau.create_line(1700,400,560,945,width=10, fill="#616CA3")#bas2
        self.__canvasPlateau.update()



    


